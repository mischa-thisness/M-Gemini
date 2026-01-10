# M-Gemini

Automated archival and security engine for Gemini CLI sessions. Captures, sanitizes, and formats execution history.

## Architecture

*   **Ingestion**: Syncs raw protobuf/JSON logs from `~/.gemini/tmp`.
*   **Sanitization**: In-flight regex-based redaction (PII, API Keys, Secrets) via `sync_raw_logs.py`.
*   **Processing**: Unified pipeline (`process_logs.py`) for Markdown conversion, journaling, and aggregation.
*   **Storage**: All artifacts stored in `Archives/`.

## Usage

```bash
# 1. Sync and Redact
python3 scripts/sync_raw_logs.py

# 2. Process Logs (Markdown, Journals, Full Log)
python3 scripts/process_logs.py
```

## Structure

*   `Archives/`: Redacted JSON sessions and rendered Markdown logs.
*   `journals/`: Daily operational summaries.
*   `antigravity-data/`: Raw Protobuf backups.
*   `FULL_CHAT_LOG.md`: Master chronological record.