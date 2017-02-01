def pow(x, y):
    if y == 0:
        return 1
    return x * pow(x, y-1)

def main():
    x = int(input('Enter x where x^y: '))
    y = int(input('Enter y where x^y: '))
    
    print(pow(x, y))
