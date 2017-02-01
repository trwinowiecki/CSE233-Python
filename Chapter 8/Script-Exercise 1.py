name = input('Enter your full name: ')
names = name.split(' ')
initials = ''

for x in names:
    initials += ' ' + x[:1] + '.'

initials = initials.lstrip(' ')

print(initials)
