string = input("Enter string: ")
symbol = input("Enter symbol: ")
print(string.rsplit(symbol, 1)[0].replace(symbol, symbol.upper()) + symbol.upper())
