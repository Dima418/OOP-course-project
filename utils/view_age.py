from .make_choise import make_choise


def view_age(group):
    print(
        '\nselect class:\n' + \
        '[0] - Developer\n' + \
        '[1] - Manager\n' + \
        '[2] - Junior Developer\n'
    )
    class_choise = make_choise(3)

    if class_choise == 0:
        group.print_ages_of_category('Developer')

    elif class_choise == 1:
        group.print_ages_of_category('Manager')

    else:
        group.print_ages_of_category('JunoirDeveloper')
