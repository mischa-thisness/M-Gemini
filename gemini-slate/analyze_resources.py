import re
import os

raw_file = "M-Gemini/gemini-slate/system_data/resource_usage_raw.txt"
report_file = "M-Gemini/gemini-slate/RESOURCE_USAGE_REPORT.md"

def parse_section(content, section_name):
    pattern = f"--- {section_name} ---\n(.*?)(?=\n--- |$)"
    match = re.search(pattern, content, re.DOTALL)
    return match.group(1).strip() if match else ""

def format_bytes(size):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"

with open(raw_file, "r") as f:
    content = f.read()

# --- CPU & Memory (Top) ---
top_output = parse_section(content, "TOP PROCESSES")
# Extract lines, skip headers if typical top output
lines = top_output.splitlines()
# Find the start of the process list (usually contains PID)
start_idx = 0
for i, line in enumerate(lines):
    if "PID" in line and "COMMAND" in line:
        start_idx = i
        break

# Process list (skip header) 
process_lines = lines[start_idx+1:] if start_idx < len(lines) else []
# Parse simplified top output: PID  PPID USER     STAT   VSZ %VSZ %CPU COMMAND
# Note: Busybox top format varies. Often: PID  PPID USER     STAT   VSZ %VSZ CPU %CPU COMMAND
# We'll just take the top few lines as they are usually sorted by CPU/Mem
top_consumers = "\n".join(lines[:15]) # Keep headers + top 10

# --- Storage (/overlay) ---
storage_output = parse_section(content, "STORAGE DUMP")
storage_items = []
for line in storage_output.splitlines():
    parts = line.split('\t')
    if len(parts) == 2:
        try:
            size_kb = int(parts[0])
            path = parts[1]
            storage_items.append((size_kb, path))
        except ValueError:
            continue

# Sort by size descending
storage_items.sort(key=lambda x: x[0], reverse=True)
top_storage = []
for size, path in storage_items[:20]:
    top_storage.append(f"{format_bytes(size * 1024):>10}  {path}")

# --- Packages ---
pkg_output = parse_section(content, "PACKAGE SIZES")
pkg_items = []
for line in pkg_output.splitlines():
    # Format: /usr/lib/opkg/info/pkgname.control:Size: 1234
    match = re.search(r'/([^/]+)\.control:Size:\s*(\d+)', line)
    if match:
        name = match.group(1)
        size = int(match.group(2))
        pkg_items.append((size, name))

pkg_items.sort(key=lambda x: x[0], reverse=True)
top_packages = []
for size, name in pkg_items[:20]:
    top_packages.append(f"{format_bytes(size):>10}  {name}")

report = f"""# Resource Usage Analysis

## Top System Processes (CPU & Memory)
*Snapshot from `top`*
```
{top_consumers}
```

## Storage Consumers (Writable Overlay)
*Top 20 directories/files in `/overlay` (User Data)*
```
{chr(10).join(top_storage)}
```

## Largest Installed Packages
*Based on package metadata (Estimate)*
```
{chr(10).join(top_packages)}
```
"""

with open(report_file, "w") as f:
    f.write(report)

print(f"Report generated: {report_file}")
