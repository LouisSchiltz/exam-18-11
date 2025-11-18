def zoek(gesorteerd: list, x: int):
    low = 0
    high = len(gesorteerd)

#Indices go from 0 up to len(list) - 1.
    while low < high:
        if gesorteerd[low] != x:
            low += 1
        else:
            return low
    return None



#Other option

def selectionSort(lst):
    for i in range(len(lst) - 1):
        # Find the minimum in lst[i:]
        currentMin = min(lst[i:])
        currentMinIndex = i + lst[i:].index(currentMin)

        # Swap if needed
        if currentMinIndex != i:
            lst[currentMinIndex], lst[i] = lst[i], lst[currentMinIndex]

    return lst





