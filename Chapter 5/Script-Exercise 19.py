def enter_vals():
    p = float(input("Enter current amount: "))
    i = float(input("Enter interest rate: "))
    t = int(input("Enter number of months: "))
    fVal(p, i, t)

def fVal(p, i, t):
    F = p * ((1 + (i / 100)) ** t)
    print("Future val is $", F, sep="")
