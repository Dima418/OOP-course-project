from datetime import date, datetime

from models.Developer import Developer
from models.Manager import Manager
from models.JunoirDeveloper import JunoirDeveloper


def manual_input(choise):
    first_name = input('\ninput first name: ')
    last_name = input('input last name: ')
    while True:
        print('\n! birth date info !\n')
        print('format: yyyy-MM-dd')
        print('date limitations:')
        print('\t- Developers (1979-01-01 : 1994-01-01)')
        print('\t- Managers (1974-01-01 : 1989-01-01)')
        print('\t- Junoir Developers (1989-01-01 : 1999-01-01)')
        print()

        birth_date = input('input birth date: ')
        
        person = None
        
        try:
            if choise == 0:
                date_start = date(1979, 1, 1)
                date_end = date(1994, 1, 1)
                if date_start < datetime.strptime(birth_date, '%Y-%m-%d').date() < date_end:
                    person = Developer(first_name, last_name, birth_date)
                else:
                    raise ValueError

            elif choise == 1:
                date_start = date(1974, 1, 1)
                date_end = date(1989, 1, 1)
                if date_start < datetime.strptime(birth_date, '%Y-%m-%d').date() < date_end:
                    person = Manager(first_name, last_name, birth_date)
                else:
                    raise ValueError

            else:
                date_start = date(1989, 1, 1)
                date_end = date(1999, 1, 1)
                if date_start < datetime.strptime(birth_date, '%Y-%m-%d').date() < date_end:
                    person = JunoirDeveloper(first_name, last_name, birth_date)
                else:
                    raise ValueError

        except ValueError as e:
            print('\nIncorrect input. Please try again\n')

        else:
            return person
