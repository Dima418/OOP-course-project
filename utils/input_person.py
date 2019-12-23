from .make_choise import make_choise
from .manual_input import manual_input
from .random_input import random_input

from models.Deserializer import Deserializer


def input_person(group):
    print(
            '\n\nselect input type:\n' + \
            '[0] - manually\n' + \
            '[1] - random\n' + \
            '[2] - from file\n'
    )
    input_choise = make_choise(3)

    # manually
    if input_choise == 0:
        print(
            '\nselect class:\n' + \
            '[0] - Developer\n' + \
            '[1] - Manager\n' + \
            '[2] - Junior Developer\n'
        )
        class_choise = make_choise(3)
        person = manual_input(class_choise)
        group.add_person(person)

    # random
    elif input_choise == 1:
        print(
            '\nselect class:\n' + \
            '[0] - Developer\n' + \
            '[1] - Manager\n' + \
            '[2] - Junior Developer\n'
        )
        class_choise = make_choise(3)
        person = random_input(class_choise)
        group.add_person(person)

    # from file
    else:
        des = Deserializer()
        group.collection = des.deserialize()
