import json


class Serializer():

    def serialize(self, collection):
        list_for_json = list()

        for person in collection:
            obj = {
                'first_name': person['obj'].first_name,
                'last_name': person['obj'].last_name,
                'birth_date': str(person['obj'].birth_date),
                'person_class': type(person['obj']).__name__,
                'subordinates': self.find_subordinates(person['obj'])
            }
            list_for_json.append(obj)

        with open('files/my_file.json','w') as file:
            json.dump(list_for_json, file, sort_keys=True, indent=4)


    def find_subordinates(self, person_obj):
        return_subs = list()
        subs_collection = person_obj.subordinates

        if subs_collection:
            for sub in subs_collection:
                item = {
                    'first_name': sub.first_name,
                    'last_name': sub.last_name
                }
                return_subs.append(item)

        return return_subs
