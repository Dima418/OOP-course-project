from abc import ABC, abstractmethod
from datetime import datetime


class Employee(ABC):

    _FNAMES = ['John', 'Guido', 'Tom', 'Martha', 'Jane', 'Kamile']
    _LNAMES = ['Doe', 'Van Rossum','Aman', 'Miller', 'Turner', 'Stein']

    # Employee supervisors property operations
    @property
    def supervisors(self):
        return self.__supervisors


    def add_supervisor(self, boss):
        if boss in self.__subordinates:
            print('Cann`t add supervisor. Person is your subordinate')
            return 0

        if boss in self.__supervisors:
            print('Cann`t add supervisor. Such supervisor already exists')
            return 0

        self.__supervisors.append(boss)

        if self not in boss.subordinates:
            boss.add_subordinate(self)
        else:
            return 0


    def remove_supervisor(self, boss):
        try:
            self.__supervisors.remove(boss)
        except ValueError as e:
            print('no such supervisor as {}'.format(boss))

    # Employee subordinates property operations
    @property
    def subordinates(self):
        return self.__subordinates


    def add_subordinate(self, pleb):
        if pleb in self.__supervisors:
            print('Cann`t add pleb. Person is your supervisor')
            return 0

        if pleb in self.__subordinates:
            print('Cann`t add subordinate. Such supervisor already exists')
            return 0

        self.__subordinates.append(pleb)

        if self not in pleb.supervisors:
            pleb.add_supervisor(self)
        else:
            return 0


    def remove_subordinate(self, pleb):
        try:
            self.__subordinates.remove(pleb)
        except ValueError as e:
            print('no such subordinate as {}'.format(pleb))


    # Employee initializator
    @abstractmethod
    def __init__(self, first_name, last_name, birth_date, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = datetime.strptime(birth_date, '%Y/%m/%d').date()
        self.date_diff = (datetime.today().date() - self.birth_date).days
        self.position = type(self).__name__.lower()
        self.responsibilities = list()

        self.__supervisors = list()
        self.__subordinates = list()


    # Employee object string represintation
    def __str__(self):
        return 'position: \t' + self.position + '\n' + \
            'first name: \t' + self.first_name + '\n' + \
            'last name: \t' + self.last_name + '\n' + \
            'birth date: \t' + self.birth_date.strftime('%Y/%m/%d')


    # Employee destructor
    def __del__(self):
        print(self.first_name, self.last_name, 'was deleted')
