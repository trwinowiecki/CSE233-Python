def main():
    name = input("Enter file name: ")
    f = open(name, 'r')
    sum = 0
    
    for line in f:
        sum += int(line)

    print(sum)
    f.close()
