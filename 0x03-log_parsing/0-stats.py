#!/usr/bin/python3
import sys

# Initializes variables to store total file size and status code counts
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

def print_stats():
    """Print the accumulated statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

try:
    line_count = 0
    for line in sys.stdin:
        # Splits the line and extract the file size and status code
        parts = line.split()
        if len(parts) > 6:
            try:
                status_code = int(parts[-2])
                file_size = int(parts[-1])
                
                # Updates total file size
                total_size += file_size
                
                # Updates status code count if it's valid
                if status_code in status_codes:
                    status_codes[status_code] += 1
                
                line_count += 1

                # Prints stats every 10 lines
                if line_count % 10 == 0:
                    print_stats()

            except (ValueError, IndexError):
                # Skips the line if there's an error in conversion
                continue
except KeyboardInterrupt:
    # Prints stats on keyboard interruption (Ctrl + C)
    print_stats()
    raise
