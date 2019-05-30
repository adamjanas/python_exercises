class human:
    name = "unknown"
    __age = 00

    def __init__(self, name, age):
        self.name = name
        self._age = age
    #returns string when we print object
    def __str__(self):
        return self.name

    def set_age(self, age):
        self.__age = age

    def set_name(self, name):
        self.name = name

    def get_age(self):
        if self.__age > 18:
            print("adult")
        elif self.__age > 10:
            print("teenager")
        else:
            print("child")

man = human("john", 24)
man.get_age()
print(man)