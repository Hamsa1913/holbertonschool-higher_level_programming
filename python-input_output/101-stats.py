#!/usr/bin/python3
import sys

def print_stats(total_size, status_counts):
    """Print total file size and status code counts."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        print("{}: {}".format(code, status_counts[code]))

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
status_counts = {}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.strip().split()
        if len(parts) < 7:
            continue
        # Extract status code and file size
        try:
            status = int(parts[-2])
            size = int(parts[-1])
        except ValueError:
            continue

        total_size += size

        if status in status_codes:
            status_counts[status] = status_counts.get(status, 0) + 1

        if line_count % 10 == 0:
            print_stats(total_size, status_counts)

except KeyboardInterrupt:
    pass

finally:
    print_stats(total_size, status_counts)
