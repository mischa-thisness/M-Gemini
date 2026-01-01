#!/usr/bin/env python3
"""
Convert Gemini CLI JSON chat logs to beautiful human-readable Markdown.

This script processes conversation chat logs from Gemini CLI and generates
clean, formatted Markdown files that are easy to read and navigate.
"""

import json
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any

def format_timestamp(timestamp_str: str) -> str:
    """Convert ISO timestamp to readable format."""
    try:
        dt = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))
        return dt.strftime('%B %d, %Y at %I:%M:%S %p')
    except:
        return timestamp_str

def format_user_message(msg: Dict[str, Any]) -> str:
    """Format a user message."""
    content = msg.get('content', '')
    return f"**You:** {content}\n\n"

def format_gemini_message(msg: Dict[str, Any]) -> str:
    """Format a Gemini message with thoughts, text, and tool usage."""
    output = []
    
    # Thoughts
    thoughts = msg.get('thoughts', [])
    if thoughts:
        output.append("<details><summary>💭 thoughts</summary>\n")
        for t in thoughts:
            output.append(f"- **{t.get('subject', 'Thought')}**: {t.get('description', '')}\n")
        output.append("</details>\n")

    # Tool Calls
    tool_calls = msg.get('toolCalls', [])
    for tool in tool_calls:
        name = tool.get('name')
        args = tool.get('args', {})
        result = tool.get('result', [])
        
        output.append(f"**Tool Call:** `{name}`")
        output.append(f"```json\n{json.dumps(args, indent=2)}\n```")
        
        if tool.get('resultDisplay'):
            output.append(f"> {tool.get('resultDisplay')}\n")
        elif result:
            output.append(f"> Result received.\n")

    # Content (Text response)
    content = msg.get('content', '')
    if content:
        output.append(f"**Gemini:** {content}\n")

    return '\n'.join(output) + '\n\n'

def convert_json_to_markdown(json_path: Path, output_dir: Path) -> Dict[str, Any]:
    """Convert a single JSON file to markdown."""
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print(f"Error decoding JSON: {json_path}")
        return None

    session_id = data.get('sessionId', json_path.stem)
    timestamp = data.get('startTime', '')
    messages = data.get('messages', [])

    if not messages:
        return None

    # Start building markdown
    md_lines = []
    md_lines.append(f"# {session_id}\n\n")

    # Count messages
    user_count = sum(1 for m in messages if m.get('type') == 'user')
    gemini_count = sum(1 for m in messages if m.get('type') == 'gemini')
    md_lines.append(f"*{format_timestamp(timestamp)} • {user_count} prompts, {gemini_count} responses*\n\n")
    md_lines.append("---\n\n")

    # Process messages
    for msg in messages:
        msg_type = msg.get('type')

        if msg_type == 'user':
            md_lines.append(format_user_message(msg))

        elif msg_type == 'gemini':
            md_lines.append(format_gemini_message(msg))

    # Write markdown file
    md_filename = json_path.stem + '.md'
    md_path = output_dir / md_filename

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(''.join(md_lines))

    return {
        'session_id': session_id,
        'filename': md_filename,
        'timestamp': timestamp,
        'user_messages': user_count,
        'gemini_messages': gemini_count
    }

def create_index(sessions: List[Dict[str, Any]], output_dir: Path):
    """Create an index markdown file."""
    md_lines = [
        "# Gemini CLI Conversations - Markdown Chat Logs\n\n",
        "Beautiful, human-readable versions of all conversation chat logs.\n\n",
        f"**Total Conversations:** {len(sessions)}\n",
        f"**Generated:** {datetime.now().strftime('%B %d, %Y at %I:%M %p')}\n\n",
        "---\n\n",
        "## Conversations\n\n"
    ]

    # Sort by timestamp (newest first)
    sorted_sessions = sorted(
        sessions,
        key=lambda x: x.get('timestamp', ''),
        reverse=True
    )

    for session in sorted_sessions:
        session_id = session['session_id']
        filename = session['filename']
        timestamp = format_timestamp(session.get('timestamp', ''))
        user_msgs = session.get('user_messages', 0)
        gemini_msgs = session.get('gemini_messages', 0)

        md_lines.append(
            f"### [{session_id}]({filename})\n\n"
            f"- **Date:** {timestamp}\n"
            f"- **Messages:** {user_msgs} prompts, {gemini_msgs} responses\n\n"
        )

    md_lines.append("\n---\n\n")
    md_lines.append("*Generated automatically by GitHub Actions*\n")

    index_path = output_dir / 'README.md'
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(''.join(md_lines))

def main():
    """Main conversion process."""
    # Setup paths
    project_root = Path(__file__).parent.parent
    chat_logs_dir = project_root / 'chat_logs'
    output_dir = project_root / 'chat_logs_markdown'

    # Create output directory
    output_dir.mkdir(exist_ok=True)

    # Process all JSON files
    sessions = []
    json_files = list(chat_logs_dir.glob('*.json'))

    print(f"Converting {len(json_files)} JSON files to Markdown...")

    for json_path in json_files:
        session_info = convert_json_to_markdown(json_path, output_dir)
        if session_info:
            sessions.append(session_info)

    # Create index
    print("Creating index...")
    create_index(sessions, output_dir)

    print(f"✓ Converted {len(sessions)} conversations to Markdown")
    print(f"✓ Output directory: {output_dir}")

if __name__ == '__main__':
    main()