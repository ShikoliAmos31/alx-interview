#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""
import sys
import re
from typing import Dict


pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - ' +\
          r'\[([\d-]+\s[\d:.]+)\] "GET /projects/260 HTTP/1.1" ' +\
          r'(?P<status_code>\d{3}) (?P<file_size>\d+)'
counter = 0
results = {}
total_file_size = 0
valid_status_codes = [200, 301, 400, 401, 403, 404, 405, 500]


def print_stats(stats: Dict[int, str], total_file_size: int) -> None:
    """ print all items in a dictionary. """
    print("File size:", total_file_size)

    for key, value in stats:
        print("{}: {}".format(key, value))


if __name__ == '__main__':
    try:
        for line in sys.stdin:
            counter += 1
            pattern_match = re.match(pattern, line)
            status_code = pattern_match.group("status_code")

            try:
                status_code = int(status_code)
            except ValueError:
                status_code = ""

            if pattern_match and status_code in valid_status_codes:
                total_file_size += int(pattern_match.group("file_size"))
                results[status_code] = results.get(status_code, 0) + 1

            if counter == 10:
                print_stats(sorted(results.items()), total_file_size)
                counter = 0

    finally:
        print_stats(sorted(results.items()), total_file_size
