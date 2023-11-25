import datetime as dt

now = dt.datetime.now()  # Returns an accurate local time
print(f"Your Current Local Time is :\n{now}")
print("-" * 20)

# year
year = now.year
print(year)
print(type(year))
if year == 2020:
    print("COVID-19")
print("-" * 20)

# month
month = now.month
weekday = now.weekday()
print(weekday)  # Computers Count from 0, Week Starts from Monday
print("-" * 20)

# creating a new datetime object

birthday_date = dt.datetime(year=2002, month=10, day=18, hour=4)
print(birthday_date)
