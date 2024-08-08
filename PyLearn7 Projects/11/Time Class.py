from datetime import datetime


class Time:
    def __init__(self, seconds=0, minutes=0, hours=0):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours
        self.total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds

    def normalize(self):
        if self.seconds < 0:
            self.minutes += self.seconds // 60
            self.seconds = self.seconds % 60
        if self.minutes < 0:
            self.hours += self.minutes // 60
            self.minutes = self.minutes % 60
        if self.hours < 0:
            raise ValueError("Subtraction of Time is not Eligible due to Negativity.")
        if self.seconds >= 60:
            self.minutes += self.seconds // 60
            self.seconds = self.seconds % 60
        if self.minutes >= 60:
            self.hours += self.minutes // 60
            self.minutes = self.minutes % 60
        self.hours = self.hours % 24
        return self.hours, self.minutes, self.seconds

    def to_seconds(self):
        return self.total_seconds

    def from_seconds(self, seconds=0):
        self.hours = seconds // 3600
        self.minutes = (seconds % 3600) // 60
        self.seconds = seconds % 60
        return self.hours, self.minutes, self.seconds

    def add_time(self, hours=0, minutes=0, seconds=0):
        self.hours += hours
        self.minutes += minutes
        self.seconds += seconds
        self.normalize()
        return self.hours, self.minutes, self.seconds

    def subtract_time(self, hours=0, minutes=0, seconds=0):
        self.hours -= hours
        self.minutes -= minutes
        self.seconds -= seconds
        self.normalize()
        return self.hours, self.minutes, self.seconds

    def utc_conversion(self):
        utc_time = Time(hours=int(datetime.utcnow().strftime("%H")),
                        minutes=int(datetime.utcnow().strftime("%M")),
                        seconds=int(datetime.utcnow().strftime("%S")))
        zone_hour, zone_minute, zone_seconds = utc_time.add_time(hours=3, minutes=30, seconds=0)
        print(f"{zone_hour}:{zone_minute}:{zone_seconds}")


first_time = Time(hours=7, minutes=0, seconds=0)

normalized_hour, normalized_minutes, normalized_seconds = first_time.normalize()
print(f"Normalized Time is {normalized_hour}:{normalized_minutes}:{normalized_seconds}")

subtracted_hour, subtracted_minute, subtracted_second = first_time.subtract_time(hours=0, minutes=400, seconds=1000)
print(f"After Subtracted time : {subtracted_hour}:{subtracted_minute}:{subtracted_second}")

added_hour, added_minute, added_second = first_time.add_time(hours=1, minutes=114, seconds=652)
print(f"After Added time : {added_hour}:{added_minute}:{added_second}")

total_seconds = first_time.to_seconds()
print(f"Total seconds is {total_seconds}")

new_hour, new_minute, new_second = first_time.from_seconds(seconds=650)
print(f"After Subtracted time : {new_hour}:{new_minute}:{new_second}")

zone_time = Time()
zone_time.utc_conversion()