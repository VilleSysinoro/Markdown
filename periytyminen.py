# PERIYTYMINEN INHERITANCE
# ========================

# KIRJASTOT JA MODUULIT
# ---------------------
#import oliot # Tuodaan koko oliot.py moduulin sisätlö
import datetime
from  oliot import Student # TUodaan oliot moduulista Student luokka

# YLILUOKKA ELI ÄITILUOKKA (SUPER / PARENT CLASS)
# -----------------------------------------------

class Person():
    """Common class for all person in Raseko"""

    def __init__(self, givenName: str, surName: str):
        """Creates a Person object

        Args:
            givenName (str): A first name
            surName (str): A last name
        """
        self.givenName = givenName
        self.surName = surName

    def calculateAge3(self, isoBirthday: str) -> float:
        birthday = datetime.datetime.fromisoformat(isoBirthday)
        age = datetime.datetime.now() - birthday
        ageInYears = age.days / 365
        return ageInYears

    # Saattinen metodi, joka laskee iän, Staattisessa metodissa ei luoda oliota lainkaan
    # Vaan metodia voi käyttää suoraan luokasta käsin
    @staticmethod
    def calculateAge(birthDay) -> float:
        """Calculates student's current age in full years

        Returns:
            float: age in years
        """
        birthDay = datetime.datetime.fromisoformat(birthDay)
        age = datetime.datetime.now() - birthDay
        ageInYears = age.days / 365
        return round(ageInYears)
    # Luokka metodi on myös staattinen, eli ei vaadi oolion muodostamista
    # Huomaa luokkaan viittaava cls, joka korvaa perinteisen self:n
    @classmethod
    def calculateAge2(cls, birthDay):
        """Calculates student's current age in full years

        Returns:
            float: age in years
        """
        birthDay = datetime.datetime.fromisoformat(birthDay)
        age = datetime.datetime.now() - birthDay
        ageInYears = age.days / 365
        return round(ageInYears)

# ALILUOKKA ELI LAPSILUOKKA (SUB / CHILD CLASS)
# ---------------------------------------------

class RasekoStudent(Person):
    """The student class, inherits The Person class"""
    def __init__(self, givenName: str, surName: str, studentNumber: int):
        """Creates a student object

        Args:
            givenName (str): Student's first name
            sureName (str): Student's last name
            studentNumber (int): Student's ID
        """
        super().__init__(givenName, surName) # Määritellään tapahtuvaksi yliluokan mukaan
        self.studentNumber = studentNumber # Ei määritelty yliluokassa 

class RasekoTeacher(Person):
    """Creates a teacher inheriting the Person class

    Args:
        Person (class): Name if the super class
    """
    def __init__(self, givenName: str, surName: str, groups: list[str]):
        """Constructor for teacher objects

        Args:
            givenName (str): Teachers first name
            surName (str): Teachers last name
            groups (list[str]): List of student groups
        """
        super().__init__(givenName, surName)
        self.groups = groups

if __name__ == "__main__":
    rasekoStudent = RasekoStudent('Jonne', 'Janttari', '12345')
    print(f'opiskeijan sukunimi on {rasekoStudent.givenName}')

    groups = ['TiVi23A', 'TiVi23B', 'TiVi20oa']
    rasekoTeacher = RasekoTeacher('Markku', 'Kynsijärvi', groups)
    # Tulostaa listan
    #print(rasekoTeacher .__dict__)
    
    print(f'{rasekoTeacher.givenName} opettaa ryhmiä {rasekoTeacher.groups}')

    # Luodaan moduulosta oliot.py Student-olio
    student = Student('Tuittu Kiukkunen', 'Auto22B', '2007-10-23')
    print(f'{student.name} on {student.calculateAge()}')

    ika = Person.calculateAge('2008-03-22')
    print(ika)

    ika2 = Person.calculateAge2('1978-12-10')
    print(ika2)

    person1 = Person('Calle', 'Keckelberg')
    ika3 = person1.calculateAge3('2009-10-22')
    print(f'Henkilön {person1.givenName} ikä on {ika3} vuotta')