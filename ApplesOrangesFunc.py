def GetApples():
    print("The price of an Apple is 20 pesos.")
    ApplesFunction = int(input("How many would you like to buy? "))
    return ApplesFunction

def GetOranges():
    print("The price of an Orange is 25 pesos.")
    OrangesFunction = int(input("How many would you like to buy? "))
    return OrangesFunction

def GetAmount(AmountFunction):
    print(f"The total amount is {AmountFunction} pesos.")

Apples = GetApples()

Oranges = GetOranges()

GetAmount(Apples*20+Oranges*25)