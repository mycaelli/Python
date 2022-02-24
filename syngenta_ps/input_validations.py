#lib that supports regular expressions
import re
from datetime import datetime

def reservations():
    #   User inputs
    input_data = input("<tipo_do_cliente>: <data1>, <data2>, <data3> \n")
    data = re.split(r"[,:]\s*",input_data)
    # CHECK CLIENT HERE
    client = check_client(data)
    data.pop(0) #removes client from list
    # CHECK VALID DATE
    data = check_date(data)

    #count days
    week = 0
    wknd = 0
    for day in data:
        if "sat" in day or "sun" in day:
            # print("aqui")
            wknd = wknd + 1
        else:
            # print("aqui")
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
        # print("Rewards")
        # print("Lake week: ", week, hotels["Lakewood"][1], " weekend: ", wknd, hotels["Lakewood"][3])
        # print("Bridg week: ", week, hotels["Bridgewood"][1], " weekend: ", wknd, hotels["Bridgewood"][3])
        # print("Ridg week ", week, hotels["Ridgewood"][1], " weekend: ", wknd, hotels["Ridgewood"][3])
    else:
        prices.append(hotels["Lakewood"][0] * week + hotels["Lakewood"][2] * wknd)
        prices.append(hotels["Bridgewood"][0] * week + hotels["Bridgewood"][2] * wknd)
        prices.append(hotels["Ridgewood"][0] * week + hotels["Ridgewood"][2] * wknd)
        # print("Lake week: ", week, hotels["Lakewood"][1], " weekend: ", wknd, hotels["Lakewood"][3])
        # print("Bridg week: ", week, hotels["Bridgewood"][1], " weekend: ", wknd, hotels["Bridgewood"][3])
        # print("Ridg week ", week, hotels["Ridgewood"][1], " weekend: ", wknd, hotels["Ridgewood"][3])

    result = list(zip(names, stars, prices))
    result.sort(key = lambda x: x[2])
    # print(result)
    if result[0][2] == result[1][2] == result[2][2]:
        result.sort(key = lambda x: x[1], reverse=True) 
    elif result[0][2] == result[1][2]:
        result.pop()
        result.sort(key = lambda x: x[1], reverse=True)
    print(result[0][0])

def check_client(data):
    #checa o tipo de cliente
    if data[0].lower() == "rewards" or data[0].lower() == "reward":
        return True
    elif data[0].lower() == "regular":
        return False
    else:
        print("Ivalid client type")
        print("Try: Reward or Regular")
        exit()

def check_date(data):
    #formata os dias da semana
    for valid_day in data:
        if "tues" in valid_day or "thur" in valid_day:
            data.remove(valid_day) #remove a string errada da lista
            #print(valid_day)
            valid_day = valid_day[:-2] + ")" #formata a string corretamente
            #print(valid_day)
            data.append(valid_day)
    for date in data:
        try:
            datetime.strptime(date, "%d%b%Y(%a)")
        except:
            print("Invalid date format")
            print("Valid format example: 08Feb2009(mon)")
            exit()
    return data

reservations()