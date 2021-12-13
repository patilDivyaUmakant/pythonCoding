# x = ["I am a good boy","I am divya"]
# y = "I"
# if y in x :
#     print ('hi')
d1 = {"a" : "pizza", "b" : "burger", "c" : "iceCream"}
# print (d1["c"])
# print (d1.keys())
# print (d1.values())
# print (d1.items())

list1 = [["a",1],["b",2],["c",3]]
# for i in list1:
#     print (i)
# for i,j in list1:
#     print (i,"eats",j,"tofees")

d2 = dict(list1)
print(d2)
for name,toffees in d2.items() :
    print(name,"eats",toffees,"toffees")
