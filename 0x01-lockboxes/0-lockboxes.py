#!/usr/bin/python3
"""
0x01-lockboxes
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
    - boxes (List[List[int]]): A list of lists, where each list
      represents a box and contains keys to other boxes.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
            boxIdx = unseen_boxes.pop()
            if not boxIdx or boxIdx >= n or boxIdx < 0:
                continue
            if boxIdx not in seen_boxes:
                unseen_boxes = unseen_boxes.union(boxes[boxIdx])
                seen_boxes.add(boxIdx)
    return n == len(seen_boxes)