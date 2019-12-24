import random
import time

from .Employee import Employee


class Manager(Employee):

    birth_date_start = '1974-01-01'
    birth_date_end = '1989-01-01'


    # Manager constructor
    def __init__(self, first_name=None, last_name=None, birth_date=None, rnd=False):
        if rnd:
            first_name = random.choice(self._FNAMES)
            last_name = random.choice(self._LNAMES)

            stime = time.mktime(time.strptime(self.birth_date_start, '%Y-%m-%d'))
            etime = time.mktime(time.strptime(self.birth_date_end, '%Y-%m-%d'))
            ptime = stime + random.random() * (etime - stime)

            birth_date = time.strftime('%Y-%m-%d', time.localtime(ptime))

        Employee.__init__(self, first_name, last_name, birth_date)

        self.init_responsibilities()


    def init_responsibilities(self):
        self.responsibilities.append(
            (
                'communicating with clients',
                'development methodology selection',
                'tasks time estimating',
                'development process control',
                'communication with the development team',
            )
        )
