"""Create the list of male/female names.
User give one name. If the name is in the list, display whether it is female or male name.
If the name is not in the list, add new name to the list"""

dict_names = {
    "Anna" : "zenskie",
    "Julia" : "zenskie",
    "Zofia" : "zenskie",
    "Maja" : "zenskie",
    "Hania" : "zenskie",
    "Maria" : "zenskie",
    "Stanisława" : "zenskie",
    "Michał" : "meskie",
    "Antoni" : "meskie",
    "Jan" : "meskie",
    "Franciszek" : "meskie",
    "Piotr" : "meskie",
    "Wiktor" : "meskie",
    "Wawrzyniec" : "meskie"
    }

name = str(input("Enter the name\t"))

if (name in list(dict_names.keys())):
    print(name, "to imię", dict_names[name])
else:
    print("Nie mamy tego imienia. Dodaj je do zbioru")
    gender = str(input("To imię męskie czy żeńskie? Wpisz m/z\t\t"))
    if gender == "m":
        dict_names[name] = "meskie"
    else:
        dict_names[name] = "zenskie"
    print(list(dict_names.keys()))