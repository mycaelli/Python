def validBraces(string):
  
    if len(string) % 2 != 0 :
        return False
  
    verify = 0  
    ini = 0
    fin = len(string)
    
    print(string)

    for i, value in enumerate(string) :
        ''' print("i " + str(i) + " value " + value)
        print("ini " + string[ini] + " ini+1 " + string[ini+1])
        print("fin " + string[fin-1])
        print("verify: " + str(verify))'''
        if value == string[ini+1] :
            print("if: ")
            print("value " + value + "compare " + string[ini+1])
            verify = verify + 1
            i = i + 2
        elif value == string[fin-1] :
            print("elif: ")
            print("value " + value + "compare " + string[fin-1])
            verify = verify + 1
            fin = fin - 1

        print("verify " + str(verify))
        
    if verify == len(string) / 2 :
        print("true")
        return True
    else :
        print("false")
        return False

#validBraces("()")
validBraces("[(])")
