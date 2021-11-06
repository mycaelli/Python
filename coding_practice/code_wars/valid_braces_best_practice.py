"""Determines if the order of the braces (in string) is valid 
    braces: () [] {} 
    valid order: (){}[] ([{}])
    invalid order: {) [({})](]
    
    
    ( [ { } 
"""

def validBraces1(string) :
    """possibly bigger than O(n)"""

    for inner in ["{}", "()", "[]"] :
        print(inner)
        string = string.replace(inner, "")
    if len(string) == 0 :
        return True 
    else :
        return False


def validBraces2(string) :
    """O(n)"""
    
    close_map = {"(" : ")" , "[" : "]", "{" : "}"} #hashmap that maps each opening char to its closing char 
    opens = [] #stack that keeps track of all the oppening tracks seen 
    
    for symbol in string :
        if symbol in close_map.keys(): #checks if the symbol is one of the dict keys
            opens.append(symbol)
        elif opens == [] or symbol != close_map[opens.pop()]: #if stack is empty or the closing symbol doesnt match the last open char
            return False 
    
    return True
            

print(validBraces2("([}{])"))
print(validBraces2("{}()[]"))
print(validBraces2("()"))
print(validBraces2("([)]"))

