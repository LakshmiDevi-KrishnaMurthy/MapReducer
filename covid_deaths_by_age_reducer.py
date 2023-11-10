#!/usr/bin/python
import sys

current_age_group = None
total_deaths = 0
total_count = 0

for line in sys.stdin:
    line = line.strip()
    age_group, deaths = line.split('\t')
    try:
		if current_age_group is None:
		current_age_group = age_group

		if age_group == current_age_group:
		total_deaths += int(deaths)
		total_count += 1
		else:
		if total_count > 0:
			average_deaths = float(total_deaths) / total_count
			print '%d\t%.2f' % (int(current_age_group), average_deaths)
		current_age_group = age_group
		total_deaths = int(deaths)
		total_count = 1
	except ValueError:
		# Handle the case where age or deaths cannot be converted to integers
		print("Invalid input:", line)
		continue  # Skip this line and continue with the next one

if current_age_group is not None and total_count > 0:
    average_deaths = float(total_deaths) / total_count
    print '%d\t%.2f' % (int(current_age_group), average_deaths)

