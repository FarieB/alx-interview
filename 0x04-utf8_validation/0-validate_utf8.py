#!/usr/bin/python3
"""Method that determines if a given data set represents
a valid UTF-8 encoding"""

def validUTF8(data):
    remaining_bytes = 0

    for num in data:
        binary = format(num, "#010b")[-8:]  # Get the last 8 bits

        if remaining_bytes == 0:
            # Count the leading 1s to determine the character's byte length
            leading_ones = sum(1 for bit in binary if bit == '1')
            if leading_ones == 0:
                continue  # 1-byte character (ASCII)
            if leading_ones == 1 or leading_ones > 4:
                return False  # Invalid leading byte

            remaining_bytes = leading_ones - 1  # Adjust for continuation bytes
        else:
            # Check if it’s a valid continuation byte (starts with '10')
            if not (binary.startswith('10')):
                return False

        remaining_bytes -= 1

    return remaining_bytes == 0
