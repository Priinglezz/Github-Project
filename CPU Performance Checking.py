#Monitor System Performance (CPU, RAM). You can create scripts to monitor system performance such as CPU usage, memory, and disk space.

import psutil

# CPU usage
print(f"CPU Usage: {psutil.cpu_percent()}%")

# Memory usage
memory = psutil.virtual_memory()
print(f"Memory Usage: {memory.percent}%")
