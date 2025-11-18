def iszigzag(reeks):
    n = len(reeks)

    for i in range(0, n, 2):  # alleen even indexen controleren
        if i - 1 >= 0 and reeks[i] < reeks[i - 1]:
            return False
        if i + 1 < n and reeks[i] < reeks[i + 1]:
            return False
    return True


def zigzag_traag(reeks: list[int]):
    lst = sorted(reeks)
    n = len(lst)

    for i in range(n-2,2):
        lst[i], lst[i+1] = lst[i+1], lst[i]

    return lst

def zigzag_snel(lst: list[int]):
    n = len(lst)

    for i in range(0,n,1):
        #als het huidige element op de even positie kleiner is dan het element
        # op de voorgaande oneven positie (indien die er is), wissel deze twee elementen dan om
        if i - 1 >= 0 and lst[i] < lst[i - 1]:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]

        #als het huidige element op de even positie kleiner is dan het element op de volgende
        # oneven positie (indien die er is), wissel deze twee elementen dan om
        if i + 1 < n and lst[i] < lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst



