def convert_to_24_hour_format(hour, minute, period):

    if (period == "pm" or period=="PM") and hour != 12:
        hour += 12
    elif (period == "am" or period=="AM") and hour == 12:
        hour = 0

    time_24_hour = f"{hour:02d}{minute:02d}"

    return time_24_hour

