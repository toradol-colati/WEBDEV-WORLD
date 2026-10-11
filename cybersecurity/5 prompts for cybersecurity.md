in general, before launching, always prompt "run a full security audit and report any remaining vulnerabilities"

- rate limiting (max 5 attempts per 15 mins on login routes) on all endpoints
- hide/remove hardcoded API keys, tokens and passwords, from the entire codebase
- move all sensitive data to environment variables in order to expose nothing on frontend nor commit it to github
- sanitize all user inputs and reject anything oversized or malformed