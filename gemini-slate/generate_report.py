import re

dump_file = "M-Gemini/gemini-slate/system_data/full_system_dump.txt"
report_file = "M-Gemini/gemini-slate/SYSTEM_REPORT.md"

def parse_section(content, section_name):
    pattern = f"--- {section_name} ---\n(.*?)(?=\n--- |$)"
    match = re.search(pattern, content, re.DOTALL)
    return match.group(1).strip() if match else "No data found."

def analyze_logs(log_content, log_name):
    issues = []
    # Keywords to search for in logs
    keywords = ["error", "fail", "warn", "crit", "alert", "emerg", "panic", "denied", "segfault"]
    
    for line in log_content.splitlines():
        if any(keyword in line.lower() for keyword in keywords):
            issues.append(line)
    
    return issues

with open(dump_file, "r") as f:
    content = f.read()

processes = parse_section(content, "PROCESSES")
init_scripts = parse_section(content, "INIT SCRIPTS")
enabled_services = parse_section(content, "ENABLED SERVICES")
ubus_services = parse_section(content, "UBUS SERVICES")
disk_usage = parse_section(content, "DISK USAGE")
memory = parse_section(content, "MEMORY")
dmesg_log = parse_section(content, "DMESG")
syslog = parse_section(content, "SYSLOG")

dmesg_issues = analyze_logs(dmesg_log, "Kernel Log")
syslog_issues = analyze_logs(syslog, "System Log")

# Format the report
report = f"""# GL-BE3600 System Health Report

## System Status

### Memory Usage
```
{memory}
```

### Disk Usage
```
{disk_usage}
```

## Running Entities

### Running Processes (Snapshot)
Total processes found: {len(processes.splitlines())}
*(First 20 processes shown for brevity)*
```
{chr(10).join(processes.splitlines()[:21])}
```

### Active Services (Ubus)
Services exposing an interface on the system bus:
```
{ubus_services}
```

### Enabled Init Scripts (Boot)
Services configured to start at boot (/etc/rc.d):
*(First 20 shown)*
```
{chr(10).join(enabled_services.splitlines()[:20])}
...
```

## Log Analysis & Issues

### Kernel Log (dmesg) - Detected Issues
Found **{len(dmesg_issues)}** potential issues (Keywords: error, fail, warn, panic, etc.)

```
{chr(10).join(dmesg_issues[-50:]) if dmesg_issues else "No major issues detected."} 
```
*(Showing last 50 issues if many)*

### System Log (logread) - Detected Issues
Found **{len(syslog_issues)}** potential issues.

```
{chr(10).join(syslog_issues[-50:]) if syslog_issues else "No major issues detected."} 
```
*(Showing last 50 issues if many)

"""

with open(report_file, "w") as f:
    f.write(report)

print(f"Report generated at {report_file}")
