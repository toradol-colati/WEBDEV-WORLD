#!/usr/bin/env python3
"""Guardiano del vault WEBDEV-WORLD.

Eseguito da Claude Code prima di ogni Edit, MultiEdit, Write e Bash.
Regola: Claude puo' solo AGGIUNGERE testo alle note esistenti, mai toglierlo
o riscriverlo, e non puo' cancellare o sovrascrivere file.
Exit 2 = azione bloccata; il messaggio su stderr torna a Claude.
"""
import json
import os
import re
import sys

PROTETTI = (".obsidian", "_backup", ".git")
CONFIG_PROTETTA = (os.path.join(".claude", "settings.json"),
                   os.path.join(".claude", "hooks"))

# Comandi che cancellano, svuotano o sovrascrivono file.
COMANDI_VIETATI = [
    (r"\b(rm|rmdir|unlink|shred|truncate)\b", "cancella file"),
    (r"-delete\b", "cancella file"),
    (r"\b(sed|perl|ruby)\b[^|;&]*\s-[a-zA-Z]*i", "riscrive file sul posto"),
    (r"\bgit\s+(rm|clean|restore|stash)\b", "puo' far sparire modifiche o file"),
    (r"\bgit\s+reset\b[^|;&]*--hard", "cancella modifiche"),
    (r"\bgit\s+checkout\b[^|;&]*\s--(\s|$)", "sovrascrive file"),
    (r"\bgit\s+push\b[^|;&]*(\s-f\b|--force)", "riscrive la cronologia remota"),
    (r"\bgit\s+(rebase|filter-branch|filter-repo)\b", "riscrive la cronologia"),
    (r"(?<![>&\d])>(?!>)\s*[^\s>|&;]*", "sovrascrive un file con >"),
]


def blocca(msg):
    print("BLOCCATO dal guardiano del vault: " + msg, file=sys.stderr)
    sys.exit(2)


def controlla_bash(cmd):
    # Ignora i redirect innocui verso /dev/null e tra descrittori (2>&1).
    pulito = re.sub(r"\d?>\s*/dev/null|\d?>&\d", " ", cmd)
    for schema, motivo in COMANDI_VIETATI:
        if re.search(schema, pulito):
            blocca(f"il comando {motivo}. In questo vault non si cancella "
                   "e non si sovrascrive nulla. Per aggiungere testo usa Edit; "
                   "per scrivere su file usa >> (accoda) solo su file nuovi.")
    # mv e cp possono sovrascrivere la destinazione: obbligatorio -n.
    for m in re.finditer(r"(?<!git )\b(mv|cp)\b([^|;&]*)", pulito):
        opzioni = re.findall(r"\s-([a-zA-Z]+)", m.group(2))
        if not any("n" in o for o in opzioni):
            blocca(f"usa '{m.group(1)} -n' così non sovrascrive file già esistenti.")


def main():
    try:
        d = json.load(sys.stdin)
    except Exception:
        blocca("impossibile leggere la richiesta, per sicurezza blocco.")

    tool = d.get("tool_name", "")
    ti = d.get("tool_input", {}) or {}

    if tool == "Bash":
        controlla_bash(ti.get("command", ""))
        sys.exit(0)

    path = ti.get("file_path") or ""
    if not path:
        sys.exit(0)
    radice = os.environ.get("CLAUDE_PROJECT_DIR") or d.get("cwd") or "."
    rel = os.path.normpath(os.path.relpath(os.path.abspath(path), radice))

    if rel.split(os.sep)[0] in PROTETTI:
        blocca(f"'{rel}' e' una cartella protetta.")
    if any(rel == p or rel.startswith(p + os.sep) for p in CONFIG_PROTETTA):
        blocca(f"'{rel}' e' la configurazione del guardiano: la modifica solo Bubi a mano.")

    if not os.path.exists(path):
        sys.exit(0)  # file nuovo: via libera

    if tool == "Write":
        try:
            vecchie = open(path, encoding="utf-8").read().splitlines()
        except UnicodeDecodeError:
            blocca(f"'{rel}' non e' un file di testo: non lo sovrascrivo.")
        nuove = set(ti.get("content", "").splitlines())
        perse = [r for r in vecchie if r.strip() and r not in nuove]
        if perse:
            blocca(f"la scrittura di '{rel}' toglierebbe {len(perse)} righe esistenti, "
                   f"ad esempio: «{perse[0][:120]}». Puoi solo aggiungere testo.")
        sys.exit(0)

    if tool in ("Edit", "MultiEdit"):
        modifiche = ti.get("edits", []) if tool == "MultiEdit" else [ti]
        for m in modifiche:
            vecchio = m.get("old_string", "")
            if vecchio not in m.get("new_string", ""):
                blocca(f"la modifica a '{rel}' toglie o riscrive testo esistente: "
                       f"«{vecchio[:120]}». Puoi solo aggiungere testo: scrivi sotto "
                       "un marcatore %% Sezione aggiunta da AI %% oppure segnala il "
                       "problema in un callout, lasciando l'originale com'e'.")
    sys.exit(0)


if __name__ == "__main__":
    main()
