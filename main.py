from models.Developer import Developer
from models.Manager import Manager
from models.Group import Group


def main():
    dev = Developer('dev_fn_1', 'dev_ln_1', '1990/12/01')
    dev2 = Developer('dev_fn_2', 'dev_ln_2', '1999/10/01')
    dev3 = Developer(rnd=True)
    dev4 = Developer(rnd=True)
    dev5 = Developer(rnd=True)
    
    man1 = Manager(rnd=True)

    g = Group()
    g.add_person_to_collection(dev)
    g.add_person_to_collection(dev2)
    g.add_person_to_collection(dev3)
    g.add_person_to_collection(dev4)
    g.add_person_to_collection(dev5)
    g.add_person_to_collection(man1)
    
    g.get_all_collection_items()

    g.print_category_ages('Developer')


if __name__ == "__main__":
    main()
