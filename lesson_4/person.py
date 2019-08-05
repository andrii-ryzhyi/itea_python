from abc import ABC, abstractmethod
from datetime import date

class Person(ABC):

    _persons_list = []

    def __init__(self, surname, birth_date, faculty):
        self._surname = surname
        self._birth_date = birth_date
        self._faculty = faculty
        self._persons_list.append(self)

    @staticmethod
    def _check_year(birth_date):
        if len(birth_date.split('.')) != 3:
            raise ValueError("Birth date has a wrong format")
        return int(birth_date.split('.')[2])
        
    @staticmethod
    def count_years(birth_date):
        year = birth_date.split('.')[2]
        year_now = date.today().year
        return year_now - int(year)
        
    @classmethod
    def find_by_year(cls, min_year, max_year=None):
        if not max_year:
            max_year = min_year
        persons = []
        for person in cls._persons_list:
            if min_year <= cls._check_year(person._birth_date) <= max_year:
                persons.append(person)
        return (persons)        

    @abstractmethod
    def info(self):
        print(f"Surname: {self._surname}")
        print(f"Birth date: {self._birth_date}")
        print(f"Faculty: {self._faculty}")
    
    @abstractmethod
    def show_age(self):
        return
 
class Abiturient(Person):

    def __init__(self, surname, birth_date, faculty):
        super().__init__(surname, birth_date, faculty)

    def info(self):
        print(f"Class: {type(self).__name__}")
        super().info()

    def show_age(self):
        age = super().count_years(self._birth_date)
        print(age)


class Student(Person):

    def __init__(self, surname, birth_date, faculty, course):
        super().__init__(surname, birth_date, faculty)
        self._course = course

    def info(self):
        print(f"Class: {type(self).__name__}")
        super().info()
        print(f"Course: {self._course}")

    def show_age(self):
        age = super().count_years(self._birth_date)
        print(age)

class Teacher(Person):

    def __init__(self, surname, birth_date, faculty, position, experience):
        super().__init__(surname, birth_date, faculty)
        self._position = position
        self._experience = experience

    def info(self):
        print(f"Class: {type(self).__name__}")
        super().info()
        print(f"Position: {self._position}")
        print(f"Experience: {self._experience}")

    def show_age(self):
        age = super().count_years(self._birth_date)
        print(age)

        
a1 = Abiturient("a1", "20.04.1990", "it ops")
a2 = Abiturient("a2", "07.03.1993", "stats")
a3 = Abiturient("a3", "18.05.1990", "it ops")
s1 = Student("s1", "26.07.1989", "maths", 5)
s2 = Student("s2", "19.06.1991", "prog", 4)
t1 = Teacher("t1", "05.08.1980", "prog", "candidate", 10)

t1.show_age()
t1.info()

persons = Person.find_by_year(1990)
for person in persons:
    person.info()
