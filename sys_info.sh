#!/bin/bash

echo "🔐 Current User: $(whoami)"
echo "⏱️ Uptime: $(uptime -p)"
echo "💽 Disk Usage:"
df -h /

echo ""
echo "🧠 Memory Usage:"
free -m | head -2

echo ""
echo "🔥 Top 5 CPU Processes:"
ps -eo pid,user,%cpu,comm --sort=-%cpu | head -n 6

echo ""
echo "End of Script $(date)"
