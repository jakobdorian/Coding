def timeConversion(s):
    # extract hour, minute, second, and period (AM/PM)
    hour = int(s[:2])
    minute = s[3:5]
    second = s[6:8]
    period = s[8:]

    # convert hour to 24-hour format
    if period == 'AM':
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12

    # format hour to be two digits
    hour = f'{hour:02}'

    # construct the final time string in 24-hour format
    return f'{hour}:{minute}:{second}'
