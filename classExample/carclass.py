class Car:
   color = "red"
   type = "supercar"
   name = "Ferrari"

   def car(self,a):
       print("My car color is "+self.color + a)
       print("My car type is "+self.type)
       print("My car name is "+self.name)


myCar = Car()
print(myCar.name)
myCar.car("a")

c1 = Car()
print(c1.color)
c1.car("b")