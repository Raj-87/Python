def add_time(start, duration, starting_day=None):
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))

    if period == 'PM' and start_hour != 12:
        start_hour += 12
    elif period == 'AM' and start_hour == 12:
        start_hour = 0

    dur_hour, dur_minute = map(int, duration.split(':'))

    total_minutes = start_minute + dur_minute
    extra_hour = total_minutes // 60
    new_minute = total_minutes % 60

    total_hours = start_hour + dur_hour + extra_hour
    days_passed = total_hours // 24
    final_hour_24 = total_hours % 24

    if final_hour_24 == 0:
        final_hour = 12
        period = 'AM'
    elif final_hour_24 < 12:
        final_hour = final_hour_24
        period = 'AM'
    elif final_hour_24 == 12:
        final_hour = 12
        period = 'PM'
    else:
        final_hour = final_hour_24 - 12
        period = 'PM'

    new_minute = str(new_minute).zfill(2)
    new_time = f"{final_hour}:{new_minute} {period}"

    if starting_day:
        start_index = days_of_week.index(starting_day.strip().capitalize())
        new_day = days_of_week[(start_index + days_passed) % 7]
        new_time += f", {new_day}"

    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"

    return new_time


# Now call the function:
print(add_time("11:43 PM", "24:20", "tueSday"))
