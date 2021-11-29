print("This project is going to change 12 hour timing format to 24 hours")
def convert24(str1) :
    if str1[-2:] == "AM" and str1[0 : 2] == "12" :
        return "00"+ str1[2 : -2]
    elif str1[-2 :] == "AM" :
        return str1[0 : -2]
    elif str1[-2:] == "PM" and str1[0 : 2] == "12" :
        return str1[0 : -2]
    elif str1[0 : 2] > "12" :
        return str1[0 : -2]
    else :
        return str(int(str1[0 : 2])+12)+str1[2 : -2]

    # print(str1)

print(convert24("08:10:20 PM"))  
# 12 : 08 : 20 AM
# 00 : 08 : 20  