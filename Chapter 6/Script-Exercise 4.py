def main():
    name = input("Enter then name of a file:")
    f = open(name, 'r')
    read(f)
    f.close()

def read(file):
    cnt = 0
    
    for line in file:
        cnt += 1

    print("# of items:", cnt)
