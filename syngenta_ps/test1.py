#lib that supports regular expressions
import re
from datetime import datetime

#   User inputs
input_dados_cliente = input("<tipo_do_cliente>: <data1>, <data2>, <data3> \n")

input_list = re.split(r"[,:]\s*",input_dados_cliente)

#checa o tipo de cliente
if input_list[0].lower() == "rewards" or input_list[0].lower() == "reward":
    client = 1
elif input_list[0].lower() == "regular":
    client = 0
else:
    print("Ivalid client type")
    print("Try: Reward or Regular")
    exit()

#print(client)
input_list.pop(0)

print(input_list)
#formata os dias da semana
for valid_day in input_list:
    if "tues" in valid_day or "thur" in valid_day:
        input_list.remove(valid_day) #remove a string errada da lista
        valid_day = valid_day[:-2] + ")" #formata a string corretamente
        input_list.append(valid_day)

print(input_list)

for date in input_list:
    try:
        datetime.strptime(date, "%d%b%Y(%a)")
    except:
        print("Invalid date format")
        print("Valid format example: 08Fev2009(mon)")

#contando os dias passados
week = 0
wknd = 0
for day in input_list:
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

#print(result)
#print("--------------------------------------------------")
if result[0][2] == result[1][2] == result[2][2]:
    result.sort(key = lambda x: x[1], reverse=True) 
elif result[0][2] == result[1][2]:
    result.pop()
    result.sort(key = lambda x: x[1], reverse=True)
#print(result[0][0])
