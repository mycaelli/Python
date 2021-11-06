def find_short(s) :
    """Return the length of the shortest word"""
    words = s.split()
    
    shortest = min(words, key=len)
    
    return len(shortest)

