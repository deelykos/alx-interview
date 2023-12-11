def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
    - boxes (List[List[int]]): A list of lists, where each list represents a box and contains keys to other boxes.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """

    # Set to keep track of visited boxes
    visited = set()
    # Stack to perform depth-first search
    stack = [0]

    while stack:
        current_box = stack.pop()

        # If the current box has not been visited
        if current_box not in visited:
            # Mark the box as visited
            visited.add(current_box)
            
            # Add keys from the current box to the stack
            stack.extend(boxes[current_box])

    # Check if all boxes have been visited
    return len(visited) == len(boxes)
