class Hotel:

    def __init__(self, name, week_rg, weekend_rg, week_rw, weekend_rw ,stars):
        self.name = name
        self.week_rg = week_rg
        self.weekend_rg = weekend_rg
        self.week_rw = week_rw
        self.weekend_rw = weekend_rw
        self.stars = stars
    
    def details(self):
        print("Name is: {}".format(self.name))
        print("Regular week taxes: {}".format(self.week_rg))
        print("Regular weekend taxes: {}".format(self.weekend_rg))
        print("Reward week taxes: {}".format(self.week_rw))
        print("Reward weekend taxes: {}".format(self.weekend_rw))
        print("Stars: {}".format(self.stars))

Lakewood = Hotel("Lakewood", 110, 90, 80, 80, 3)
Bridgewood = Hotel("Bridgewood", 160, 60, 110, 50, 4)
Ridgewood = Hotel("Ridgewood", 220, 150, 100, 40, 5)

Lakewood.details()
print("--------------------------")
Bridgewood.details()
print("--------------------------")
Ridgewood.details()
print("--------------------------")

class Client:
    
    def __init__(self, type):
        self.type = type

    def details(self):
        print("Client's type: {}".format(self.type))

    fid_club = 0
    if type == "Reward":
        fid_club = 1

a = Client("Reward")
b = Client("Regular")

a.details()
print("--------------------------")
b.details()
print("--------------------------")

print(a.fid_club)
print(b.fid_club)




########################################
print(hotels)

#se for reward 
#1 3
#sort list
#https://www.geeksforgeeks.org/defaultdict-in-python/
#stars = [3, 4, 5]
prices = []
if client: 
    prices[0] = hotels["Lakewood"][1] * week + hotels["Lakewood"][3] * wknd
    prices[1] = hotels["Bridgewood"][1] * week + hotels["Bridgewood"][3] * wknd
    prices[2] = hotels["Ridgewood"][1] * week + hotels["Ridgewood"][3] * wknd
else:
    prices[0] = hotels["Lakewood"][0] * week + hotels["Lakewood"][2] * wknd
    prices[1] = hotels["Bridgewood"][0] * week + hotels["Bridgewood"][2] * wknd
    prices[2] = hotels["Ridgewood"][0] * week + hotels["Ridgewood"][2] * wknd

#stars_prices = zip(stars, prices)
# print("Lakewood", result_lakewood)
# print("Bridgewood", result_bridgewood)
# print("Ridgewood", result_ridgewood)

print(stars_prices)