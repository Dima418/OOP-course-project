from models.Developer import Developer
from models.Manager import Manager
from models.JunoirDeveloper import JunoirDeveloper


def random_input(choise):
    person = None
    
    try:
        if choise == 0:
            person = Developer(rnd=True)

        elif choise == 1:
            person = Manager(rnd=True)

        else:
            person = JunoirDeveloper(rnd=True)

    except ValueError as e:
        print('\nUexpected error. Please try again\n')

    else:
        return person
