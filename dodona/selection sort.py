def selection_sort(mylist):

    n = len(mylist)
    for i in range(n - 1):   #by the time you reach the last item it is already in place
        min_index = i  #start by assuming that the smallest item is at position i
        for j in range(i + 1, n): #Look through the remaining unsorted part of the list
            if mylist[j] < mylist[min_index]: #if you find a smaller element, remember its place
                min_index = j
        min_value = mylist.pop(min_index)  #pop/remove the smallest element from the list
        mylist.insert(i, min_value)  #Insert that smallest element into the correct sorted position i
