import re
str = "one two three four five six seven eight 9 10"
patt = re.compile(r"\d")
result = patt.findall(str)
for i in result : 
    print (i)
    
# print (r"\n")
# escape sequential characters are : \n \r \a ......
# 'r' is going to give you a raw string .. example , print (r"\n") 