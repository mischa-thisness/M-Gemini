# M-Gemini ♊️

A comprehensive archive and toolkit for **Gemini CLI** session history, transcripts, and analysis tools. This repository serves as a personal knowledge base derived from interactions with Google's Gemini CLI agent.

## 📂 Repository Structure

- **`FULL_TRANSCRIPT.md`**
  A single, chronologically ordered master transcript of all recorded sessions. Ideal for searching through entire conversation histories.

- **`transcripts/`**
  Individual Markdown files for each session, named by their unique Session ID.
  - Contains full conversation logs.
  - Includes tool calls, arguments, and outputs.
  - Metadata such as timestamps and user roles.

- **`scripts/`** (Root directory scripts)
  - `convert_sessions.py`: Parses raw JSON logs from the Gemini CLI temporary directory and converts them into readable Markdown.
  - `combine_transcripts.py`: Aggregates all individual session logs into the master `FULL_TRANSCRIPT.md`.

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