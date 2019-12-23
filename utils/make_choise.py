def make_choise(size):
    while True:
        try:
            choise = int(input('your choise: '))
        
            if choise not in range(size):
                raise ValueError

        except ValueError as e:
            print('\nIncorrect input. Please try again\n')

        else:
            return choise
