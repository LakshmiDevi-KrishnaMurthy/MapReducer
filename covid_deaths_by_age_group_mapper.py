#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip()
    _,_,_,_,_,Age,_,_,Deaths,_,_,_ = line.split(',')
    
    
    try:
        Age = int(Age)
        Deaths = int(Deaths)
    except ValueError:
        # Handle the case where age or deaths cannot be converted to integers
        print("Invalid input:", line)
        continue  # Skip this line and continue with the next one
    
    age_group = (Age // 10) * 10  # Group ages into 10-year ranges
    print('%d\t%s' % (age_group, Deaths))
 
