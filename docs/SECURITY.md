# Security Policy

## Protocol

*   **Private Reporting Only**: Do not disclose vulnerabilities via public issues.
*   **No Secrets**: Repository enforces strict exclusion of:
    *   Unredacted `.json`/`.pb` session files.
    *   Environment files (`.env`).
    *   Cryptographic keys/certificates.

## Enforcement

*   **Redaction**: `scripts/sync_raw_logs.py` applies regex masks to PII (Email, Phone, IP) and Secrets (API Keys, Private Keys) during ingestion.
*   **Verification**: Manual audit recommended prior to push.