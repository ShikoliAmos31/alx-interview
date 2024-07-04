def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    stack = [0]
    
    while stack:
        box_index = stack.pop()
        for key in boxes[box_index]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)
    
    return all(unlocked)
