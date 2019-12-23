def add_subordinate(group):
    to_person_id = input('\ninput person id: ')
    sub_person_id = input('\ninput person id to subordinate: ')
    for person_to in group.collection:
        if person_to['id'] == int(to_person_id):
            to = person_to['obj']
            for person_sub in group.collection:
                if person_sub['id'] == int(sub_person_id):
                    to.add_subordinate(person_sub['obj'])
