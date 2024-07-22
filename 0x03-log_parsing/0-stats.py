#!/usr/bin/python3
import sys
import signal
import re

# Initialize variables
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Regular expression for parsing log lines
log_pattern = re.compile(r'\S+ - \[.*?\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)')

def print_stats():
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Set up signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

# Read from stdin line by line
try:
    for line in sys.stdin:
        match = log_pattern.match(line)
        if match:
            status_code = int(match.group(1))
            file_size = int(match.group(2))
            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1
        line_count += 1
        if line_count % 10 == 0:
            print_stats()
except Exception as e:
    pass
finally:
    print_stats()
