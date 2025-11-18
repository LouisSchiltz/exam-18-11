def combisom(getallen, doel):
    gezien = set()
    for a in getallen:
        if doel - a in gezien:
            return True
        gezien.add(a)
    return False
