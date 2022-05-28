




from ast import And
from itertools import count


print("hello world")


var1=type(7.6)
print(var1)

print(type("a"))
var2=7.99776553344546556557674634242446757453434465757453434
print(type(var2))

go1=567//23
print(type(go1))
if type(go1)==int:
    print("the result is an integer because double division operator returns the floor value of quotient")

value=3**2
print(value)
for x in range(1,11):
    print(x*"*")
    


move=4*"s"
print(move)
print(int(5))
print("s")

print("*")
print("**")
print("***")

for v in [[1,1,3,4],[9,9,9,9]]:
    for c in v:
        print(c)
    print("\n")

print(bin(3))
print(int("0b11",base=2))
    
#BINARY TO DECIMAL COVERSION PROGRAM:
'''bin_number=input("enter binary number in the format 0b00")
dec_number=int(bin_number,base=2)
print("The decimal number of given number is:"+str(dec_number))'''

'''#formatted strings
my_name="Hamza Murtaza"
my_age=22
my_percentage=89.0
print("I am "+my_name+"and my age is "+str(my_age)+"and my percentage is "+str(my_percentage))
#this statement of print can also be written using formatted strings in a very easy way:
print(f"My name is {my_name} and my age is {my_age} and my percentage is {my_percentage}")'''

#booleans
b=True
print(type(b))
var4=bool(())
print(var4)

'''#birth year calculator program:
name=input("Enter your name please\n")
age=int(input("Enter your age please\n"))
birth_year=2022-age
print(f"{name}, your birth year is {birth_year}\n")
print("Thank you for using our software.")'''

'''#user name and password account creation and password checker:
the_name=input("Enter your full name\n")
the_password=input("Enter your password\n")
length_of_password=len(the_password)
stars=length_of_password*"*"
print(f"{the_name}, your account is successfully created !\n")
print("Please login now\n")
print(
    \''' -----------------------------------------------------------------------
            |              Welcome To Airways login                |
            |                                                      | 
            |                                                      |
            |                                                      |
            |            AEROPLANE RESERVATION SYSTEM              |                           
            |          "Pakistan's no.1 Airways for you"           |                                     
            |                                                      |
            |                                                      | 
        ------------------------------------------------------------------------

    \'''
)
login_name=input("enter name for login")
login_password=input("enter password for login")
print("wait for Authentication service......")
if login_name==the_name and login_password==the_password:
    print("user name and password is correct !\n")
    print("login successfull")
    print(f"{login_name}, your password {stars} is {length_of_password} characters long")

elif login_name!=the_name or login_password!=the_password:
    print("username or password is incorrect\n")
    print("retry please")
else:
    print("error occured !")'''

'''#print the following numbers of list in reverse order.

list1=[1,2,3,4,5,6,7]
list2=[]
for a in range(1,8):
    list2.append(list1[-a])
print(list2)'''

#program to covert a character into ASCII code:
char1="1"
char_to_ASCII=ord(char1)
print(char_to_ASCII)

'''#program to find whether user has entered a number or not:
user_input=input("Enter a number please")
ascii_generator=ord(user_input)
if ascii_generator>=48 and ascii_generator<=57:
    print("USER HAS ENTERED A NUMBER")
else:
    print("USER HAS NOT ENTERED A NUMBER")'''
    
#to covert ASCII code into character:
ASCII_code=48
ASCII_code_to_character=chr(ASCII_code)
print(ASCII_code_to_character)

'''#prgoram to count items of list and also tell total:
my_list=[1,2,3,4,5,6,7,8,9,10]
i=1
for x in  my_list:
    print(str(i)+"......"+str(x))
    i=i+1
print("there are "+str(i-1)+"items in the list")'''

'''#program to print a shape:
shape= [[0,0,0,1,0,0,0],
        [0,0,1,1,1,0,0],
        [0,1,1,1,1,1,0],
        [1,1,1,1,1,1,1],
        [0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0]
]

for x in shape:
    for y in x:
        if y==0:
            print(" ",end="")
        else:
             print("*",end="")
    print("")'''

'''#program to print duplicates in the list:
given_list=["a","a","b","c","d","e","e"]

duplicates=[]
for x in given_list:
    if given_list.count(x)>1:
        if x not in duplicates:
         duplicates.append(x)

print(duplicates)'''

'''#program to write duplicate items only once in the list:
see_list=["a","b","c","c","a","d","e","e"]
pure_list=[]

for x in see_list:
    if see_list.count(x)>=1:
        if x not in pure_list:
            pure_list.append(x)
print(pure_list)'''

#*args and **kwargs:

def my_func(*num): #*num is an *args parameter that recieve more than one values from function call
    print(*num)
    sum(num)
    return sum(num)

result=my_func(1,2,3,4,5)
print(result)

#**kwargs is used for keyword arguments if used in the function call:
def myanother(**kwargs):
    print(kwargs)
    print(kwargs.values())

myanother(num=1,num2=4,num3=5)

'''#print the highest even number using function:
def highest_even(Li):
    evens=[]
    for x in Li:
        if x % 2 ==0:
            evens.append(x)
    max(evens)
    return max(evens)

                       
f_result=highest_even([2,3,4,5,8,10,13,15,17,18])
print(f_result)'''









    
             







    

    

        













