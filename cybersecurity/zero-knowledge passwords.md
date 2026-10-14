aka high-level one way hashing ≠ storing reversable passwords

the point is to never actually be able to see users' passwords: you have encrypted passwords stored; after the user inserts its credentials the same encryption function encrypts the input and confronts it with the stored encrypted password...if they corresponds is ok, if they don't then they don't.

## also implement:
- 2 factor authentication (or an OTP functionality) (with appropriate rate limiting)

## password management
- try bitwarden (on github)