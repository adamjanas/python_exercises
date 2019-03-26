class TooColdException(Exception):
    def __init__(self, temp):
        print('temperature {} is too low'.format(temp))


def celcius_to_kelvin(temp):
    if temp < -273.15:
        raise TooColdException(temp)
    return temp + 273.15


print(celcius_to_kelvin(10))
