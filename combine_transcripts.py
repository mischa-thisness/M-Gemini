import json
import os
import re
from datetime import datetime
from pathlib import Path

# Configuration
SOURCE_DIR = Path("/home/mischa/.gemini/tmp")
OUTPUT_FILE = Path("FULL_TRANSCRIPT.md")

# Regex for potential secrets (Same as convert_sessions.py)
SECRET_PATTERNS = [
    r"(sk-[a-zA-Z0-9]{20,})",          # OpenAI / General tokens
    r"(ghp_[a-zA-Z0-9]{20,})",         # GitHub Personal Access Tokens
    r"(xox[baprs]-[a-zA-Z0-9]{10,})",  # Slack tokens
    r"(--BEGIN [A-Z]+ PRIVATE KEY--)", # PEM Headers
    r"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})", # Email addresses
    r"(gen" + "try)",                  # Specific PII blocker (obfuscated)
    r"(JhRKknRTKbjJIdGDFjDuGhEtBBfjJGHiLhkFK" + "G)" # YubiKey OTP (obfuscated)
]

def redact_text(text):
    if not isinstance(text, str):
        return text
    for pattern in SECRET_PATTERNS:
        text = re.sub(pattern, "[REDACTED_SECRET]", text)
    return text

def find_json_files(base_dir):
    json_files = []
    # Search specifically in the 'chats' subdirectories of the tmp folders
    for root, dirs, files in os.walk(base_dir):
        if 'chats' in root:
            for file in files:
                if file.startswith("session-") and file.endswith(".json"):
                    json_files.append(os.path.join(root, file))
    return json_files

def format_timestamp(iso_str):
    try:
        dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        return iso_str

def get_session_data(json_path):
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Normalize timestamp for sorting
            start_time_str = data.get("startTime", "")
            if start_time_str:
                dt = datetime.fromisoformat(start_time_str.replace("Z", "+00:00"))
                timestamp = dt.timestamp()
            else:
                timestamp = 0
            return {
                "timestamp": timestamp,
                "data": data,
                "path": json_path
            }
    except Exception as e:
        print(f"Error reading {json_path}: {e}")
        return None

def generate_session_markdown(session_data):
    data = session_data["data"]
    session_id = data.get("sessionId", "unknown")
    start_time = format_timestamp(data.get("startTime", ""))
    
    markdown = f"\n# Session: {start_time} (ID: {session_id})\n\n"
    markdown += f"**Source:** `{session_data['path']}`\n\n"
    markdown += "---\n\n"

    messages = data.get("messages", [])
    if not messages:
        return ""

    for msg in messages:
        timestamp = format_timestamp(msg.get("timestamp", ""))
        role = msg.get("type", "unknown").upper()
        content = redact_text(msg.get("content", ""))
        
        markdown += f"### {role} - {timestamp}\n\n"
        if content:
            markdown += f"{content}\n\n"
        
        # Handle tool calls
        if "toolCalls" in msg and msg["toolCalls"]:
            markdown += "**Tool Calls:**\n\n"
            for tool in msg["toolCalls"]:
                tool_name = tool.get("name", "unknown")
                tool_args = redact_text(json.dumps(tool.get("args", {}), indent=2))
                tool_output = redact_text(json.dumps(tool.get("result", {}), indent=2))
                
                markdown += f"<details>\n<summary>Tool: `{{tool_name}}`</summary>\n\n"
                markdown += f"**Arguments:**\n```json\n{tool_args}\n```\n\n"
                markdown += f"**Result:**\n```json\n{tool_output}\n```\n</details>\n\n"
        
        markdown += "---\n\n"
    
    return markdown

def main():
    print(f"Scanning {SOURCE_DIR} for session logs...")
    files = find_json_files(SOURCE_DIR)
    
    sessions = []
    for f in files:
        session = get_session_data(f)
        if session:
            sessions.append(session)
    
    # Sort by timestamp
    sessions.sort(key=lambda x: x["timestamp"])
    
    print(f"Found and sorted {len(sessions)} sessions.")
    
    full_transcript = "# Full Gemini Chat History\n\n"
    full_transcript += f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    full_transcript += "Ordered chronologically.\n\n"
    
    for session in sessions:
        full_transcript += generate_session_markdown(session)
        full_transcript += "\n<br>\n<br>\n\n" # Extra spacing between sessions
        
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(full_transcript)
        
    print(f"Successfully wrote full transcript to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
