numlist = [100, 101, 0, "103", 104]

try:
    i1 = int(input("Give an index: "))
    print("100 /", numlist[i1], "=", 100 / numlist[i1])
except IndexError:
    print("Fout: De opgegeven index bestaat niet in de lijst.")
except ZeroDivisionError:
    print("Fout: Delen door nul is niet mogelijk.")
except ValueError:
    print("Fout: Ongeldige invoer, geef een geheel getal in.")
except TypeError:
    print("Fout: Het gekozen element kan niet gebruikt worden voor een deling (verkeerd type).")
except Exception as e:
    print("Fout:", str(e))