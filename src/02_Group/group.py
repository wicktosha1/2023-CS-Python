from datetime import date, datetime, timezone
from typing import List


class Person:
    """
    >>> person = Person('Ivan', 'Ivanov', 'male', date(1999, 8, 12))
    >>> person
    Person('Ivan', 'Ivanov', 'male', datetime.date(1999, 8, 12))

    >>> Person('Ivan', 'Ivanov', 'male', datetime.now(tz=timezone.utc).date()).full_ages()
    0
    >>> Person('Ivan', 'Ivanov', 'man', "1989.4.26")
    Traceback (most recent call last):
        ...
    ValueError: bday must be date type
    """

    name: str
    surname: str
    sex: str
    bday: date

    def __init__(self, name: str, surname: str, sex: str, bday: date):
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"Person({self.name!r}, {self.surname!r}, {self.sex!r}, {self.bday!r})"

    def __eq__(self, other: "Person") -> bool:
        raise NotImplementedError

    def full_ages(self):
        raise NotImplementedError


class Student(Person):
    """
    >>> student = Student('Ivan', 'Ivanov', 'male', date(1999, 8, 12), 161, 9)
    >>> student
    Student('Ivan', 'Ivanov', 'male', datetime.date(1999, 8, 12), 161, 9)
    """

    name: str
    surname: str
    sex: str
    bday: date
    group: int
    skill: int

    def __init__(self, name: str, surname: str, sex: str, bday: date, group: int, skill: int):
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError

    def __eq__(self, other: "Student") -> bool:
        raise NotImplementedError


class Group:
    """
    Encapsulates list of students
    """

    group: List[Student]

    def __init__(self, group: List[Student]):
        self.group = list(group)

    def __eq__(self, other: "Group") -> bool:
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"Group([{', '.join([repr(group) for group in self.group])}])"

    def sort_by_age(self, *, reverse: bool = False):
        self.group = sorted(
            self.group,
            key=lambda student: student.full_ages(),
            reverse=reverse,
        )

    def sort_by_skill(self, *, reverse=False):
        raise NotImplementedError

    def sort_by_age_and_skill(self, *, reverse=False):
        raise NotImplementedError
