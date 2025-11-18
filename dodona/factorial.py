def factorial(n):
    # Controle: als n te groot is, niet berekenen
    if n > 13:
        return "invoer te groot"
    # Basisgeval
    if n == 0:
        return 1
    # Recursieve stap
    return n * factorial(n - 1)

# Hoofdprogramma
t = int(input())  # aantal testgevallen
for _ in range(t):
    n = int(input())
    print(factorial(n))