class Time_object: 

    def __init__(self, hour, min):
        self.hour = int(hour)
        self.min = int(min)

    # custom method to add time
    def __add__(self, other):
        return Time_object(self.hour + other.hour, self.min + other.min)
    
    # method how to show the object
    def __repr__(self):
        return f"{self.hour:02d}:{self.min:02d}"


class Time_calculator:

    @staticmethod
    def calculate_time(start_time, duration, day_of_week = "MON"):
        
        # split the strings to extract the hour and minute integers 
        start_hour, start_min = start_time.split(":")
        duration_hour, duration_minute = duration.split(":")

        # create objects to use with the custom methods
        start_time_object = Time_object(start_hour, start_min)
        duration_time_object = Time_object(duration_hour, duration_minute)

        # perform the addition, return the result
        return start_time_object + duration_time_object

# test run 1
print(Time_calculator.calculate_time("10:05", "3:20"))
