seconds = int(input("Seconds: "))

if seconds >= 60:
    minutes = 0
    minutes += (seconds//60)
    new_seconds = seconds % 60
    if minutes >= 60:
        hour = 0
        hour += (minutes // 60)
        new_minutes = minutes % 60
        print(f"{seconds} seconds is equal to {hour}:{new_minutes}:{new_seconds}")
    else:
        print(f"{seconds} seconds is equal to {minutes}:{new_seconds}")

else:
    print(f"{seconds} seconds is equal to {seconds} seconds!! (Dummy)")

