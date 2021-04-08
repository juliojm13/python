duration = int(input("write the seconds, please: "))
sec = 0
min = 0
hour = 0
if duration < 60:
    print(duration, " sec")
elif duration >= 60 and duration < 3600:
    while duration >= 60:
        duration -= 60
        min += 1
    else:
        print(min, " min", duration, " sec")
elif duration >= 3600 and duration < 86400:
    hour = duration // 3600
    min = (duration % 3600) // 60
    sec = (duration % 3600) % 60
    print(hour, " hours", min, "min", sec, "sec")
else:
    days = duration // 86400
    hour = (duration % 86400) // 3600
    min = ((duration % 86400) % 3600) // 60
    sec = ((duration % 86400) % 3600) % 60
    print(days, "days", hour, " hours", min, "min", sec, "sec")
