def pretty_time(timestamp):
    time_arr = str(timestamp).split('.')
    hour = int(time_arr[0].split(':')[0])
    minute = time_arr[0].split(':')[1]
    tod = 'AM'

    if hour > 12:
        hour -= 12
        tod = 'PM'

    return f'{hour}:{minute} {tod}'
