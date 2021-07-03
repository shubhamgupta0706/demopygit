choice = ''
started = False
while choice.upper() != 'QUIT':
    choice = input('>')
    if choice.upper() == 'HELP':
        print('''
start - to start the car
stop - to stop the car
quit - to exit
        ''')
    elif choice.upper() == 'START':
        if started:
            print('Car already started.')
        else:
            started = True
            print('Car started...Ready to go!')
    elif choice.upper() == 'STOP':
        if not started:
            print('Car already stopped.')
        else:
            started = False
            print('Car stopped!')
    elif choice.upper() == 'QUIT':
        print('Quitting...')
        break
    else:
        print("Sorry! I don't understand that")

print('Exit Successful!')