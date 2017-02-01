def boy():
        name = input("Enter a boy's name:")
        f = open('BoyNames.txt', 'r')
        names = f.read().splitlines()
        
        if name in names:
                print(name, "was a popular boy's name between 2000 and 2009.")
        else:
                print(name, "was not a popular boy's name between 2000 and 2009.")

def girl():
        name = input("Enter a girl's name:")
        f = open('GirlNames.txt', 'r')
        names = f.read().splitlines()
        
        if name in names:
                print(name, "was a popular girl's name between 2000 and 2009.")
        else:
                print(name, "was not a popular girl's name between 2000 and 2009.")

type = input("Enter 'boy', 'girl', or 'both':")

if type == 'boy':
        boy()
elif type == 'girl':
        girl()
elif type == 'both':
        boy()
        girl()
