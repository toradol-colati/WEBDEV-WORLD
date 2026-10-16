---
name: chiedi-al-vault
description: Risponde a "cosa dice WEBDEV-WORLD su X" cercando nelle note del vault e citandole con link. Usala quando Bubi chiede cosa contengono le sue note su un argomento, in quale nota aveva salvato qualcosa, o quando una risposta può partire da ciò che il vault già contiene.
argument-hint: <argomento o domanda>
context: fork
agent: Explore
---

Domanda: $ARGUMENTS

Rispondi usando SOLO le note di questo vault Obsidian. Non modificare, spostare o creare nessun file.

## Come cercare

1. Trasforma la domanda in parole chiave, in italiano E in inglese (le note mescolano le due lingue), più sinonimi e nomi di strumenti (es. "SEO" → seo, search console, indicizzazione, ranking, google).
2. Cerca senza distinzione di maiuscole nei file `.md`, escludendo `.obsidian/`, `.git/`, `_backup/` e `.claude/`:
   - nel testo delle note;
   - nei nomi dei file;
   - nei MOC (`MOC *.md`) e in `01 Home.md`, per capire in che area sta l'argomento.
3. Leggi per intero le note che corrispondono (sono brevi) e segui i `[[link]]` utili fino a un livello.

## Come rispondere (in italiano)

- **In breve**: 2-4 righe con quello che il vault dice sull'argomento.
- **Dove sta**: per ogni nota usata, `[[Nome nota]]` (cartella) e il punto rilevante, citato tra virgolette quando è utile.
- **Attenzione**: segnala doppioni tra note, contraddizioni, link interni rotti, e note con `stato: non-verificato` o `da-verificare` (il contenuto viene dai social e non è verificato).
- Tieni separato quello che dice il vault da quello che sai tu: se aggiungi qualcosa di tuo, mettilo sotto **Fuori dal vault** e dillo chiaramente.
- Se il vault non dice nulla, rispondi "Nel vault non c'è niente su questo" e indica in quale area/MOC andrebbe una nota sull'argomento.
