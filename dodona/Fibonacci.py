def fib(n: int) -> int:
    """Geef het n-de Fibonaccigetal terug (met fib(0)=0, fib(1)=1)."""
    if n < 0:
        raise ValueError("n moet een niet-negatief geheel getal zijn")
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

