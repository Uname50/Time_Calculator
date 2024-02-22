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
        duration_hour, duration_min = duration.split(":")

        # create objects to use with the custom methods
        start_time_object = Time_object(start_hour, start_min)
        duration_time_object = Time_object(duration_hour, duration_min)

        # perform the addition
        added_time = start_time_object + duration_time_object

        # convert overlapping minutes into hours 
        overlap_minute = added_time.min // 60
        if overlap_minute >= 1:
            added_time.hour += overlap_minute
            added_time.min -= 60*overlap_minute

        # flag for the next day indication
        is_next_day = False
        days_after = 0

        # convert overlapping hours into days
        overlap_hour = added_time.hour // 24
        if overlap_hour == 1:
            added_time.hour -= 24*overlap_hour
            days_after = 1
            is_next_day = True
        
        elif overlap_hour >= 2:
            added_time.hour -= 24*overlap_hour
            days_after = overlap_hour
            is_next_day = False

        if days_after == 0:
            return added_time
        elif is_next_day:
            return f"{added_time}, next day"
        else:
            return f"{added_time}, {days_after} days after"

# test run 
print(Time_calculator.calculate_time("00:00", "75:70"))
