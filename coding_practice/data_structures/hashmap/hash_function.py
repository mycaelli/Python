'''
define a simple hash function 
'''


class Hash_Function:
    
    #defines a hash to a given string key considering a 5 elements array
    def hash(sef, key) :
        index = 0 
        for char in key :
            index += ord(char) 
        return index % 6

if __name__ == "__main__" :
    
    hf = Hash_Function()
    print(hf.hash("William"))
    print(hf.hash("Kate"))
    print(hf.hash("Bob"))
    print(hf.hash("Rose"))
     