def add_time(start, duration, show_day = None):
    
    hour = int(start.split()[0].split(':')[0].strip())
    min = int(start.split()[0].split(':')[1].strip())
    am_pm = start.split()[1]
    
    added_hour = int(duration.split(':')[0].strip())
    added_min = int(duration.split(':')[1].strip())

    change_am_pm = {
        'AM': 'PM',
        'PM':'AM'
    }
    
    next_day = None
    if (min + added_min) >= 60:
        hour += int((min+added_min)/60)
        min =  (min + added_min) % 60
        
    else:
        min += added_min
    
    hour+=added_hour

    
    if added_hour >=24:

        
    
    if hour >= 12 :
        if am_pm == 'PM':
            next_day = True
        hour = hour % 12
        am_pm = change_am_pm[am_pm]


    if hour == 0: hour = 12
    if min >=10:
        if next_day == True: return f"{hour}:{min} {am_pm} (next day)"
        else: return f"{hour}:{min} {am_pm}"
    else:
        if next_day == True: return f"{hour}:{'0'+str(min)} {am_pm} (next day)"
        else: return f"{hour}:{'0'+str(min)} {am_pm}"