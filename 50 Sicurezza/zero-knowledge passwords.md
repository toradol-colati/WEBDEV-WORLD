aka high-level one way hashing ≠ storing reversable passwords

the point is to never actually be able to see users' passwords: you have encrypted passwords stored; after the user inserts its credentials the same encryption function encrypts the input and confronts it with the stored encrypted password...if they corresponds is ok, if they don't then they don't.

## also implement:
- 2 factor authentication (or an OTP functionality) (with appropriate rate limiting)

## password management
- try bitwarden (on github)

---
%% Sezione aggiunta da AI il 2026-10-16. Tutto il testo sopra è il tuo originale, non modificato. %%
## Collegamenti
- Indice: [[MOC Sicurezza]]
- [[other basic concepts]]: checklist sicurezza
- [[prompts for cybersecurity]]: prompt per l'autenticazione
- [[on backend]]: auth lato backend

> [!warning] Da verificare (nota aggiunta da AI)
> Quello descritto è il normale **hashing delle password**, non "zero-knowledge". Le password non si criptano (la crittografia è reversibile): si fa l'hash con salt usando un algoritmo lento apposito (Argon2id, bcrypt, scrypt). Zero-knowledge è un'altra cosa, per esempio un password manager dove il server non vede mai i dati in chiaro. Titolo suggerito: "Hashing delle password e 2FA".
