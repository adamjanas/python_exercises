import datetime

teraz = datetime.datetime.now()
print(str(teraz.hour)+":"+str(teraz.minute))
print(teraz.strftime("%H:%M   %d.%m.%Y"))     # alternative     print(teraz.strftime("%H:%M  %d %b %Y) Nazwa miesiaca