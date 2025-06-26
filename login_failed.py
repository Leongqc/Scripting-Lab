#!/usr/bin/env python3

#log_file = "/var/log/auth.log"  # For Debian/Ubuntu
log_file = "/var/log/secure"  # For RHEL/CentOS

with open(log_file, "r") as f:
    for line in f:
        if "Failed password" in line:
            parts = line.split()
            time = " ".join(parts[0:3])
            ip = parts[-4]
            user_index = parts.index("for") + 1
            username = parts[user_index]
            port = parts[-2]
            service = parts[-1]
            print(f"\nFailed login detected:")
            print(f"Time: {time}")
            print(f"Username: {username}")
            print(f"IP Address: {ip}")
            print(f"From Port: {port}")
            print(f"To Service: {service}")
