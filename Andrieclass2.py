#Object Oriented Programming:
'''
class Student:
    def __init__(self,name,age,ID,gender,dept,section,roll_number):
      if age>20:

        self._name=name #attrubibute with naming convention _name is initialized to make it private variable so that other programmers will not modify it. This naming convention in python is done so because no private keyword is avaiable in python.
        self._age=age #similar as above
        self.ID=ID
        self.gender=gender
        self.dept=dept
        self.section=section
        self.roll_number=roll_number
      
    def merge_roll_number_and_ID(self):
        merger=str(self.roll_number)+str(self.ID)
        print(merger)
    def info_statement(self):
        print(f"This student is {self._name}, His/Her age is {self._age}, the roll number is {self.roll_number}, he/she belongs to {self.dept} department and belongs to section: {self.section}.")
        return ""
student1=Student("Hamza murtaza",22,1800790,"MALE","Software engineering","A",18007)
student2=Student("Usama Amir",22,18003890,"MALE","Electrical engineering","B",180038)
#student3=Student("Huzaifa shuja",19,18003890,"MALE","Electrical engineering","B",180038)
print(student1._name)
print(student1.info_statement())
print(student2.info_statement())
#print(student3.info_statement())'''

# INHERITANCE :


'''

class car:
    def __init__(self,car_name,car_model,car_color,):
        self.car_name=car_name
        self.car_model=car_model
        self.car_color=car_color
    
    def car_age(self):
        if self.car_model<2010:
            print("car is old")
        else:
            print("car is new")

class racing_car(car):
    def __init__(self,car_speed,car_engine,design):
        car.__init__(self,"supra",2018,"red")
        
        
        self.car_speed=car_speed
        self.car_engine=car_engine
        self.design=design
        

    
    def how_much_fast(self):
        if self.car_speed>2000:
            print("This car is very fast")
        else:
            print("Not much fast")

supra1=racing_car(2000,2,"fire")
print(supra1.car_age())'''

#error handling:
'''
try:
    number_1=int(input("enter a number please"))
except:
    print("you have not enter a number !")
else:
    print("good")'''
    
#program to print fibonacci numbers using generators:
'''
def fib(num):
    a=0
    b=1
    for i in range(num):
        yield a
        temp=a
        a=b
        b=temp+a

for m,x in enumerate(fib(20)):#for printing 20 fibonacci numbers
    print(m,x)'''







    