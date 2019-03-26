try:

    plik = open("test.txt","w")
    plik.write("hello world")
    plik.read("y")

except FileNotFoundError as e:
    print("plik nie istnieje")
    print(e)
except TypeError as e:
    print("zly typ")
    print(e)
except Exception as e:  # e  tlumaczenie bledu
    print("nieznany błąd")
    print(e)
