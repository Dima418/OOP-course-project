import json

from models.Developer import Developer
from models.Manager import Manager
from models.JunoirDeveloper import JunoirDeveloper


class Deserializer():

    def deserialize(self):

        _id = 0

        # get data fron json file
        data = None
        with open('files/my_file.json','r') as file:
            data = json.load(file)

        # creates list of objects from json file
        # creates list of subordinates
        # object and subordinate connected via _id
        objects_list = list()
        objects_subs_list = list()
        for person in data:
            obj = None
            first_name = person['first_name']
            last_name = person['last_name']
            birth_date = person['birth_date']

            person_class = person['person_class']
            if person_class == 'Developer':
                obj = Developer(first_name, last_name, birth_date)
            elif person_class == 'Manager':
                obj = Manager(first_name, last_name, birth_date)
            elif person_class == 'JunoirDeveloper':
                obj = JunoirDeveloper(first_name, last_name, birth_date)

            objects_list.append({'id': _id, 'obj': obj})

            if person['subordinates']:
                objects_subs_list.append({'id': _id, 'subs': person['subordinates']})

            _id = _id + 1

        # fills in objects subordinates
        # first fin corresponding between two lists '_id'
        # then find person`s object by first name and second name
        for obj in objects_list:
            for objects_subs in objects_subs_list:
                if obj['id'] == objects_subs['id']:
                    for sub in objects_subs['subs']:
                        sub_fn = sub['first_name']
                        sub_ln = sub['last_name']
                        person = self.find_person(objects_list, sub_fn, sub_ln)

                        obj['obj'].add_subordinate(person)

        return objects_list


    def find_person(self, collection, fn, ln):
        for person in collection:
            if person['obj'].first_name == fn and person['obj'].last_name == ln:
                return person['obj']
