print("Im your Apple and Change counter!")

def GetAmount():
    AmountFunction = int(input("How much is your money? "))
    return AmountFunction

def GetPrice():
    PriceFunction = int(input("What is the price of an Apple? "))
    return PriceFunction

def GetOutput(QuantityFunction, ChangeFunction):
    print(f"You can buy {QuantityFunction} apples and your change is {ChangeFunction} pesos.")

Amount = GetAmount()

Price = GetPrice()

GetOutput(Amount//Price, Amount-Amount//Price*Price)