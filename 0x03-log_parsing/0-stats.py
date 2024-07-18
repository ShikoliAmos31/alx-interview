#!/usr/bin/python3
"""
Log parsing script that reads from stdin and computes metrics.
"""

import sys
import signal

def print_stats(total_size, status_codes):
    """
    Print the accumulated metrics.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """
    Signal handler to catch keyboard interrupt and print stats before exiting.
    """
    print_stats(total_size, status_codes)
    sys.exit(0)

if __name__ == "__main__":
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    # Register signal handler for keyboard interruption
    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) < 7:
                continue

            # Extract status code and file size from the line
            try:
                status_code = int(parts[-2])
                file_size = int(parts[-1])
            except (ValueError, IndexError):
                continue

            # Update metrics
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1

            line_count += 1

            # Print metrics every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_codes)
