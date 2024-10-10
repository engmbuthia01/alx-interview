#!/usr/bin/python3
"""
A module for lockboxes
"""


def canUnlockAll(boxes):
    """
    determines if all the boxes
    can be opened
    """
    n = len(boxes)
    unlocked = {0}
    keys = boxes[0][:]

    while keys:
        key = keys.pop()
        if key < n and key not in unlocked:
            unlocked.add(key)
            keys.extend(boxes[key])
    return len(unlocked) == n
