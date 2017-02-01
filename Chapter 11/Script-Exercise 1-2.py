class Employee:
    __name = ''
    __number = 0

class ProductionWorker(Employee):
    __shift = 0
    __pay = 0

class ShiftSupervisor(Employee):
    __salary = 0
    __bonus = 0

emp = ProductionWorker()
sup = ShiftSupervisor()

emp.__name = input('Enter employee name: ')
emp.__number = int(input('Enter employee number: '))
emp.__shift = int(input('Enter employee shift: '))
emp.__pay = int(input('Enter employee pay: '))
print()

print('Name:', emp.__name)
print('Number:', emp.__number)
print('Shift:', emp.__shift)
print('Pay:', emp.__pay)
print()

sup.__name = input('Enter shift supervisor name: ')
sup.__number = int(input('Enter shift supervisor number: '))
sup.__shift = int(input('Enter shift supervisor shift: '))
sup.__salary = int(input('Enter shift supervisor salary: '))
sup.__bonus = int(input('Enter shift supervisor bonus: '))
print()

print('Name:', sup.__name)
print('Number:', sup.__number)
print('Shift:', sup.__shift)
print('Salary:', sup.__salary)
print('Bonus:', sup.__bonus)
