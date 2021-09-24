def get_memory_score(input_nums):
   mylist1=[]
   mylist2=[]
   Score=0 

   ok=False
   for index in range(len(input_nums)):
       if type(input_nums[index])!= int:
           ok=True
           mylist2.append(input_nums[index])
   if ok:
      return mylist2
   else:
      for index in range(len(input_nums)):
        if input_nums[index] in mylist1:
               Score+=1
        else: 
               if len(mylist1)<5:
                   mylist1.append(input_nums[index]) 
               else:
                   del mylist1[0]
                   mylist1.append(input_nums[index])    

      return Score 



input_nums =   [1,2,3,4,5]


if type(get_memory_score(input_nums))!=int:
  print('Please enter a valid input list. Invalid inputs detected:',get_memory_score(input_nums))
else:  
  print('Score:',get_memory_score(input_nums)) 
