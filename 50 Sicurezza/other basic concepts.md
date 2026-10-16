- strictly lock each user in its own UUID
- password resete-links expiretion
- error handling with custom error screens for every failure states

### other things
- add hsts
- add csrf tokens
- tighten CORS
- disable production debugging
- update patch dependencies
- reset session on password change
- expire reset links
- prevent user enumeration
- whitelist upload types
- verify payment webhooks
- set prices server-side
- enforce permission server-side
- block prompt injection
- cap AI usage
- limit request size
- rate limit password resets
- sanitize before storing
- lock down cors
- disable directory listing
- remove default admin routes
- protect admin routes
- lock accounts after a couple of failed logins
- log security events
- set secure cookie flags
- restrict database permissions
- enable raw level security
- keep auth tokens out of the local storage
- remove sensitive data out of the log
- keep .env off github
- validate file uploads
- 

- Hide API keys
- keep API secrets server-side
- remove secret keys from the server
- enforce paywall server-side
- Rate limit login
- Purge Git secrets
- Add bot protection
- Use public DB key
- Parameterize queries
- Enable row-level security
- Validate all input
- Encrypt sensitive data
- Escape user content
- Enforce server-side auth
- Restrict file uploads
- Lockrecord access
- Trim APi responses
- Block field tampering
- Add security headers
- Secure session cookies
- Force HTTPS
- Hash passwords
- Scan dependencies

- block XSS (basically, maybe, remove session tokens/jwts from localstorage and move them to httpOnly, Secure, SameSite=Strict cookies)
- Rate limits
- CSRF
- Exposed environments
- Insecure file uploads
- Default credentials
- Path traversal
- Unsigned webhooks
- verify webhooks
- SSRF
- FE Payment checks
- Broken password reset 
- IDOR / BOLA
- Weak session mgmt
- APis + user input
- JWT secrets
- Exposed logs
- Permissive CORS
- Exposed source maps
- verify email addresses

---
%% Sezione aggiunta da AI il 2026-10-16. Tutto il testo sopra è il tuo originale, non modificato. %%
## Collegamenti
- Indice: [[MOC Sicurezza]]
- [[prompts for cybersecurity]]: prompt per applicare questa checklist
- [[zero-knowledge passwords]]: password e 2FA
- [[AI for cybersecurity]]: strumenti di audit
- [[on backend]]: JWT, OAuth, rate limiting
- [[XML injection]]: validazione input

> [!warning] Da verificare (nota aggiunta da AI)
> "enable raw level security" va letto **row**-level security. "remove secret keys from the server" contraddice "keep API secrets server-side": probabilmente era "dal client". "Use public DB key" si riferisce alla chiave pubblica (anon) di servizi come Supabase, sicura solo se le row-level security sono attive. Alcune voci sono ripetute più volte (CORS, HTTPS, rate limit, webhook, row-level security).
