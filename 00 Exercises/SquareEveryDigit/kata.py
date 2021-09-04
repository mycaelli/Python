'''In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.'''

def square_digits(num):
    
    numberS = str(num)
    res = ""
    for n in numberS:
        print(n)
        aux = int(n) ** 2
        print(aux)
        res = res + str(aux) 
        print(res)
    
    return int(res)

print(square_digits(8748))

#64491664