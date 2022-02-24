import re
from datetime import datetime

def reservations():
    input_data = input("<client_type>: <date1>, <date2>, <date3> \n")
    user_data = re.split(r"[,:\s]\s*",input_data)
    client = check_client(user_data)
    user_data.pop(0)
    user_data = check_date(user_data)

    week = 0
    wknd = 0
    for day in user_data:
        if "sat" in day or "sun" in day:
            wknd = wknd + 1
        else:
            week = week + 1

    hotels = {
        "Lakewood": [110, 80, 90, 80],
        "Bridgewood": [160, 110, 60, 50],
        "Ridgewood": [220, 100, 150, 40]
    }

    prices = []
    stars = [3, 4, 5]
    names = ["Lakewood", "Bridgewood", "Ridgewood"]
    if client: 
        prices.append(hotels["Lakewood"][1] * week + hotels["Lakewood"][3] * wknd)
        prices.append(hotels["Bridgewood"][1] * week + hotels["Bridgewood"][3] * wknd)
        prices.append(hotels["Ridgewood"][1] * week + hotels["Ridgewood"][3] * wknd)
    else:
        prices.append(hotels["Lakewood"][0] * week + hotels["Lakewood"][2] * wknd)
        prices.append(hotels["Bridgewood"][0] * week + hotels["Bridgewood"][2] * wknd)
        prices.append(hotels["Ridgewood"][0] * week + hotels["Ridgewood"][2] * wknd)
    result = list(zip(names, stars, prices))
    result.sort(key = lambda x: x[2])
    if result[0][2] == result[1][2] == result[2][2]:
        result.sort(key = lambda x: x[1], reverse=True) 
    elif result[0][2] == result[1][2]:
        result.pop()
        result.sort(key = lambda x: x[1], reverse=True)
    print(result[0][0])

def check_client(user_data):
    if user_data[0].lower() == "rewards" or user_data[0].lower() == "reward":
        return True
    elif user_data[0].lower() == "regular":
        return False
    else:
        exit()

def check_date(user_data):
    if(not user_data):
        exit()
    set_data = set(user_data)
    for valid_day in set_data:
        if "tues" in valid_day or "thur" in valid_day:
            set_data.remove(valid_day)
            valid_day = valid_day[:-2] + ")"
            set_data.add(valid_day)
    for date in set_data:
        try:
            datetime.strptime(date, "%d%b%Y(%a)")
        except:
            exit()
    return set_data

reservations()