def min_moves(list1):
    removed = 0
    while len(list1)>0:
        if len(set(list1)) == len(list1):
            return removed
        else:
            list1.pop(0)
            removed += 1
    return -1