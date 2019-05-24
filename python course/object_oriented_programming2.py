class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def introduce_yourself(self):
        print(f"Hello I am {self.name}, {self.surname} and I have {self.age} yo")

    def birthday(self):
        xd = self.age
        print(f"{xd} is the year of my birthday")


def main():
    # two objects of Person
    Adam = Person("Adam", "hehehe", "21")
    Janusz = Person("Janusz", "hyhyhyhy", "55")

    #calling the methods of introduce_yourself
    Adam.introduce_yourself()
    Janusz.introduce_yourself()

    Adam.birthday()
    Janusz.birthday()


    #modification of fields
    Adam.surname = "hehehehe"
    Janusz.surname = "hehehehe"


    Adam.introduce_yourself()
    Janusz.introduce_yourself()


main()





