def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m-1, 1)
    else:
        return ackermann(m-1, ackermann(m, n-1))

def main():
    m = int(input('Enter int m for Ackermann\'s function: '))
    n = int(input('Enter int n for Ackermann\'s function: '))

    print(ackermann(m, n))
