a = int(input("enter your percent of exam to get grade:"))
if a >= 90:
    print("A")
elif 90 > a >= 75:
    print("B")
elif 75 > a >= 50:
    print("C")
elif 50 > a >30:
    print("D")
else:
    print("E")
# add
import datetime

teraz = datetime.datetime.now()
print(str(teraz.hour)+":"+str(teraz.minute))


print(teraz.strftime("%H:%M   %d.%m.%Y"))     # alternatywa     print(teraz.strftime("%H:%M  %d %b %Y) Nazwa miesiaca

