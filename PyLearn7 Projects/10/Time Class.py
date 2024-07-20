class Time():
    def __init__(self, seconds, minutes, hours):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours
        self.normalize()

    def normalize(self):
        if self.seconds <= 0 and self.minutes <= 0 and self.hours <= 0:
            raise ValueError("The Desired Time Must contain Positive values.")
        if self.seconds >= 60:
            self.minutes += self.seconds // 60
            self.seconds = self.seconds % 60
        if self.minutes >= 60:
            self.hours += self.minutes // 60
            self.minutes = self.minutes % 60
        self.hours = self.hours % 24
        print(f"The Normalized form of the Desired Time is {self.hours} hours, {self.minutes} minutes and {self.seconds} seconds.")

    def to_seconds(self):
        print(f"Total Seconds is : {self.hours * 3600 + self.minutes * 60 + self.seconds} Seconds.")

    def add_time(self, hours=0, minutes=0, seconds=0):
        self.hours += hours
        self.minutes += minutes
        self.seconds += seconds
        self.normalize()

    def subtract_time(self, hours=0, minutes=0, seconds=0):
        self.hours -= hours
        self.minutes -= minutes
        self.seconds -= seconds
        self.normalize()


time1 = Time(minutes=90, hours=1, seconds=600)
time1.subtract_time(hours=2, minutes=11)