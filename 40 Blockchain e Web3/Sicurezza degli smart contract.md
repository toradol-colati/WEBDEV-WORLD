---
autore: ai
stato: non-verificato
creato: 2026-10-16
tags: [blockchain, sicurezza]
---

# Sicurezza degli smart contract

Nota scheletro da completare. Collegata a [[other basic concepts]] e [[prompts for cybersecurity]].

## Vulnerabilità classiche
- Reentrancy
- Controllo accessi mancante o sbagliato
- Manipolazione degli oracle e dei prezzi
- Front-running e MEV
- Overflow (gestito di default da Solidity 0.8+), errori di arrotondamento
- Firme riutilizzabili (replay)

## Pratiche
- Usare librerie testate (OpenZeppelin)
- Test approfonditi e fuzzing (Foundry)
- Analisi statica (Slither)
- Audit esterni prima del lancio
- Contratti aggiornabili (proxy) solo se servono, con i loro rischi

Indice: [[MOC Blockchain]]
