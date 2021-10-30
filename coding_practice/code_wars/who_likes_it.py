
"""
[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

"""

def likes(names) :
    if not names :
        text = "no one likes this"
        return text
    elif len(names) == 1 :
        text = str(names[0]) + " likes this"
        return text
    elif len(names) == 2 :
        text = str(names[0]) + " and " + str(names[1]) + " like this"
        return text
    elif len(names) == 3 :
        text = str(names[0] + ", " + str(names[1] + " and " + str(names[2] + " like this")))
        return text
    else :
        text = str(names[0]) + ", " + str(names[1]) + " and " + str(len(names)-2) + " others like this"
        return text
    
#likes([])
#likes(["Peter"])
#likes(["Jacob", "Alex"])
#likes(["Max", "John", "Mark"]      )
#likes(["Alex", "Jacob", "Mark", "Max"])
#likes(["Alex", "Jacob", "Mark", "Max", "Alex", "Jacob", "Mark", "Max"])