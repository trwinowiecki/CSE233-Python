item1 = float(input("Price of item 1: "))
item2 = float(input("Price of item 2: "))
item3 = float(input("Price of item 3: "))
item4 = float(input("Price of item 4: "))
item5 = float(input("Price of item 5: "))

subtotal = item1 + item2 + item3 + item4 + item5
tax = 0.07
total = subtotal * (1 + tax)

print("Subtotal: $", subtotal, sep="")
print("Total: $", total, sep="")
