def main():
    inp = int(input("Enter an integer: "))

    if is_prime(inp):
        print(inp, "is prime!")
    else:
        print(inp, "is not prime!")

def is_prime(n):
    if n == 0 or n == 1:
        return False

    for x in range(2, n // 2):
        if n % x == 0:
            return False

    return True

def display_100_prime():
    for x in range(1, 101):
        if is_prime(x):
            print(x)
