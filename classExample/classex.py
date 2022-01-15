class Cat:
    var1 = "mammal"
    var2 = "cat"
    var3 = "brown Cat" 

    def fun(self):
        print ("i am a "+ self.var1)
        print ("i am a "+ self.var2)
        print ("i am a "+ self.var3)

obj = Cat()        
print (obj.var1)
obj.fun()