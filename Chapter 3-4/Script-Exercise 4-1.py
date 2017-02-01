sum = 0
day = 1
bugs = 0

while day <= 5:
    string = "Number of bugs collected on day " + str(day) + ": "
    bugs = int(input(string))
    sum += bugs
    day += 1

print("Total bugs =", sum)
