hours = int(input("Hours = "))
minutes = int(input("Minutes = "))
seconds = int(input("Seconds = "))

# Convert to Seconds
to_seconds = (60 * ((hours * 60) + minutes)) + seconds

# Handling Values Greater than 60 Seconds from User
if seconds >= 60:
    minutes += (seconds//60)
    seconds -= (60 * (seconds//60))

# Handling Values Greater than 60 Minutes from User
if minutes >= 60:
    hours += (minutes // 60)
    minutes -= (60 * (minutes // 60))

# Print Demanded Output
print(f"{hours}:{minutes}:{seconds} is equal to {to_seconds} seconds.")