# M-Gemini ♊️

A comprehensive archive and toolkit for **Gemini CLI** session history, transcripts, and analysis tools. This repository serves as a personal knowledge base derived from interactions with Google's Gemini CLI agent.

## 📂 Repository Structure

- **`FULL_TRANSCRIPT.md`**
  A single, chronologically ordered master transcript of all recorded sessions. Ideal for searching through entire conversation histories.

- **`transcripts/`**
  Raw JSON logs synchronized from the local Gemini temporary directory. These are redacted versions of the original logs.

- **`transcripts-markdown/`**
  Individual Markdown files for each session, converted from the JSON transcripts.
  - Contains full conversation logs.
  - Includes tool calls, arguments, and outputs.
  - Metadata such as timestamps and user roles.

- **`antigravity-data/`**
  Raw Protocol Buffer (`.pb`) files synced from the local Antigravity storage.

- **`scripts/`**
  - `convert_sessions.py`: Parses raw JSON logs from `transcripts/` (or tmp) and converts them into Markdown.
  - `combine_transcripts.py`: Aggregates sessions into the master `FULL_TRANSCRIPT.md`.
  - `sync_raw_logs.py`: Syncs and redacts logs from the local filesystem to this repository.

- **`docs/`**
  - `SECURITY.md`: Security policies and redaction details.

## 🚀 Usage

### Prerequisites
- Python 3.x
- Access to local Gemini CLI log files (typically in `~/.gemini/tmp/...`)

### Generating Transcripts

1. **Update Transcripts:**
   Run the conversion script to parse new sessions from the local cache:
   ```bash
   python3 convert_sessions.py
   ```

2. **Combine History:**
   Regenerate the master transcript file:
   ```bash
   python3 combine_transcripts.py
   ```

## 🔒 Security & Privacy

This repository implements automated redaction to protect sensitive information.
- **PII Redaction:** Email addresses and specific personal identifiers are automatically masked.
- **Secret Redaction:** Patterns matching API keys, tokens (GitHub, Slack, etc.), and Private Keys are replaced with `[REDACTED_SECRET]`.
- **Pre-commit Hooks:** The repository is configured to reject commits containing specific high-sensitivity strings.

## ℹ️ About Gemini CLI

Gemini CLI is an interactive command-line agent capable of performing software engineering tasks, system administration, and general assistance directly within the terminal. This archive captures the "thought process" and execution steps of the agent.

---
*Generated automatically by M-Gemini tools.*