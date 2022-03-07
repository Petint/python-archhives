# nyitvatartas.py pbq 10a 20211102
# Nyitvatartás: 8:00 - 18:00
#A bolt zárva van
# A bolt még myitva van x órat

timetable = {
    "open" : 8,
    "close" : 16,
}

DUtime = int(input("What time? (H): "))
if DUtime >= timetable["open"] and DUtime < timetable["close"]:
    hours = timetable["close"] - DUtime
    print(f"The store is open for {hours} more hours.")
else:
    print("The store is cloesed.")