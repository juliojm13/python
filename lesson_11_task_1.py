import re


class Date:
    def __init__(self, date):
        self.day = None
        self.year = None
        self.month = None
        self.date = date
        self.pattern = re.compile(r"(?P<day>\d{2})-(?P<month>\d{2})-(?P<year>\d{2})")
        result_ = self.pattern.match(date)
        if not result_:
            raise ValueError(f"Error!! {date} is not valid.You must write the date in this order ' dd-mm-yy '")

    def __str__(self):
        return f'{self.date}'

    @classmethod
    def get_numbers(cls, self):
        result = self.pattern.finditer(self.date)
        for i in result:
            self.day = int(i.groupdict()['day'])
            self.month = int(i.groupdict()['month'])
            self.year = int(i.groupdict()['year']) + 2000
            print(f'day = {self.day} , month = {self.month} , year = {self.year} ')

    @staticmethod
    def check(self, max_):
        year_max = max_
        if self.month > 12 or self.month < 1:
            raise ValueError(f'the month {self.month} is not correct! It must be from 1 to 12!')
        if self.year > year_max:
            raise ValueError(f'the year {self.year} is not correct! It must be less then  {year_max}!')
        return print('Everything ok')


date_1 = Date('01-12-20')
Date.get_numbers(date_1)
Date.check(date_1, 2021)
date_2 = Date('28-12-22')
Date.get_numbers(date_2)
Date.check(date_1, 2022)
print(date_1.day + date_2.day)
date_3 = Date('26-01-06')
Date.get_numbers(date_3)
Date.check(date_3, 2021)
