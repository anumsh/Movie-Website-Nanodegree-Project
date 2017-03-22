class Parent():
    def  __init__(self,last_name,eye_color):
        print("parent constructor called")
        self.last_name=last_name
        self.eye_color=eye_color
    def show_info(self):  # this function will shoe variables values of parent class
         print ("last_name- "+self.last_name)
         print ("eye color - "+self.eye_color)
         
class Child(Parent):
    def __init__(self,last_name,eye_color,number_of_toys):
        print("child constructor called")
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toys = number_of_toys
    def show_info(self):  # this function will show the varaibles values of child class
         print ("last_name- "+self.last_name)
         print ("eye color - "+self.eye_color)
         print("number of toys-" +str(self.number_of_toys))
        
babli = Parent("sharma","black")
#babli.show_info()
#print(babli.last_name)

anum = Child("AAAA","brown",4)
anum.show_info()
#print(anum.last_name)
#print(anum.eye_color)
#print(anum.number_of_toys)'''
