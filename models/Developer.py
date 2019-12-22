import random
import time

from .Employee import Employee


class Developer(Employee):

    # Developer constructor
    def __init__(self, first_name=None, last_name=None, birth_date=None, rnd=False):
        if rnd:
            first_name = random.choice(self._FNAMES)
            last_name = random.choice(self._LNAMES)

            stime = time.mktime(time.strptime('1979/01/01', '%Y/%m/%d'))
            etime = time.mktime(time.strptime('1994/01/01', '%Y/%m/%d'))
            ptime = stime + random.random() * (etime - stime)

            birth_date = time.strftime('%Y/%m/%d', time.localtime(ptime))

        Employee.__init__(self, first_name, last_name, birth_date)

        self.responsibilities.append(
            (
                'code writing',
                'code review',
                'branch merge',
                'project`s technologies selecting',
                'stories and epics grooming',
                'tasks time estimating',
            )
        )
