def add_time(start, duration, show_day = None):
    
    hour = int(start.split()[0].split(':')[0].strip())
    min = int(start.split()[0].split(':')[1].strip())
    am_pm = start.split()[1]
    
    added_hour = int(duration.split(':')[0].strip())
    added_min = int(duration.split(':')[1].strip())

    day_to_number = {
        'Monday' : 1,
        'Tuesday': 2,
        'Wednesday': 3,
        'Thursday' : 4,
        'Friday' : 5,
        'Saturday' : 6,
        'Sunday' : 7
    }

    number_to_day = dict([(value, key) for key, value in day_to_number.items()])
    days = 0
    while added_hour != 0: # add hours
        hour += 1
        added_hour -= 1

        if hour == 12:
            hour = 0
            if am_pm == 'AM': am_pm = 'PM'
            else:
                am_pm = 'AM'
                days +=1

    if (min + added_min) >= 60:
        hour += int((min+added_min)/60)
        if hour == 12:
            hour = 0
            if am_pm == 'AM': am_pm = 'PM'
            else:
                am_pm = 'AM'
                days +=1

        min =  (min + added_min) % 60
    else: min += added_min

    if hour == 0: hour = 12 

    if show_day != None:
        day = day_to_number[str(show_day).lower().capitalize()]
        days_2 = days
        while days_2 > 0:
            day += 1
            days_2 -= 1
            if day == 8: day = 1
        
        if days == 0:
            if min >= 10: return f"{hour}:{min} {am_pm}, {number_to_day[day]}"
            else: return f"{hour}:{'0'+str(min)} {am_pm}, {number_to_day[day]}"
        elif days == 1:
            if min >= 10: return f"{hour}:{min} {am_pm}, {number_to_day[day]} (next day)"
            else: return f"{hour}:{'0'+str(min)} {am_pm}, {number_to_day[day]} (next day)"
        else:
            if min >= 10: return f"{hour}:{min} {am_pm}, {number_to_day[day]} ({days} days later)"
            else: return f"{hour}:{'0'+str(min)} {am_pm}, {number_to_day[day]} ({days} days later)"

    if days == 0:
        if min >= 10: return f"{hour}:{min} {am_pm}"
        else: return f"{hour}:{'0'+str(min)} {am_pm}"
    elif days == 1:
        if min >= 10: return f"{hour}:{min} {am_pm} (next day)"
        else: return f"{hour}:{'0'+str(min)} {am_pm} (next day)"
    else:
        if min >= 10: return f"{hour}:{min} {am_pm} ({days} days later)"
        else: return f"{hour}:{'0'+str(min)} {am_pm} ({days} days later)"
        

    
