import webbrowser as wb

print('Enter (q) to open youtube')
print('or Enter (g) to open google')
print('or Enter (s) to open stackoverflow')

k = input('(g) to open google or (s) to open stackoverflow or (q) to open youtube')

if k == 'q':
    wb.register('chrome', None)
    wb.open('https://www.youtube.com')
elif k == 'g':
    wb.register('chrome', None)
    wb.open('https://www.google.com')
elif k == 's':
    wb.register('chrome', None)
    wb.open('https://stackoverflow.com')
