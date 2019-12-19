from .Employee import Employee


class Manager(Employee):

    # Manager constructor
    def __init__(self, first_name, last_name, birth_date):

        Employee.__init__(self, first_name, last_name, birth_date)
        self.responsibilities.append('management')
