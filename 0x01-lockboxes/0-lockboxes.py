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

    # Number of boxes
    n = len(boxes)

    # Set to keep track of seen boxes
    seen_boxes = {0}

    # Set of unseen boxes initially excluding the first box
    unseen_boxes = set(boxes[0]).difference({0})

    while len(unseen_boxes) > 0:
        # Pop a box index from the set of unseen boxes
        boxIdx = unseen_boxes.pop()

        # Check if the box index is valid
        if not (0 <= boxIdx < n):
            continue

        # Check if the box has not been seen
        if boxIdx not in seen_boxes:
            # Add keys from the current box to the set of unseen boxes
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])

            # Mark the current box as seen
            seen_boxes.add(boxIdx)

    return n == len(seen_boxes)