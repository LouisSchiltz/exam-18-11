def dubbel(getallen):
    gezien = set()
    for x in getallen:
        if x in gezien:
            return x
        gezien.add(x)
    return None


def dubbels(getallen):
    telling = {}
    for x in getallen:
        telling[x] = telling.get(x, 0) + 1

    enkel = set()
    meer = set()
    for x, k in telling.items():
        if k == 1:
            enkel.add(x)
        else:
            meer.add(x)
    return enkel, meer