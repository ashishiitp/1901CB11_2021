#import os
#os.system("cls")
 

def meraki_helper(n):#function to find whether the number is meraki or not
    a=n
    count=0 #finding count of no of digits in an integer
    while a!=0:
       count+=1  # loop for finding the count  
       a//=10
    if count==1: #checking if a number is of single digit
           return True
    for i in range(0,count-1): #loop for traversing through the digit 
        x=n%10
        n=n//10 # finding the adjacent digit every time
        y=n%10 
        if abs(y-x)!=1: #checking if difference not comes out to be 1 terminating the loop
         return False
         break
       
    return True #otherwise returning true
         
         
input = [12, 14, 56, 78, 98, 54, 678, 134, 789, 0, 7, 5, 123, 45, 76345, 987654321]


meraki_count=0

nonmeraki_count=0

for index in range(len(input)): #traversing the list of input
    if meraki_helper(input[index])==True: #if condition satisfied printing the number with yes
        meraki_count+=1;
        print('YES -',input[index],'is a Meraki number')
    else:
        nonmeraki_count+=1; #if not satisfied printing number with no
        print('NO -',input[index],'is not a Meraki number')
        
print('The input list contains',meraki_count,'meraki and',nonmeraki_count,'non meraki numbers.') #printing the count of meraki and non meraki number    


