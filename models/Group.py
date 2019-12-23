
def print_subordinates(obj):
    subordinates = obj.subordinates
    if subordinates:
        print('\nsubordinates of {} {}:'.format(obj.first_name, obj.last_name))
        for sub in subordinates:
            print('- ' + sub.first_name + ' ' + sub.last_name)
            print_subordinates(sub)

    else:
        print('\n{} {} has no subordinates \n'.format(obj.first_name, obj.last_name))
        print('_________________________')
        return 0


class Group():

    collection = list()
    _id = 0


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Group, cls).__new__(cls)
        return cls.instance


    def add_person(self, person):
        obj = {'id': self._id, 'obj': person}
        self.collection.append(obj)
        self._id = self._id + 1


    def remove_person(self, person_id):
        for person in self.collection:
            if person['id'] == person_id:
                self.collection.remove(person)

    def clear(self):
        self.collection.clear()
        self._id = 0


    def get_all(self):
        print('-------------------------')
        if self.collection is not None:
            for person in self.collection:
                print('id: \t[{}]'.format(person['id']))
                print(person['obj'])
                print()
        else:
            print('Group is empty\n')


    def print_person_subordinates(self, person_id):
        for person in self.collection:
            if person['id'] == int(person_id):
                print('-------------------------')
                print(person['obj'])
                print('_________________________')
                print_subordinates(person['obj'])
                print('-------------------------\n')


    def print_ages_of_category(self, category):
        categorized_persons = list()

        for person in self.collection:
            if type(person['obj']).__name__ == category:
                categorized_persons.append(person['obj'])

        if categorized_persons:
            max_age_person = categorized_persons[0]
            min_age_person = categorized_persons[0]

            for person in categorized_persons:
                if person.date_diff > max_age_person.date_diff:
                    max_age_person = person
                elif person.date_diff < min_age_person.date_diff:
                    min_age_person = person
            print('mAx age: ')
            print(max_age_person)
            print('\nmIn age: ')
            print(min_age_person)
            print('\n')
        else:
            print('\n No person found in such category')