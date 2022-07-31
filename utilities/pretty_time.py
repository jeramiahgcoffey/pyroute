def pretty_time(timedelta):
    """
    Format timedelta to a 12-hour clock time string.

    :param timedelta: Timedelta object to format.
    :return: String. The formatted time.
    """

    time_arr = str(timedelta).split('.')
    hour = int(time_arr[0].split(':')[0])
    minute = time_arr[0].split(':')[1]
    tod = 'AM'

    if hour > 12:
        hour -= 12
        tod = 'PM'

    return f'{hour}:{minute} {tod}'
