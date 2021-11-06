def validBraces(string) :
    """Determines if the order of the braces (in string) is valid 
    braces: () [] {} 
    valid order: (){}[] ([{}])
    invalid order: {) [({})](]
    """
    if len(string) % 2 != 0 :
        return False
    
    flag = 0
    index = 0
    revindex = -1

    if len(string) == 2 :
        if string[0] == "(" and string[-1] == ")" :
            return True
        elif string[0] == "[" and string[-1] == "]" :
            return True
        elif string[0] == "{" and string[-1] == "}" :
            return True 
        else :
            return False
        
    
    while index < len(string) :
        if revindex < (len(string) / 2 * (-1))  :
            if string[-2] == "(" and string[-1] == ")" :
                flag += 1
            if string[-2] == "[" and string[-1] == "]" :
                flag += 1
            if string[-2] == "{" and string[-1] == "}" :
                flag += 1
            break
        if string[index] == "(" :
            if string[revindex] == ")" or string[index+1] == ")" :
                flag += 1
        if string[index] == "[" :
            if string[revindex] == "]" or string[index+1] == "]" :
                flag += 1
        if string[index] == "{" :
            if string[revindex] == "}" or string[index+1] == "}" :
                flag += 1
        index += 1
        revindex -= 1
    
        
    if flag == len(string) / 2 :
        return True
    else :
        return False
        
            
#print(validBraces("([}{])"))
#print(validBraces("{}()[]"))
# print(validBraces("()"))
#print(validBraces("([)]"))

