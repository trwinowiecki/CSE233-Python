inp = input('Enter a date (mm/dd/yyyy): ')
date = inp.split('/')

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July' \
          'August', 'September', 'October', 'November', 'December']

day = date[1]
month = months[int(date[0]) - 1]
year = date[2]

print(month, ' ', day, ', ', year, sep='')
