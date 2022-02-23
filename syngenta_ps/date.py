from datetime import datetime

test = "16Mar2009(thu)"

#format = "%d%b%Y(%a)"

try:
    datetime.strptime(test, "%d%b%Y(%a)")
    print("funfo")
except:
    print("no no")
