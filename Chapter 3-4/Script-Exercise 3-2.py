l1 = int(input("Enter the length of the first rectangle: "))
w1 = int(input("Enter the width of the first rectangle: "))

l2 = int(input("Enter the length of the second rectangle: "))
w2 = int(input("Enter the width of the second rectangle: "))

a1 = l1 * w1
a2 = l2 * w2

if a1 > a2:
    print("The first rectangle is larger")
elif a1 < a2:
    print("The second rectangle is larger")
else:
    print("They are the same size")
