'''
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190


1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list based on this

'''

arr = [2200, 2350, 2600, 2130, 2190]

for i in range(len(arr)) :
    #1 item
    fisrtq = abs(arr[-1] - arr[1])
    #3 item 
    if arr[i] == 2000 :
        print("2000 is a lot of money")
    

#2 item
secondq = arr[0] + arr[1] + arr[2]

#4 item 
arr.append(1980)

#5 item

arr[3] = arr[3] - 200

for num in arr :
    print(num)

