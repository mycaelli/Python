import math

def expanded_form(num):
    """ Return (int) num as a string in expanded form : 
        12 -> '10 + 2' """
    
    lst = []
    i = 0
    while num != 0 :
        value = num % 10
        num = num // 10
        if value == 0 :
            i+=1
            continue
        lst.append(value * int(math.pow(10, i)))
        i += 1
    
    result = ''
    for number in reversed(lst) :
        if number == lst[0] :
            result += str(number)
            return result
        result += str(number) + " + "
        

