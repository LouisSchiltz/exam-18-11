def woorden_splitsen(tekst):
    tekst = open(tekst, 'r')
    tekst = tekst.read()
    tekst = replacepunctuation(tekst)
    return tekst.split()

def replacepunctuation(tekst):
    for ch in tekst:
        if ch in '~@#$%^&*()_-+=~"<>?/,.;!{}[]|':
            tekst = tekst.replace(ch,'')
    return tekst

def woorden_tellen(tekst):
    tekst = woorden_splitsen(tekst)
    woorden = {}
    for line in tekst:
        line = line.lower()
        if line not in woorden:
            woorden[line] = 1
        else:
            woorden[line] += 1
    return woorden