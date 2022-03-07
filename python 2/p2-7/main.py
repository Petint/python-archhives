import pendulum as pdm
import datetime as dt


def idozona():
    cities = ["Europe/Budapest",
              "Australia/Sydney",
              "Europe/Moscow",
              "America/Toronto",
              "Europe/Vienna"
              ]
    times = []
    for city in cities:
        now = pdm.now(city)
        now = now.to_datetime_string()
        times.append(now)
    for item in range(len(cities)):
        print(f"It's {times[item]} in {cities[item]}.")



# idozona()


print(dt.datetime.now())
print(dt.datetime.today())
print(dt.datetime.today().strftime("%A")) # day
print(dt.datetime.today().strftime("%W")) # num. of week
print(dt.datetime.today().strftime("%w")) # num. of day in week
print(dt.datetime.today().strftime("%j")) # day of year

today = dt.date.today()
yeasterday = today - dt.timedelta(days=1)
print(type(today))

