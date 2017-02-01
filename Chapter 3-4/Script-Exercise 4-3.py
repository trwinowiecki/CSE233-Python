budget = float(input("Your budget for the month: "))
inp = float(input("Enter your expenses (or -1 to stop): "))
expenses = 0

while inp != -1:
    expenses += inp
    inp = float(input("Enter your expenses (or -1 to stop): "))

left = budget - expenses

if left < 0:
    print("You are over budget by", -1 * left)
elif left > 0:
    print("You are under budget by", left)
else:
    print("You are exactly at budget")
