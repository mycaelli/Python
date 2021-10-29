'''
Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
'''

maxNum = int(input())

odd_numbers = []

for i in range(maxNum+1) :
    if i % 2 != 0 :
        odd_numbers.append(i)
        

