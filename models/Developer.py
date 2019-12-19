from .Employee import Employee


class Developer(Employee):

    # Developer constructor
    def __init__(self, first_name, last_name, birth_date):

        Employee.__init__(self, first_name, last_name, birth_date)
        self.responsibilities.append('develop')
