year = int(input("Укажите год"))

if year % 4 != 0:
    print("Не високосный год")
elif year % 100 != 0:
    print("Високосный год")
elif year % 400 == 0:
    print("Високосный год")
else:
    print("Не високосный год")