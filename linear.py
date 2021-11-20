print ('This is a linear search code')

def linearSearch(arr,x) :
    
    for i in range(len(arr)) : 
      if arr[i] == x :
        search = arr[i]              
        return search  

    return -1     
while(True):   
 arr1 = [1,3,5,6,10,15,19,24,29]   
 x = int(input('Please enter a number that you want to search : '))   
 linear = linearSearch(arr1,x)
 if linear == -1:
   print('the number you have entered is not in the list')
 else :
   print(linear,'is there is the list')

# if linear = :
#     print(linear,'is there is the list')
# else :     
#     print ('the number is not in the list')
