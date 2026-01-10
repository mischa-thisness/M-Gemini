# M-Gemini

Automated archival and security engine for Gemini CLI sessions. Captures, sanitizes, and formats execution history.

## Architecture

*   **Ingestion**: Syncs raw protobuf/JSON logs from `~/.gemini/tmp`.
*   **Sanitization**: In-flight regex-based redaction (PII, API Keys, Secrets) via `sync_raw_logs.py`.
*   **Formatting**: JSON-to-Markdown conversion preserving tool calls and thought processes.
*   **Journaling**: Chronological daily summaries.

## Usage

```bash
# 1. Sync and Redact
python3 scripts/sync_raw_logs.py

# 2. Generate Artifacts
python3 scripts/convert_to_markdown.py
python3 scripts/generate_journals.py
python3 scripts/combine_chat_logs.py
```

## Structure

*   `chat_logs/`: Redacted raw JSON sessions.
*   `chat_logs_markdown/`: Rendered session logs.
*   `journals/`: Daily operational summaries.
*   `antigravity-data/`: Raw Protobuf backups.
*   `FULL_CHAT_LOG.md`: Master chronological record.