def main():
    name = input("Enter then name of a file:")
    f = open(name, 'r')
    read(f)
    f.close()

def read(file):
    cnt = 1
    
    for line in file:
        print(cnt, ":\t", line, sep="", end = "")
        cnt += 1
