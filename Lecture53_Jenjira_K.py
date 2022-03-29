def vatCal(price):
    total = price+(price*7/100)
    return total

price = int(input("How much: "))
print(vatCal(price))
