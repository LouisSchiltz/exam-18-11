def nPrintln(message, times):
    if times >= 1:
        print(message)
        return nPrintln(message, times - 1)
    else: print(message)
nPrintln('hey',3)

