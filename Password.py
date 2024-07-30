loop = True
while loop is True:
    name = input()
    password = input()
    age = input()
    if name == 'Theodore':
        if password == 'raspi':
            if age == '14':
                print(f'Hello {name}')
                print('Access granted.')
                loop = False
            else:
                print('Nope, try again.')
        else:
            print('Wrong password.')
    else:
        print('Nope, try again.')
print('Done')
