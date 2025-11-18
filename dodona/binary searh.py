def binarysearch(sorted: list, x: int):
    low = 0
    high = len(sorted) - 1

    while high >= low:
        mid = (low + high) // 2
        if x < sorted[mid]:
            high = mid - 1
        elif x == sorted[mid]:
            return mid
        else:
            low = mid + 1
    