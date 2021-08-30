#a start time in the 12-hour clock format (ending in AM or PM)
#a duration time that indicates the number of hours and minutes
#(optional) a starting day of the week, case insensitive

"""The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show (next day) after the time. 
If the result will be more than one day later, it should show (n days later) after the time, 
where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should 
display the day of the week of the result. The day of the week in the output should appear after 
the time and before the number of days later."""

def add_time(start, duration, day = ''):
	days_of_the_week = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')

	time = start.split()[0]
	start_time_of_day = start.split()[1]
	
	start_hour = int(time.split(':')[0])
	start_minutes = int(time.split(':')[1])
	
	duration_hours = int(duration.split(':')[0])
	duration_minutes = int(duration.split(':')[1])
	
	finish_hour = start_hour + (duration_hours % 24)
	finish_minutes = start_minutes + duration_minutes

	days_later = duration_hours // 24

	
	if finish_minutes >= 60:
		finish_hour += 1
		finish_minutes -= 60

	if finish_hour > 12:
		finish_hour -= 12
		if start_time_of_day == 'PM':
			time_of_day = 'AM'
			days_later += 1
		else:
			time_of_day = 'PM'
	elif finish_hour == 12 and finish_minutes > 0:
		if start_time_of_day == 'PM':
			time_of_day = "AM"
			days_later += 1
		else:
			time_of_day = "PM"
	else:
		time_of_day = start_time_of_day
	
	if days_later == 0:
		number_of_days = ''
	elif days_later == 1:
		number_of_days = ' (next day)'
	else:
		number_of_days = f' ({days_later} days later)'

	if day.lower() in days_of_the_week:
		start_day_index = days_of_the_week.index(day.lower())
		end_day_index = (start_day_index + days_later) % 7

		end_day = days_of_the_week[end_day_index]

		new_time = f"{finish_hour}:{finish_minutes:02d} {time_of_day}, {end_day.title()}{number_of_days}"
	else:
		new_time = f"{finish_hour}:{finish_minutes:02d} {time_of_day}{number_of_days}"

	return new_time


def main():
	value = add_time("2:59 AM", "24:00", "saturDay")
	print(value)

if __name__ == '__main__':
	main()