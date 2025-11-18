def samenvoegen1(a, b):
    resultaat1 = []
    for x, y in zip(a, b):
        resultaat1.extend([x, y])
    return resultaat1

#zonder zip functie

def samenvoegen(a, b):

    resultaat = []
    n = min(len(a), len(b))
    for i in range(n):
        resultaat.append(a[i])
        resultaat.append(b[i])
    return resultaat


def weven(a, b):

    la, lb = len(a), len(b)
    if la == 0 or lb == 0:
        return []

    n = max(la, lb)
    resultaat = []
    for i in range(n):
        resultaat.append(a[i % la])
        resultaat.append(b[i % lb])
    return resultaat




def ritsen(a, b):
    resultaat = []
    n = min(len(a), len(b))

    # beurtelings toevoegen
    for i in range(n):
        resultaat.append(a[i])
        resultaat.append(b[i])

    # rest toevoegen
    if len(a) > n:
        resultaat.extend(a[n:])
    elif len(b) > n:
        resultaat.extend(b[n:])
    return resultaat
