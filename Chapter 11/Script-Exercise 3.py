class Person:
    name = ''
    addr = ''
    phone = ''

class Customer(Person):
    number = 0
    mail = False

cust = Customer()

cust.name = input('Enter customer name: ')
cust.addr = input('Enter customer address: ')
cust.phone = input('Enter customer phone number: ')
cust.number = int(input('Enter customer number: '))
if input('Would they like to join the mailing list (y or n): ') == 'y':
    cust.mail = True
else:
    cust.mail = False
print()

print("Name:", cust.name)
print("Address:", cust.addr)
print("Phone number:", cust.phone)
print("Number:", cust.number)
print("Mailing list?", cust.mail)
