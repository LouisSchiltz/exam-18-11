def leesgetal():
    while True:
        try:
            waarde = int(input("geef een getal in"))
            return waarde
        except ValueError:
            print("ongeldige waarde")

leesgetal()


def safedivide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "delen door nul mag niet"
    except (TypeError,ValueError):
        return "geef een getal door"

def leesbestand(pad):
    try:
        bestand = open("pad","r")
        return bestand
    except FileNotFoundError:
        return "bestand niet gevonden"
    except PermissionError:
        return "geen toestemming"
    except Exception as e:
        return "onverwachte fout"


def veiligefaculteit(n):
    try:
        # Typefout?
        if not isinstance(n, int):
            raise TypeError

        # Negatief?
        if n < 0:
            raise ValueError

        # Te groot?
        if n > 13:
            return "input too big"

        # Basisgeval
        if n == 0:
            return 1

        # Recursie
        return n * veiligefaculteit(n - 1)

    except TypeError:
        return "geef een getal in"
    except ValueError:
        return "geef een positief getal in"


def som(lst):
    if len(lst) == 0:
        return 0
    return lst[0]+ lst[1:]





