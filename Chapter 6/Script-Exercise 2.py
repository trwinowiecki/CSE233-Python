def main():
    name = input("Enter then name of a file:")
    f = open(name, 'r')
    read(f)
    f.close()

def read(file):
    cnt = 1
    
    for line in file:
        if cnt <= 5:
            print(line, end = "")
        else:
            break

        cnt += 1
