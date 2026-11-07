def calculate_change(paid,price):
    change=paid-price
    return change

print("Welcome to the snack vending machine")
snack_price=25
while True:
    total_inserted=0
    total_coins=0
    print("The total price of a snack is $25")
    coins=int(input("Please insert a 5, 10, 25,$ coin"))

    if coins!=5 and coins!=10 and coins!=25:
        print("INVALID AMOUNT")
        continue

    total_inserted+=total_inserted
    total_coins+=coins
    break
change_due=calculate_change(total_inserted,total_coins)

print("Vending loading...")

if change_due==0:
    pass
else:
    print("change due: ",change_due)

print("RECIPT")
print("=====================")
print("Total coins inserted: ",total_inserted)
print("Paid: ",coins)