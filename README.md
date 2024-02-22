# Time_Calculator 

```
Program that calculates time using following requirements: 

- start time to be in the 24-hour clock format
- a duration time that indicates the number of hours and minutes, and an optional starting day of the week, case insensitive

The program adds the duration time to the start time and returns the result.

If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

Examples: 

add_time("3:00", "3:10")
# Returns: 6:10

add_time("11:30", "2:32", "Monday")
# Returns: 2:02, Monday

add_time("11:43", "00:20")
# Returns: 12:03 

add_time("10:10", "3:30")
# Returns: 1:40 (next day)

add_time("11:43", "24:20", "tueSday")
# Returns: 12:03, Thursday (2 days later)

add_time("6:30", "205:12")
# Returns: 7:42 (9 days later)

```