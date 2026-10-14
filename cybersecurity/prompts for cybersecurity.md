in general, before launching, always prompt "run a full security audit and report any remaining vulnerabilities"

- rate limiting (max 5 attempts per 15 mins on login routes) on all endpoints
- hide/remove hardcoded API keys, tokens and passwords, from the entire codebase
- move all sensitive data to environment variables in order to expose nothing on frontend nor commit it to github
- sanitize all user inputs and reject anything oversized or malformed

For secure authentication
    "Act as a senior security engineer. Review the authentication system of this project and make it secure. Ensure passwords are securely hashed, sessions expire, email verification is enabled, password reset tokens expire, login attempts are rate limited, and authentication secrets are never exposed to the frontend. Refactor any insecure authentication logic!"

To implement data isolation
    "Review all API endpoints and database queries. Ensure every request verifies the logged-in user owns the data being accessed. Prevent insecure direct object reference (IDOR) vulnerabilities by enforcing ownership checks before reading, modifying, or deleting any resource!"

For secure deployment & monitoring in order to prevent abuse & bots attacks
    "Configure the application for secure deployment. Enforce HTTPS, ensure secrets are stored securely, restrict direct database access from the public internet, and add logging for authentication attempts, API errors, and unusual traffic patterns so suspicious behavior can be detected."

To protect secrets and API keys
    "Scan the entire project for secrets and credentials. Ensure API keys, database service keys, and tokens are never exposed in frontend code or committed to the repository. Move all secrets to secure environment variables and ensure they are only used on the server."

To validate & sanitize user input
    "Identify every place where user input enters the system including forms, APIs, uploads, and query parameters. Add strict validation and sanitization to prevent SQL injection, command injection, script injection, and unsafe file uploads. Reject invalid data and enforce strict input types."

just launch a claude code /security-review ([[on AI skills and developing environments setup/Claude]])