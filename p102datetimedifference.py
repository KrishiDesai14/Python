import datetime

today = datetime.date.today()

birthDate = datetime.date(2023, 10, 11)

age = today.year - birthDate.year

print(age)
