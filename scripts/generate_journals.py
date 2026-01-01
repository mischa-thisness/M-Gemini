#!/usr/bin/env python3
import json
import os
from pathlib import Path
from datetime import datetime
from collections import defaultdict

def get_time_of_day(hour):
    if 5 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 18:
        return "Day"
    else:
        return "Night"

def summarize_session(messages):
    interactions = []
    current_user_prompt = None

    for msg in messages:
        msg_type = msg.get('type')
        content = msg.get('content', '').strip()

        if msg_type == 'user':
            # Extract first line/core command as prompt summary
            current_user_prompt = content.split('\n')[0][:120].strip()
        elif msg_type == 'gemini' and current_user_prompt:
            # Identify core utility: Tool usage or text response
            tool_calls = msg.get('toolCalls', [])
            if tool_calls:
                tools = list(dict.fromkeys([t.get('name') for t in tool_calls]))
                action = f"Invoke {', '.join(tools)}"
            else:
                action = "Technical response"
            
            interactions.append(f"- **Prompt:** {current_user_prompt} | **Utility:** {action}")
            current_user_prompt = None

    if not interactions:
        return "- Background/System session"
        
    return "\n".join(interactions)

def main():
    repo_root = Path("/home/mischa/M-Gemini")
    chat_logs_dir = repo_root / "chat_logs"
    journals_dir = repo_root / "journals"
    
    json_files = sorted(list(chat_logs_dir.glob("*.json")))
    
    daily_data = defaultdict(lambda: defaultdict(list))
    
    for json_file in json_files:
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except:
            continue
            
        start_time_str = data.get('startTime')
        if not start_time_str:
            continue
            
        start_time = datetime.fromisoformat(start_time_str.replace('Z', '+00:00'))
        date_str = start_time.strftime('%Y-%m-%d')
        hour = start_time.hour
        period = get_time_of_day(hour)
        
        daily_data[date_str][period].append({
            'timestamp': start_time.strftime('%H:%M'),
            'summary': summarize_session(data.get('messages', []))
        })
        
    for date_str, periods in daily_data.items():
        filename = f"{date_str}.md"
        filepath = journals_dir / filename
        
        content = f"# Journal - {date_str}\n\n"
        
        # Combine all entries chronologically
        all_entries = []
        for p in ["Morning", "Day", "Night"]:
            all_entries.extend(periods[p])
        
        all_entries.sort(key=lambda x: x['timestamp'])
        
        if all_entries:
            for entry in all_entries:
                content += f"**{entry['timestamp']}**\n{entry['summary']}\n\n"
        else:
            content += "No collaboration recorded.\n\n"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
    print(f"Generated {len(daily_data)} journal entries in {journals_dir}")

if __name__ == "__main__":
    main()
