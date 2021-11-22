print ('This is a binary search')
def binarySearch(arr,start,end,i) :
    # print ('inside binary search')
    if end >= start :
        
        # print (arr,start,end,i)
        mid = (start + end)// 2
        if arr[mid] == i :
            return mid
        elif i < arr[mid] :
            return binarySearch(arr,start,mid-1,i)
        else : 
            return binarySearch(arr,mid+1,end,i)   
    else :
        return -1   


while True : 
    arr = sorted(["a","b","h","z","i","u","x"])
    # print (arr)
    userInput  = input('please input the alphabet you want to search : ')
    result = binarySearch(arr,0,len(arr)-1,userInput)
    if result != -1 :
        print ("The value that you are searching is at the index",result )
    else :
        print ("The value that you are searching is not in the array. ")
