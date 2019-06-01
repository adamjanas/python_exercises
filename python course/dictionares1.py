contacts = {}
contacts["Adam"] = 123123123
contacts["Frank"] = 345345345
contacts["Ola"] = 567567567

print(contacts)

for name, number in contacts.items():
    print ("%s ma numer telefonu %d" % (name, contacts[name]))

del contacts["Adam"]

print(contacts)
contacts.pop("Ola")