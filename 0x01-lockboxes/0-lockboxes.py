#!/usr/bin/python3
"""
0-lockboxes
"""

def canUnlockAll(boxes):
    opened = [0]
    keys = set(boxes[0])

    while keys:
        new_key = keys.pop()
        if new_key < len(boxes) and new_key not in opened:
            opened.append(new_key)
            keys.update(boxes[new_key])

    return len(opened) == len(boxes)
