from collections.abc import Iterable
from datetime import date, datetime, timezone
from itertools import permutations

import pytest
from group import Group, Person, Student


@pytest.fixture
def polina() -> Person:
    return Person("Polina", "Gagarina", "female", date(1990, 4, 12))


@pytest.fixture
def galina():
    return Student("Galina", "Moskovskaya", "female", date(1992, 4, 12), 161, 5)


@pytest.fixture
def group() -> Group:
    return Group(
        [
            Student("Ivan", "Petrov", "male", date(1997, 1, 1), 1, 1),
            Student("Petya", "Sidorov", "female", date(1993, 1, 1), 1, 1),
            Student("Serge", "Ivanov", "male", date(1994, 1, 1), 1, 1),
        ]
    )


class TestPerson:
    @staticmethod
    def test_init(polina: Person):
        assert hasattr(polina, "name")
        assert hasattr(polina, "surname")
        assert hasattr(polina, "sex")
        assert hasattr(polina, "bday")

    @staticmethod
    def test_error_init():
        with pytest.raises(ValueError):
            Person("a", "b", "c", "1990/4/12")

        with pytest.raises(ValueError):
            Person("a", "b", "c", 1990)

        with pytest.raises(ValueError):
            Person("a", "b", "c", [])

    def test_ages(self, polina: Person):
        assert hasattr(polina, "full_ages")
        assert polina.full_ages() == datetime.now(tz=timezone.utc).year - polina.bday.year

        for i in range(10):
            polina.bday = date(1990 + i, 4, 12)
            assert polina.full_ages() == datetime.now(tz=timezone.utc).year - polina.bday.year

    @staticmethod
    def test_eq(polina: Person):
        assert polina == Person("Polina", "Gagarina", "female", date(1990, 4, 12))

    @staticmethod
    @pytest.mark.parametrize(
        "not_polina",
        [
            Person("Polina", "Gagarina", "female", date(1992, 4, 12)),
            Person("Polina", "Gagarina", "male", date(1990, 4, 12)),
            Person("Polina", "Mareeva", "female", date(1990, 4, 12)),
            Person("Nadya", "Gagarina", "female", date(1990, 4, 12)),
            Person("Katya", "Gagarina", "female", date(1990, 4, 12)),
            Person("Mark", "Sobolev", "male", date(1999, 4, 12)),
        ],
    )
    def test_not_eq(polina: Person, not_polina: Person):
        assert polina != not_polina

    @staticmethod
    def test_repr(polina: Person):
        import datetime  # noqa: F401

        assert eval(repr(polina))  # noqa: S307


class TestStudent:
    @staticmethod
    def test_inheritance():
        assert issubclass(Student, Person)
        assert "full_ages()" not in Student.__dict__

    @staticmethod
    def test_init(galina: Student):
        assert hasattr(galina, "group")
        assert hasattr(galina, "skill")

    @staticmethod
    def test_error_init():
        with pytest.raises(ValueError):
            Student("a", "b", "c", "1990/4/12", 1, 1)

        with pytest.raises(ValueError):
            Student("a", "b", "c", 1990, 1, 1)

        with pytest.raises(ValueError):
            Student("a", "b", "c", [], 1, 1)

    def test_repr(self, galina: Student):
        import datetime  # noqa: F401

        assert eval(repr(galina))  # noqa: S307

    def test_eq(self, galina: Student):
        assert galina == Student("Galina", "Moskovskaya", "female", date(1992, 4, 12), 161, 5)

    @staticmethod
    @pytest.mark.parametrize(
        "not_galina",
        [
            Student("Galina", "Moskovskaya", "female", date(1992, 4, 12), 161, 6),
            Student("Galina", "A", "female", date(1992, 4, 12), 161, 5),
            Student("Galina", "Moskovskaya", "female", date(1992, 4, 11), 11, 6),
            Student("Galina", "Moskovskaya", "female", date(1992, 2, 12), 161, 6),
            Student("Galina", "Moskovskaya", "female", date(1992, 4, 12), 162, 6),
            Student("Galina", "Moskoviskaya", "female", date(1992, 4, 12), 161, 6),
        ],
    )
    def test_not_eq(galina: Student, not_galina:
