name = input('What is your name: ')
print ('Hello, ' + name + '.')

name_length = len(name)
print(name + ' has ' + str(name_length) + ' letters. ')

birth_month = input('What is your birth month: ')
if birth_month.upper() == 'JULY':
    print(f'Happy Birthday, {name}!')