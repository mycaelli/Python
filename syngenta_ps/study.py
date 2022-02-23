#input que nao existe
#datas invalidas


#lib that supports regular expressions
import collections
import re

#   User inputs
input_dados_cliente = input("<tipo_do_cliente>: <data1>, <data2>, <data3> \n")

#specify the regular expression pattern in the first parameter and the target character string in the second parameter
#Enclose a string with [] to match any single character in it. It can be used to split by multiple different characters
#\s - Lowercase 's'. Matches a single whitespace character like: space, newline, tab, return.
#https://pynative.com/python-regex-split/
#https://www.quora.com/What-does-an-R-mean-before-a-string-in-Python
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
input_list.pop(0) #tira o regular/reward da lista

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

#print(hotels)

#se for reward 
#1 3
#sort list
#https://www.geeksforgeeks.org/defaultdict-in-python/
prices = []

if client: 
    prices.append(hotels["Lakewood"][1] * week + hotels["Lakewood"][3] * wknd)
    prices.append(hotels["Bridgewood"][1] * week + hotels["Bridgewood"][3] * wknd)
    prices.append(hotels["Ridgewood"][1] * week + hotels["Ridgewood"][3] * wknd)
else:
    prices.append(hotels["Lakewood"][0] * week + hotels["Lakewood"][2] * wknd)
    prices.append(hotels["Bridgewood"][0] * week + hotels["Bridgewood"][2] * wknd)
    prices.append(hotels["Ridgewood"][0] * week + hotels["Ridgewood"][2] * wknd)



stars = [3, 4, 5]
names = ["Lakewood", "Bridgewood", "Ridgewood"]

result = list(zip(names, stars, prices))
result.sort(key = lambda x: x[2])

print(result)
print("--------------------------------------------------")
if result[0][2] == result[1][2] == result[2][2]:
    result.sort(key = lambda x: x[1], reverse=True) 
elif result[0][2] == result[1][2]:
    result.pop()
    result.sort(key = lambda x: x[1], reverse=True)
print(result[0][0])
