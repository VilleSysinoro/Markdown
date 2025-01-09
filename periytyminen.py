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

    def __init__(self, etunimi: str, sukunimi: str):
        """Creates a Person object

        Args:
            etunimi (str): A first name
            sukunimi (str): A last name
        """
        self.etunimi = etunimi
        self.sukunimi = sukunimi

    # Saattinen metodi, joka laskee iän, Staattisessa metodissa ei luoda oliota lainkaan
    # Vaa

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
    def __init__(self, etunimi: str, sukunimi: str, opiskelijanumero: str):
        """Creates a student object

        Args:
            etunimi (str): opiskelijan etunimi
            sukunimi (str): opiskelijan sukunimi
            opiskelijanumero (str): opiskelijanumero
        """
        super().__init__(etunimi, sukunimi) # Määritellään tapahtuvaksi yliluokan mukaan
        self.opiskelijanumero = opiskelijanumero # Ei määritelty yliluokassa 

class RasekoTeacher(Person):
    """Creates a teacher inheriting the Person class

    Args:
        Person (class): Name if the super class
    """
    def __init__(self, etunimi: str, sukunimi: str, luokat: list[str]):
        """Constructor for teacher objects

        Args:
            etunimi (str): Teachers first name
            sukunimi (str): Teachers last name
            luokat (list[str]): List of student groups
        """
        super().__init__(etunimi, sukunimi)
        self.luokat = luokat

if __name__ == "__main__":
    rasekoStudent = RasekoStudent('Jonne', 'Janttari', '12345')
    print(f'opiskeijan sukunimi on {rasekoStudent.sukunimi}')

    luokat = ['TiVi23A', 'TiVi23B', 'TiVi20oa']
    rasekoTeacher = RasekoTeacher('Markku', 'Kynsijärvi', luokat)
    # Tulostaa listan
    #print(rasekoTeacher .__dict__)
    
    print(f'{rasekoTeacher.etunimi} opettaa ryhmiä {rasekoTeacher.luokat}')

    # Luodaan moduulosta oliot.py Student-olio
    student = Student('Tuittu Kiukkunen', 'Auto22B', '2007-10-23')
    print(f'{student.name} on {student.calculateAge()}')

    ika = Person.calculateAge('2008-03-22')
    print(ika)

    ika2 = Person.calculateAge2('1978-12-10')
    print(ika2)