import json

from utils.make_choise import make_choise
from utils.input_person import input_person
from utils.view_age import view_age
from utils.add_subordinate import add_subordinate
from utils.view_subordinates import view_subordinates

from models.Group import Group
from models.Serializer import Serializer


def main():
    group = Group()

    while True:
        print(
            '\n\nselect action:\n' + \
            '[0] - insert person\n' + \
            '[1] - view group collection\n' + \
            '[2] - view min & max age of person from category\n' + \
            '[3] - add subordinate to the person\n' + \
            '[4] - view subordinates of the person\n' + \
            '[5] - save current group collection to the file\n' + \
            '[6] - exit\n'
        )
        choise = make_choise(7)
        
        if choise == 0:
            input_person(group)

        elif choise == 1:
            group.get_all()

        elif choise == 2:
            view_age(group)

        elif choise == 3:
            add_subordinate(group)

        elif choise == 4:
            view_subordinates(group)

        elif choise == 5:
            serializer = Serializer()
            serializer.serialize(group.collection)
            print('collection saved successfully\n')

        else:
            break


if __name__ == "__main__":
    main()
