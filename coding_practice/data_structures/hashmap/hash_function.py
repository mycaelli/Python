'''
define a simple hash function 
'''
class Hash_Function:
    def hash(sef, key) :
        #arr index == 57
        index = 0 
        for char in key :
            index += ord(char) 
        #index %= 53
        return index % 6

if __name__ == "__main__" :
    
    hf = Hash_Function()
    print(hf.hash("William"))
    print(hf.hash("Kate"))
    print(hf.hash("Bob"))
    print(hf.hash("Rose"))
     