class Human:
    name = ""
    surname = ""

    def __init__(self):
        print("start")

    def __del__(self):
        print("end")

    def introduce(self):
        print(self.name + " " + self.surname)

    def change_name(self):
        self.name = input("Change the name\t")
        print(self.name)



friend = Human()  #object
friend.name = "xddd"
friend.surname = "hehehe"
friend.introduce()

friend1 = Human()
friend1.name
friend1.change_name()