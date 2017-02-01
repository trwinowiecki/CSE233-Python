f = open('USPopulation.txt', 'r')
data = f.read().splitlines()
f.close()

lar = 0
larI = 0
small = -1
smallI = 0
total = 0
curr = 0

for i in range(0, len(data) - 2):
    curr = int(data[i+1]) - int(data[i])

    if curr < small or small == -1:
        small = curr
        smallI = i

    if curr > lar:
        lar = curr
        larI = i

    total += curr

print("Average change:", total / len(data))
print("Largest change:", 1950 + larI)
print("Smallest change:", 1950 + smallI)
