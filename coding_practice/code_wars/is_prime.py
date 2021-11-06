
import math

def is_prime(num):
    """Return true if num is a prime number and false if it is not"""
    if num <= 0 or num == 1:
        return False
   
    i=2
    while i <= math.floor(math.sqrt(num)) :
        if num % i == 0.0 :
            return False
        i+=1
    
    return True
    
        
