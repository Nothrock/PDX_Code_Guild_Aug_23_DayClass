current_time =input('What time is it?: ')

# find out if am or pm
meridian = current_time[-2:]
time = int(current_time[:-2])

#what are our mealtimes
if meridian.lower() == 'am':
    if 7 <= time <= 9:
        print("{} is Breakfast time!".format(current_time))
    elif time == 12 or time >= 1 and time <= 4:
        print("{} is Hammer time!".format(current_time))
    else:
        print("This doesn\'t seem like a good time to eat, dude.")
elif meridian.lower() == 'pm':
    if time == 12 or time == 1 or time == 2:
        print("{} is Lunch time!".format(current_time))
    elif time >= 7 and time <= 9:
        print("{} is Dinner time!".format(current_time))
    elif time >= 10 and time <= 11:
        print("{} is Hammer time!".format(current_time))
    else:
        print("This doesn\'t seem like a good time to eat, dude.")
else:
    print("This doesn\'t seem like a good time to eat, dude.")
