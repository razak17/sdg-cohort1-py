def convert_to_days(data):
    number_of_days = None

    if data["periodType"] == "months":
        number_of_days = data["timeToElapse"] * 30

    elif data["periodType"] == "weeks":
        number_of_days = data["timeToElapse"] * 7

    elif data["periodType"] == "days":
        number_of_days = data["timeToElapse"]

    return number_of_days


def requested_time(data):
    if data["periodType"] == "months":
        return 2 ** int((data["timeToElapse"] * 30) / 3)

    elif data["periodType"] == "weeks":
        return 2 ** int((data["timeToElapse"] * 7) / 3)

    return 2 ** int(data["timeToElapse"] / 3)
