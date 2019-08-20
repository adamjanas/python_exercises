class Person:
    #initalization of an instance
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    #methods
    def introduce_yourself(self):
        print(f"Hello I am {self.name}, {self.surname} and I have {self.age} yo")

    def birthday(self):
        xd = self.age
        print(f"{xd} is the year of my birthday")


def main():
    #two objects of Person
    adam = Person("Adam", "hehehe", "21")
    janusz = Person("Janusz", "hyhyhyhy", "55")

    #calling the methods of introduce_yourself
    adam.introduce_yourself()
    janusz.introduce_yourself()

    adam.birthday()
    janusz.birthday()


    #modification of fields
    adam.surname = "hehehehe"
    janusz.surname = "hehehehe"


    adam.introduce_yourself()
    janusz.introduce_yourself()


main()


