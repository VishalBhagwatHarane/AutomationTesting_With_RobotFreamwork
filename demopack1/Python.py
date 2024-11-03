# def my_function(x):
#     return 5 *x
# print(my_function(4))
# print(my_function(5))
# print(my_function(8))

# def find_square(num):
#     result=num*num
#     print(result)
# square=find_square(5)
# print('Square:',square)

# def find_square(num):
#  result = num * num
#  return result
# # function call
# square = find_square(3)
# print('Square:',square)

# def greet():
#  print("Helllo")
#  greet()
# greet()

# def greet():
#  print("Hello")
#  greet()
# greet()

# def count(num):
#  if num<=0:
#   print('stop')
#  else:
#   print(num)
#   count(num-1)
# count(5)

# def factorial(n):
#  if n==0:
#   return 1
#  else:
#   return n* factorial(n-1)
# num=int(input("Enter a number: "))
# print(factorial(num))

# def fib(n):
#  if n==0:
#   return 0
#  elif n==1:
#   return 1
#  else:
#   return fib(n-1)+fib(n-2)
# num=int(input("Enter a number: "))
# print(fib(num))

# def Fibonacci(n):
#  if n<0:
#   print("Incorrect input")
#  elif n==0:
#   return 0
#  elif n==1 or n==2:
#   return 1
#  else:
#   return Fibonacci(n-1)+Fibonacci(n-2)
# print(Fibonacci(9))

# def fib(n):
#     previsouno=0
#     preprevisouno=1
#     print(previsouno)
#     print(preprevisouno)
#     for i in range(2,n):
#         c=preprevisouno+previsouno
#         previsouno=preprevisouno
#         preprevisouno=c
#         print(preprevisouno+previsouno)
# fib(6)

# def fib(n):
#     previsouno=0
#     preprevisouno=1
#     if n==1:
#         print(previsouno)
#     else:
#         print(previsouno)
#         print(preprevisouno)
#         for i in range(2,n):
#             c=previsouno+preprevisouno
#             previsouno=preprevisouno
#             preprevisouno=c
#             print(preprevisouno+previsouno)
# fib(8)

# def f():
#     s='i love Automation'
#     print(s)
# f()

# def f():
#     s='i love automation'
#     print('inside function',s)
# f()

# def greet():
#     message='Hello'
#     print('Local',message)
# greet()

# def f():
#     s='Me too'
#     print(s)
# s='Love automation'
# print(s)
# f()

# message='Hello'
# def greet():
#     print("local",message)
# greet()
# print('Global',message)

# c=1
# def add():
#     print(c)
# add()

# c=1
# def add():
#     c=c+2
#     print(c)
# add()

# c=1
# def add():
#     global c
#     c=c+2
#     print(c)
# add()

# def outer_function():
#     num=20
#     def inner_fuction():
#         global num
#         num=25
#     print("Before calling inner fuction:",num)
#     inner_fuction()
#     print("After calling inner function:",num)
# outer_function()
# print('Outside both function:',num)

# def f():
#     global s
#     s+=' GFG'
#     print(s)
#     s='Look for Geeksforgeeks Python section'
#     print(s)
# s='Python is great!'
# f()
# print(s)

# import Module1
#
# Module1.add(12,12)
# Module1.sub(12,12)
# Module1.mul(12,12)
# Module1.div(12,12)

# from Module1 import *
# add(12,1)
# sub(2,3)
# mul(2,6)
# div(2,3)

# import Module1 as a
# a.add(343,33)
# a.mul(34,3)
# a.div(33,22)
# a.mul(33,2)

# import math
# # print(math.sqrt(33))
# print(math)
# print(math.factorial(22))

# print(help("modules"))
# print(help("math"))

# import math
# x=dir()
# print(x)

# import india
# import bharat
# india.indian()
# india.bharatiya()
# bharat.indian()
# bharat.bharatiya()
#
# from india import *
# from bharat import *
# indian()
# bharatiya()

# num=[3,4,5,7]
# if len(num)>3:
#     raise Exception (f"Length of the given list must be less than or equal to 4 but (lem{num})")

# x=-1
# if x<0:
#     raise Exception('Sorry no number below zero')

# try:
#     raise NameError("Hi there")
# except NameError:
#     print("An exception")
#     # raise

# try:
#     x=int(input("Enter a number: "))
#     if x>100:
#         raise ValueError(x)
# except ValueError:
#     print(x,'is out of allowed range')
# else:
#     print(x,'is within the allowed range')

# f=open("demofile.txt")
# print(f.read())

# f=open('demofile.txt','r')
# print(f.read(7))


# f=open('demofile.txt','r')
# print(f.readline())

# f=open('demofile.txt','r')
# for x in f:
#     print(x)

# f=open('demofile.txt','r')
# print(f.readline())
# f.close()

# f=open('demofile.txt','a')
# f.write("Now the file has more content")
# f.close()

# f=open('demofile.txt','r')
# print(f.read())
# f.close()

# f=open('demofile.txt','w')
# f.write("Woops i have deleted the content")
# # print(f.read())
# f.close()
#
# f=open("demofile.txt",'r')
# print(f.read())

# f=open("demo2.txt",'x')
# f=open("myfile.txt",'w')

# f=open("myfile",'w')
# f=open('geek.txt','w')
# f.write("This isthe write command")
# f.write("It allows us to write in a particular file")
# f.close()

# import os
# os.remove('demo2.txt')
# import os
# os.rename("demofile.txt",'fileee.txt')

# with open("geek1.txt",'w') as f:
#     content=f.write("Vishal")
#     f.close()
# with open("geek1.txt",'a')as f:
#     f.write("MAyur")
#     f.close()
# with open('fffff.txt','r') as f:
#     print(f.read())

# import os
# try:
#     os.remove('fileee.txt')
#     print('The file is removed')
# except FileNotFoundError:
#     print("The file is not present")

# import os
# if os.path.exists("geek.txt"):
#     os.remove("geek.txt")
# else:
#     print("THe file does not exist")

# class Myclass:
#     def myfun(self):
#         pass
#
#     def display(self,name):
#         print('Name is: ',name)
# mc=Myclass()
# mc.myfun()
# mc.display('Vishal')

# class Myclass():
#     def m1(self):
#         print("We are printing instance method")
#
#     @staticmethod
#     def m2():
#         print("We are printing static method")
# mc1=Myclass()
# mc1.m2()

# class Myclass():
#     def m1(self):
#         print("We are printing instance Method")
#
#     @staticmethod
#     def m2(self):
#         print("We are printing static method")
# mc1=Myclass()
# mc1.m2("vvv")

# class Myclass():
#     def m1(self):
#         print("we are printing instance method")
#
#     @staticmethod
#     def m2():
#         print("We are printing static method")
# mc1=Myclass()
# mc1.m2()
# mc1.m1()

# class Myclass2:
#     a=100
#     b=200
#     def add(self):
#         print(self.a+self.b)
#     def mul(self):
#         print(self.a*self.b)
#
# mc2=Myclass2()
# mc2.add()
# mc2.mul()

# i,j=100,300
# class myclass3:
#     a,b=10,20
#     def add(self,x,y):
#         print(x+y)
#         print(self.a+self.b)
#         print(i+j)
# mc3=myclass3()
# mc3.add(23,22)

# a,b=100,200
# class Myclass:
#     a,b=10,20
#     def add(self,a,b):
#         print(a+b)
#         print(self.a+self.b)
#         print(globals()['a']+globals()['b'])
#
# mc4=Myclass()
# mc4.add(23,22)

# class Myclass5:
#     def add(self,x,y):
#         print(x+y)
# mc5=Myclass5()
# mc6=Myclass5()
# mc5.add(33,44)
# mc6.add(0,44)

# class Myclass5:
#     def add(self,x,y):
#         print(x+y)
#     def display(self):
#         print('Helllo')
# mc5=Myclass5()
# mc6=Myclass5()
# mc6.add(33,44)
# mc6.display()
# mc5.add(33,44)
# mc5.display()

# class Myclass5:
#     def add(self,x,y):
#         print(x+y)
#     def display(self):
#         print("Hello")
# mc5=Myclass5()
# mc5.add(1000,2)
# mc5.display()
# Myclass5().add(33,44)
# Myclass5().display()

# class Myclass5:
#     def add(self,x,y):
#         print(x+y)
#     def display(self):
#         print('Hello')
# mc4=Myclass5()
# mc4.add(33,33)
# mc4.display()
# mc5=Myclass5()
# mc5.add(33,33)
# mc5.display()
# print(id(mc4))
# print(id(mc5))


# class Myclass7():
#     def __init__(self):
#         print("This is constructor")
# mc7=Myclass7()


# class Myclass0():
#     def __init__(self,name):
#         print(name)
# mc=Myclass0("Vishal")

# class Myclass():
#     name='Amit'
#     def __init__(self,name):
#         print(name)
#         print(self.name)
# mcc=Myclass("Vishal")

# class Myclass:
#     def values(self,val1,val2):
#         print(val1)
#         print(val2)
#     def add(self):
#         print(val1+val2)
# mc5=Myclass()
# mc5.values(56,33)
# mc5.add()

# class Myclass8:
#     def value(self,val1,val2):
#         print(val1)
#         print(val2)
#         self.val1=val1
#         self.val2=val2
#     def add(self):
#         print(self.val1+self.val2)
# mc8=Myclass8()
# mc8.value(34,33)
# mc8.add()

# class Myclass8:
#     def __init__(self,val1,val2):
#         print(val1)
#         print(val2)
#         self.val1=val1
#         self.val2=val2
#     def add(self):
#         print(self.val2+self.val1)
# mc8=Myclass8(33,44)
# mc8.add()

# class Myclass9:
#     def m1(self):
#         print("This is m1 method")
#         self.m1(100)
#     def m2(self,a):
#         print("This is m2 method and value of argumentis: ",a)
# m9=Myclass9()
# # m9.m1()
# m9.m2(4)

# class emp:
#     def __init__(self,eid,ename,esal):
#         self.eid=eid
#         self.ename=ename
#         self.esal=esal
#     def display(self):
#         print("Eid: {} ,Enpname: {}, EmpSal: {}".format(self.eid,self.ename,self.esal)
#               )
#
# e1=emp('h168685','Vishal','30000')
# e1.display()


# class A:
#     def m1(self):
#         print("This m1 method is from parent A")
#
# class B(A):
#     pass
#
# b1=B()
# b1.m1()

# class A:
#     def m1(self):
#         print("This m1 method is from Parent A")
# class B(A):
#     def m2(self):
#         print("This m2 methos is from parent B")
# aobj=A()
# aobj.m1()
#
# Bobj=B()
# Bobj.m1()
# Bobj.m2()

# class Parent:
#     def flats(self,delhi,Pune):
#         print("Parent ka flat hai Delhi mai",delhi)
#         print("Unka Pune bhi flat hai",Pune)
# class Child(Parent):
#     def Print(self):
#         print("Mere kuch nahi")
#         print("Parent ka sab apna hai")
# c=Child()
# c.flats('1BHK','2Bhk')
# c.Print()

# class A:
#     a,b=100,200
#     def m1(self):
#         print(self.a+self.b)
# class B(A):
#     x,y=11,22
#     def m2(self):
#         print(self.x+self.y)
# bobj=B()
# bobj.m2()
# bobj.m1()

# class A:
#     a,b=100,200
#     def m1(self):
#         print(self.a+self.b)
# class B(A):
#     x,y=10,20
#     def m2(self):
#         print(self.x+self.y)
# class C(B):
#     i,j=11,22
#     def m3(self):
#         print(self.i+self.j)
# aobj=A()
# aobj.m1()
#
# bobj=B()
# bobj.m1()
# bobj.m2()
#
# cobj=C()
# cobj.m1()
# cobj.m2()
# cobj.m3()

# class A():
#     def m1(self):
#         print("This is m1 method of Parent A")
# class B(A):
#     def m2(self):
#         print("This is m2 method of Child B")
# class C(A):
#     def m3(self):
#         print("This is m3 method of GrandChild C")
# b1=B()
# b1.m2()
# b1.m1()
#
# c1=C()
# c1.m1()
# c1.m3()

# class A():
#     def m1(self):
#         print("This is m1 method of Parent A")
# class B():
#     def m2(self):
#         print("This is m2 method of Child B")
# class C(A,B):
#     def m3(self):
#         print("This is m3 method of GrandChild C")
#
# a1=A()
# a1.m1()
#
# b1=B()
# b1.m2()
#
# c1=C()
# c1.m1()
# c1.m2()
# c1.m3()


# class A():
#     def m1(self):
#         print("This is m1 method of Parent A")
# class B(A):
#     def m2(self):
#         print("This is m2 method of Child B")
#         super().m1()
# bobj=B()
# bobj.m2()

# class A:
#     a,b=100,200
#     def m1(self):
#         print(self.a+self.b)
# class B(A):
#     i,j=10,20
#     def m2(self,x,y):
#         print(x+y)
#         print(self.i+self.j)
#         print(self.a+self.b)
# bobj=B()
# bobj.m2(33,44)

# a,b=200,200
# class A:
#     a,b=20,22
#     def m1(self):
#         print(self.a+self.b)
# class B(A):
#     a,b=10,20
#     def m2(self,a,b):
#         print(a+b)
#         print(self.a+self.b)
#         # print(self.a+self.b)
#         print(super().a+super().b)
#         print(globals()['a']+globals()['b'])
# bobj=B()
# bobj.m2(1,2)

# class A():
#     def __init__(self):
#         print("This is constructor of Parent A")
# class B(A):
#     pass
# bobj=B()

# class A():
#     def __init__(self):
#         print("This is constructor of Parent A")
# class B(A):
#     def __init__(self):
#         print("This is constructor of Parent B")
# bobj=B()

# class A():
#     def __init__(self):
#         print("This is constructor of Parent A")
# class B(A):
#     def __init__(self):
#         print("This is constructor of Parent B")
#         super().__init__()
#         A.__init__(self)
#
# bobj=B()

# print(len("geeks"))
# print(len([11,22,33]))

# def add(x,y,z=0):
#     return x+y+z
# print(add(23,3))
# print(add(22,33,44))

# class India():
#     def capital(self):
#         print("New Delhi is the capital of India")
#     def language(self):
#         print("Hindi is the most widely spoken language of India")
#     def type(self):
#         print("India is developing country.")
# class USA():
#     def capital(self):
#         print("Washington D.C is the capital of USA")
#
#     def language(self):
#         print("English is the primary languange of USA.")
#     def type(self):
#         print("USA is developed country")
# obj_ind=India()
# obj_usa=USA()
#
# for country in (obj_usa,obj_ind):
#     country.type()
#     country.capital()
#     country.language()

# class Bird:
#     def intro(self):
#         print("There are many types of birds:")
#     def fight(self):
#         print("Most of the birds can fly but some cannot")
# class sparrow(Bird):
#     def fight(self):
#         print("Sparrows can fly.")
# class ostrich(Bird):
#     def fight(self):
#         print("Ostriches cannot fly.")
#
# obj_bird=Bird()
# obj_spr=sparrow()
# obj_ost=ostrich()
# obj_bird.intro()
# obj_bird.intro()
# obj_spr.intro()
# obj_spr.fight()
# obj_ost.intro()
# obj_ost.fight()

# class India():
#     def capital(self):
#         print("New Delhi is the capital of India.")
#     def language(self):
#         print("Hindi is the most widely spoken language of India.")
#
#     def type(self):
#         print("India is a developing country")
# class USA():
#     def capital(self):
#         print("Washington D.C is the capital of USA.")
#     def language(self):
#         print("English is the primary language os USA.")
#
#     def type(self):
#         print("USA is developed country.")
# def func(obj):
#     obj.capital()
#     obj.language()
#     obj.type()
# obj_ind=India()
# obj_usa=USA()
# func(obj_usa)
# func(obj_ind)

# class Animal:
#     def speak(self):
#         raise NotImplementedError("Subclass must implement this method")
#
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
# class Cat(Animal):
#     def speak(self):
#         return 'Meow!'
# animals=[Dog(),Cat()]
#
# for animal in animals:
#     print(animal.speak())


# class Parent():
#     def __init__(self):
#         self.value='Inside Parent'
#
#     def show(self):
#         print(self.value)
#
# class Child(Parent):
#     def __init__(self):
#         self.value="inside child"
#
#     def show(self):
#         print(self.value)
# obj1=Parent()
# obj2=Child()
#
# obj1.show()
# obj2.show()


# class Animal:
#     name=''
#     def eat(self):
#         print("I can eat")
# class Dog(Animal):
#     def eat(self):
#         print("I like to eat bones")
# labrador=Dog()
# labrador.eat()

# class Animal:
#     name=''
#
#     def eat(self):
#         print("I can eat")
# class Dog(Animal):
#     def eat(self):
#         super().eat()
#         print("I like to eat bones")
#
# labrador=Dog()
# labrador.eat()

# def product(a,b):
#     p=a*b
#     print(p)
# # product(12,11)
#
# def product(a,b,c):
#     p=a*b*c
#     print(p)
# # product(12,11)
# product(12,11,22)

# def add(datatype,*args):
#     if datatype=='int':
#         answer=0
#     if datatype=='str':
#         answer=''
#     for x in args:
#         answer=answer+x
#     print(answer)
# add('int',5,6)
# add('str','Hi','Geeks')

# class Myclass5:
#     def add(self,x,y):
#         print(x+y)
#     def display(self):
#         print("Hello")
# mc5=Myclass5()
# mc5.add(100,200)
# mc5.display()
# mc5.add(11,22)
# mc5.display()

# from abc import ABC,abstractmethod
#
# class Car(ABC):
#     def mileage(self):
#         pass
#
# class Tesla(Car):
#     def mileage(self):
#         print("The mileage is 30kmph")
# class Suzuki(Car):
#     def mileage(self):
#         print("The mileage is 25kmph")
# class Duster(Car):
#     def mileage(self):
#         print("The mileage is 24kmph")
# class Renault(Car):
#     def mileage(self):
#         print("The mileage is 27kmph")
# t=Tesla()
# t.mileage()
#
# r=Renault()
# r.mileage()
#
# s=Suzuki()
# s.mileage()

# from abc import ABC
# class Polygon(ABC):
#     def sides(self):
#         pass
# class Triangle(Polygon):
#     def sides(self):
#         print("Triangle has 3 sides")
# class Pentagon(Polygon):
#     def sides(self):
#         print("Pentagon has 5 sides")
# class Hexagon(Polygon):
#     print("Hexagon has 6 sides")
# class square(Polygon):
#     def sides(self):
#         print("I have 4 sides")
# t=Triangle()
# t.sides()
#
# s=square()
# s.sides()
#
# p=Pentagon()
# p.sides()
#
# k=Hexagon()
# k.sides()

# class Employee:
#     def __init__(self,name,project):
#         self.name=name
#         self.project=project
#     def work(self):
#         print(self.name,'is working on',self.project)
# emp=Employee("Vishal",'Telecome')

# class Employee:
#     def __init__(self,name,salary,project):
#         self.name=name
#         self.salary=salary
#         self.project=project
#
#     def show(self):
#         print("Name:",self.name,'Salary:',self.salary)
#
#     def work(self):
#         print(self.name,'is working on',self.project)
# emp=Employee('Vishal',90000,'NPl')
# emp.show()
# emp.work()

# class Employee:
#     def __init__(self,name,salary,project):
#         self.name=name
#         self._project=project
#         self.__salary=salary


# class myclass():
#     __a=10
#     def display(self):
#         print(self.__a)
# obj=myclass()
# obj.display()

# class myclass():
#     __a=10
#     x=20
#     def display(self):
#         print(self.x)
#         print(self.__a)
# obj=myclass()
# obj.display()


# class myclass():
#     __a=10
#     x=20
#     def display(self):
#         print(self.x)
#         print(self.__a)
# obj=myclass()
# obj.display()

# class myclass():
#     __a=10
#     x=20
#     print(__a)
#     def display(self):
#         print(self.__a)
# obj=myclass()
# obj.display()
# print(myclass.x)

# class myclass():
#     def __display(self):
#         print("This is private method")
#     def show(self):
#         print("This is public method")
# obj=myclass()
# obj.__display()
# obj.show()


# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self._salary=salary
#     def show(self):
#         print("Name:",self.name,'Salary:',self.salary)
# emp=Employee("Vishal",1000)
# emp.show()

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.__salary=salary
#     def show(self):
#         print("Name:",self.name,'Salary:',self.__salary)
# emp=Employee("Vishal",10000)
# emp.show()

# print()

# p=float(input("Enter the principal amount: "))
# r=float(input("Enter the rate of interset"))
# t=float(input("Enter the time period: "))
# interest=(p*r*t)/100
# print("Simple Interest:",interest)

# num=int(input("Enter a number:"))
# if num%2==0:
#     print("Even")
# else:
#     print("Odd")

# import math
# radius=float(input("Enter the radius of the circle:"))
# area=math.pi*radius*radius
# print("Area:",area)

# squares=[i**2 for i in range(10)]
# print(squares)
#
# for i in range(10):
#     print(i**2)

# with open("Output.txt",'r') as file:
#     data=file.read()
#     print("Data from file:",data)
# with open('Output.txt','w') as file:
#     file.write("Hello this is a sample text")
# with open("Output.txt") as file:
#     data=file.read()
#     print("Data from file:",data)

# def is_palindrome(s):
#     return s==s[::-1]
# string=input("Enter a string:")
# if is_palindrome(string):
#     print("Palidrome")
# else:
#     print("Not a palindrome")

# a = float(input("Enter the first number: "))
# b = float(input("Enter the second number: "))
# c = float(input("Enter the third number: "))
# max_num=max(a,b,c)
# print("Largest Number:",max_num)

# num=int(input("Enter a number:"))
# for i in range(1,11):
#     print(f'{num}x {i}={num*i}')

# celsius = float(input("Enter temperature in Celsius: "))
# fahreheit=(celsius*9/5)+32
# print("Temperature in Fahrenheit:",fahreheit)

# string = "Hello, World!"
# print('Length of the string:',len(string))
# print('Uppercase:',string.upper())
# print('Lowercase:',string.lower())
# print("Reversed string",string[::-1])

# def is_leap_year(year):
#     if (year%4==0 and year%100 !=0) or (year%400):
#         return True
#     return False
# year=int(input("Enter a Year:"))
# if is_leap_year(year):
#     print("Leap Year")
# else:
#     print("Not a leap year")

# def count_vowels(s):
#     vowels='aeipuAEIPU'
#     count=0
#     for char in s:
#         if char in vowels:
#             count+=1
#     return count
# string=input("Enter a string")
# print("Number of vowels:",count_vowels(string))

# def computerlcm(x,y):
#     if x>y:
#         greater=x
#     else:
#         greater=y
#     while True:
#         if greater%x==0 and greater%y==0:
#             lcm=greater
#             break
#         greater+=1
#     return lcm
# num1=int(input("Enter a number: "))
# num2=int(input("Enter second number: "))
# print("LCM: ",computerlcm(num2,num2))

# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         return self.length*self.width
# length=float(input("Enter length of the rectangle: "))
# width=float(input("Enter width of the rectangle: "))
# rect=Rectangle(length,width)
# print("Area of the rectangle: ",rect.area())

# def is_anagra(s1,s2):
#     return sorted(s1)==sorted(s2)
# string=input("Enter first sting: ")
# string2=input("Enter sencond string: ")
# if is_anagra(string,string2):
#     print("Anagrams")
# else:
#     print("No anagrams")

# import random
# print("Random number:",random.randint(1,100))

# def binary_serch(arr,x):
#     low= 0
#     high=len(arr)-1
#     while low<=high:
#         mid=(low+high)
#         if arr(mid)<x:
#             low=mid+1
#         elif arr[mid]>x:
#             high=mid-1
#         else:
#             return mid
#     return -1
# arr=[2,3,4,10,40]
# x=10
# result=binary_serch(arr,x)
# if result!=-1:
#     print("Enter found at index",result)
# else:
#     print("Element not found")



# import keyword
# print(keyword.kwlist)
# print("Hello world")

# def fib(n):
#     a,b=0,1
#     count=0
#     if n<=0:
#         print("Please enter postive integer")
#     elif n==1:
#         print(f"Fibacci sequence up to {n} term:{a}")
#     else:
#         print(f"fibonacci sequence upq to {n} term")
#         while count<n:
#             print(a,end=" ")
#             nth=a+b
#             a=b
#             b=nth
#             count+=1
# n_terms=10
# fib(n_terms)


# def fibonacci(n):
#     a,b=0,1
#     series=[]
#     for _ in range(n):
#         series.append(a)
#         a,b=b,a+b
#     return series
# n=int(input("Enter number: "))
# fib_series=fibonacci(n)
# print("Fibonacci series ",fib_series)

# number=[0, 1, 1, 2, 3, 5, 8, 13]
# sorted_nummber=sorted(number,reverse=True)
# print(sorted_nummber)

# def fibbco(n):
#     a,b=0,1
#     series=[]
#     for _ in range(n):
#         series.append(a)
#         a,b=a,a+b
#     return series
# n_tre=10
# fib=fibbco(n_tre)
# print('Fibcocoo',fib)

string1='CREDENCE'
# print(string1)
# print(string1[0])
# print(string1[2])
# print(string1)
# print(string1[-3])

String = 'CredenceAutomation'
# print(String[0])
# print(string1[3])
# print(string1[0:4])
# print(String[3:])
# print(String[2:5])
# print(String[::-1])
# print(String[0:7])
# print(String[0:8])
# print(String[-1])
# print(String[-5:-1])
# print(String)
# print(String[1])
# print(String[::-4])
# print(String[::-1])
# print(String[::-2])
# print(String[::3])
# print(String[-3:18])

# copy=String[:]
# print(copy)
# copy = String[0:2]
# print(copy)
# copyy=String[2:7]
# print(copyy)
# copy=str(String)
# print(copy)
# copy='  '+String
# print(copy)
# print(String.capitalize())
# print(String.casefold())
# a="ßABc"
# print(a.casefold())
# print(a.capitalize())
# print(String.count('C'))

# print(String.endswith('Automation'))
String2 = 'CredenceAutomation'
# print(String2.find('A'))
# print(String2.find('C'))
# print(String2.find('e'))
# print(String2.find('A',0))
# print(String2.find('A',11))
# print(String2.find('A',2,3))

# print(String2.format('CLASs'))
# my_string = "{}, is a {},software testing {}, for students"
# print(my_string.format('credence','computre','class'))

# my_string = "{}, is a {} {} software testing for {}"
# print(my_string.format('credence','computre','class','visha'))

# print(String2.index('A'))
# print(String.index('A',1))
# print(String.index('A',9))
# print(String.index('A',10))

# print(String.isalnum())
# String1="123ACS"
# print(String1.isalnum())
# String1 = 'Credence Automation 123 TesTiNG'
# print(String1.isalnum())
# String1 = 'Credence_Automation_TesTiNG'
# print(String1.isalnum())
# String1 = 'Credence_Automation_TesTiNG'
# print(String1.isalnum())
# String1="Credence"
# print(String1.isalnum())

# String = 'Credence_Automation_TesTiNG'
# String1="Credence"
# print(String.isalpha())
# print(String1.isalpha())

# s = "12345"
# print(s.isdecimal())
# s = "12credence34"
# print(s.isdecimal())
# s = "12 34"
# print(s.isdecimal())
# s = "12345"
# print(s.isnumeric())
# s = "12credence34"
# print(s.isnumeric())
# s = "12 34"
# print(s.isnumeric())

# s = "12345"
# print(s.isdigit())
# s = "12credence34"
# print(s.isdigit())
# s = "12 34"
# print(s.isdigit())

# s = "0123"
# print(s.isnumeric())
# # contains alphabets
# s = "0123"
# print(s.isdigit())
# # contains numbers and spaces
# s = "0123"
# print(s.isdecimal())
# s = "2²"
# print(s.isnumeric())
# # contains alphabets
# s = "2²"
# print(s.isdigit())
# # contains numbers and spaces
# s = "2²"
# print(s.isdecimal())

# s = "ↁ"
# print(s.isnumeric())
# # contains alphabets
# s = "ↁ"
# print(s.isdigit())
# # contains numbers and spaces
# s = "ↁ"
# print(s.isdecimal())

# a="yusuf"
# print(a.islower())
# a="yuSuf"
# print(a.islower())
# s = 'Credence For Credence'
# print(s.istitle())
# # First character in first
# # word is lowercase
# s = 'credence For Credence'
# print(s.istitle())
# Third word has uppercas

# s = 'Credence For CREDENCE'
# print(s.istitle())
#
# s = '6041 Is My Number'
# print(s.istitle())

# s = 'CREDENCE'
# print(s.istitle())

# s = 'Credence For Credence'
# print(s.isupper())
# # First character in first
# # word is lowercase
# s = 'credence For Credence'
# print(s.isupper())
# # Third word has uppercase
# # characters at middle
# s = 'Credence For CREDENCE'
# print(s.isupper())
# # Ignore the digit 6041, hence returns True
# s = '6041 Is My Number'
# print(s.isupper())
# # word has uppercase
# # characters at middle
# s = 'CREDENCE'
# print(s.isupper())
#
# s = 'credence For Credence'
# print(s.lower())
# # Third word has uppercase
# # characters at middle
# s = 'Credence For CREDENCE'
# print(s.lower())
# # Ignore the digit 6041, hence returns True
# s = '6041 Is My Number'
# print(s.lower())
# # word has uppercase
# # characters at middle
# s = 'CREDENCE'
# print(s.lower())

# s = 'Credence For Credence'
# print(s.upper())
# # First character in first
# # word is uppercase
# s = 'credence For Credence'
# print(s.upper())

# s = 'Credence For CREDENCE'
# print(s.upper())
# # Ignore the digit 6041, hence returns True
# s = '6041 Is My Number'
# print(s.upper())
# # word has uppercase
# # characters at middle
# s = 'CREDENCE'
# print(s.upper())

# s = 'Credence For Credence'
# print(s.title())
# # First character in first
# # word is titlecase
# s = 'credence For Credence'
# print(s.title())
# # Third word has titlecase
# # characters at middle
# s = 'Credence For CREDENCE'
# print(s.title())
# # Ignore the digit 6041, hence returns True
# s = '6041 Is My Number'
# print(s.title())


# s = 'credence For Credence'
# print(len(s))
# s = 'Credence For CREDENCE'
# print(len(s))
# s = '6041 Is My Number'
# print(len(s))
# s = 'CREDENCE'
# print(len(s))

# string = "grrks FOR grrks"
# new_string=string.replace('r','e')
# print(new_string)
# string = "geeks for geeks \ngeeks for geeks"
# # print(string)
#
# print(string.replace('geeks','GeeksForGeeks'))

# string = "geeks for geeks geeks geeks geeks"
# # print(string.replace("e", "a"))
# print(string.replace('ek','a',3))

# string = "gEEksFORgeeks"
# print(string.swapcase())
# string = "GEEKSFORGEEKS"
# print(string.swapcase())

# String = "Credence"
# print('$'.join(String))
# print(','.join(String))

# s1 = 'abc'
# s2 = '123'
# print('s1 join(s2):',s1.join(s2))
# print('s2 join s1:',s2.join(s1))

# list1 = [1, 2, "Python", "Program", 15.9]
# list2 = ["Amy", "Ryan", "Henry", "Emma"]
# print(list1)
# print(list2)
# print(type(list1))
# print(type(list2))

# list1 = [12, 14, 16, 18, 20]
# list2=list1*2
# print(list2)

# list1 = [1, 2, "Python", "Program", 15.9]
# list2 = ["Amy", "Ryan", "Henry", "Emma"]
# can=list1+list2
# print(can)

# list1 = [12, 14, 16, 18, 20, 23, 27, 39, 40]
# print(len(list1))

# list1 = [12, 14, 16, 39, 40]
# for i in list1:
#     print(i)

# list1 = [100, 200, 300, 400, 500]
# print(600 in list1)
# print(100 in list1)
# print(400 in list1)
# print(200 in list1)
# print(232 in list1)

# a = [ 1, 2, "Ram", 3.50, "Rahul", 5, 6 ]
# b = [ 1, 2, 5, "Ram", 3.50, "Rahul", 6 ]
# print(a==b)

# a = [ 1, 2, "Ram", 3.50, "Rahul", 5, 6]
# b = [ 1, 2, "Ram", 3.50, "Rahul", 5, 6]
# print(a==b)

# my_list = [1, 2, 3, 4, 5]
# print(my_list[:])

# my_list = [1, 2, 3, 4, 5]
# print(my_list[2:])

# my_list = [1, 2, 3, 4, 5]
# print(my_list[2:])

# my_list = [1, 2, 3, 4, 5]
# print(my_list[:2])

# my_list = [1, 2, 3, 4, 5]
# print(my_list[2:4])
# my_list = [1, 2, 3, 4, 5]
# print(my_list[::2])

# my_list = [1, 2, 3, 4, 5]
# print(my_list[::-2])

# my_list = [1, 2, 3, 4, 5]
# # print(my_list[1:4:2])
# # print(my_list[0:6])
# # print(my_list[:])
# print(my_list[2:5])
# print(my_list[1:6:2])

# list = [1,2,3,4,5]
# print(list[-1])
# print(list[-3])
# print(list[:-1])
# print(list[-3:-1])

# Lst = [50, 70, 30, 20, 90, 10, 50]
# # print(Lst[::])
# print(Lst[::-1])
# print(Lst[-7::1])

# List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print("\nOriginal List:\n", List)
# print("\nSliced Lists: ")
# print(List[3:9:2])

# List = ['Geeks', 4, 'geeks !']
# # print("\nOriginal List:\n", List)
# # print("\nSliced Lists: ")
# # # Display sliced list
# # print(List[::-1])
# print(List[::-3])
# # Display sliced list
# print(List[:1:-2])

# List = [-999, 'G4G', 1706256, '^_^', 3.1496]
# print("\nOriginal List:\n", List)
# print("\nSliced Lists: ")
# # Display sliced list
# print(List[10::2])
# # Display sliced list
# print(List[1:1:1])
# Display sliced list
# print(List[-1:-1:-1])
# # Display sliced list
# print(List[:0:])

# )

# List = [-999, 'G4G', 1706256, 3.1496, '^_^']
# # print("\nOriginal List:\n", List)
# # print("\nSliced Lists: ")
# # Modified List
# List[2:4] = ['Geeks', 'for', 'Geeks', '!']
#
# print(List)
# # Modified List
# List[:6] = []
# print(List

# List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print('\nOrinal List:\n',List)
# print('\nSliced lists:')

# newList = List[:3]+List[7:]
# print(newList)
# print(List[:2]+List[7:])
# print(new)

# list = [1, 2, 3, 4, 5, 6]
# print(list)
# list[2]=10
# print(list)

# thislist = ["apple", "banana", "cherry"]
# thislist[1]='blackcurrent'
# print(thislist)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3]=['blackcurrant','watermelon']
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2]=['blackcurrant','watermelon']
# print(thislist)

# animals = ['cat', 'dog', 'rabbit']
# animals.append('Tiger')
# print('Updated animmal list',animals)

# animals list
# animals = ['cat', 'dog', 'rabbit']
# # list of wild animals
# wild_animals = ['tiger', 'fox']
# animals.append(wild_animals)
# print(animals)

# fruits = ['apple', 'banana', 'cherry', 'orange']
# fruits.clear()
# print(fruits)

# list = [{1, 2}, ('a'), ['1.1', '2.2']]
# list.clear()
# print(list)

# Defining a list
# list = [{1, 2}, ('a'), ['1.1', '2.2']]
# del list
# print('list:',list)

# my_list = ['cat', 0, 6.7]
# new_list=my_list.copy()
# print(new_list)

# old_list = [1, 2, 3]
# new_list=old_list
# # old_list=[1,2,3]
# new_list.append('a')
# # print(new_list)
# print(old_list)
# print(new_list)

# list = ['cat', 0, 6.7]
# new_list=list[:]
# new_list.append('dog')
# print('old list',list)
# print('New List',new_list)

# numbers = [2, 3, 5, 2, 11, 2, 7]
# count=numbers.count(2)
# print('Count of 2:',count)

# owels = ['a', 'e', 'i', 'o', 'i', 'u']
# # count=owels.count('i')
# # print(count)
# print('Count of P:',owels.count('p'))

# odd_numbers = [1, 3, 5]
# numbers=[1,4]
# numbers.extend(odd_numbers)
# print(numbers)

# languages = ['French', 'English']
# languages1 = ['Spanish', 'Portuguese']
# languages.extend(languages1)
# print(languages)

# languages = ['French']
# # languages tuple
# languages_tuple = ('Spanish', 'Portuguese')
# languages_set = {'Chinese', 'Japanese'}
# languages.extend(languages_tuple)
# print(languages)
# languages.extend(languages_set)
# print(languages)

# a1 = [1, 2]
# a2 = [1, 2]
# b = (3, 4)
# a1.extend(b)
# print(a1)
# a2.append(b)
# print(a2)

# vowels = ['a', 'e', 'i', 'o', 'i', 'u']
# index=vowels.index('a')
# print(index)

# vowels = ['a', 'e', 'i', 'o', 'u']
# index = vowels.index('p')
# print("The indes of p:",index)

# alphabets = ['a', 'e', 'i', 'o', 'g', 'l', 'i', 'u']
# index=alphabets.index('e')
# # print(index)
# print("The index of e:",index)
# index = alphabets.index('i', 4)
# print('The indes of i',index)
# index=alphabets.index('i',3,5)
# print("The index of i :",index)

# fruits = ['apple', 'banana', 'cherry']
# fruits.insert(1,'orange')
# print(fruits)

# vowel = ['a', 'e', 'i', 'u']
# vowel.insert(3,'o')
# print('List',vowel)

# prime_numbers = [2, 3, 5, 7]
# prime_numbers.insert(4,11)
# print('List',prime_numbers)

# mixed_list = [{1, 2}, [5, 6, 7]]
# number_tuple = (3, 4)
# mixed_list.insert(1,number_tuple)
# print(mixed_list)
# prime_numbers = [2, 3, 5, 7]
# removed_element=prime_numbers.pop(2)
# print('Removed Element:',removed_element)
# print('Updated list:',prime_numbers)

# languages = ['Python', 'Java', 'C++', 'French', 'C']
# return_value=languages.pop(3)
# print("Return Values: ",return_value)
# print(languages)

languages = ['Python', 'Java', 'C++', 'Ruby', 'C']
# print("When index is not passed")
# print('Return value:',languages.pop())
# print(languages)
# print('\n when -1 is passed:')
# print('return values:',languages.pop(-1))
# print(languages)
# print('\n when -3 is passed:')
# print('Return vale:',languages.pop(-3))
# print("Updated values:",languages)

# prime_numbers = [2, 3, 5, 7, 9, 11]
# prime_numbers.remove(9)
# print('Updated List:',prime_numbers)

# animals list
# animals = ['cat', 'dog', 'rabbit', 'guinea pig']
# animals.remove('rabbit')
# print('Updated animals: ',animals)

# animals = ['cat', 'dog', 'dog', 'guinea pig', 'dog']
# animals.remove('dog')
# print('updated animals list:',animals)

# animals = ['cat', 'dog', 'rabbit', 'guinea pig']
# animals.remove('fish')
# print("Updated animals list:",animals)

# inputList = ['TutorialsPoint', 'Python', 'Codes', 'hello', 'everyone']
# del inputList[2]
# print(inputList)

# prime_numbers = [2, 3, 5, 7]
# prime_numbers.reverse()
# print('Reverserd List:',prime_numbers)

# systems = ['Windows', 'macOS', 'Linux']
# print('Original List',systems)
# systems.reverse()
# print('Updated List:',systems)

# systems = ['Windows', 'macOS', 'Linux']
# print('Original List:', systems)
# reversed_list=systems[::-1]
# print(reversed_list)

# prime_numbers = [11, 3, 7, 5, 2]
# prime_numbers.sort()
# print(prime_numbers)

# vowels = ['e', 'a', 'u', 'o', 'i']
# vowels.sort()
# print('Sorted list',vowels)

# vowels list
# vowels = ['e', 'a', 'u', 'o', 'i']
# vowels.sort(reverse=True)
# print("Sorted list in descending",vowels)

# my_tuple = ()
# print(my_tuple)

# my_tuple = (1, 2, 3)
# print(my_tuple)

# my_tuple = (1, "Hello", 3.4)
# print(my_tuple)

# my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
# print(my_tuple)

# var1 = ("Hello") # string
# var2 = ("Hello",) # tuple
# print(type(var1))
# print(type(var2))

# var3 = "hello",
# print(type(var3))

# tuple1 = (101, 102, 103) + (104, 105, 106)
# print(tuple1)

# T = ('red', 'green', 'blue') + (1, 2, 3)
# print(T)

# tuple1 = (101, 102, 103) + (104, 105, 106)
# T = ('red', 'green', 'blue') + (1, 2, 3)
# print(tuple1+T)

# T = ('red',)*3
# print(T)

# T = ('red', 'Green') * 3
# print(T)
# print('red' in T)

# tuple1 = (12, 14, 16, 18, 20, 23, 27, 39, 40)
# print(len(tuple1))

# T = ('red', 'green', 'blue')
# T[0] = 'black'

# tuple1 = (0, 1, 2, 3)
# tuple1[0]=4
# print(tuple1)

# T = ('red', 'green', 'blue', 'yellow', 'black')
# print(T[0])

# T = ('red', 'green', 'blue', 'yellow', 'black')
# print(T[-1])
# print(T[-2])

# tup1 = ('physics', 'chemistry', 1997, 2000);
# tup2 = (1, 2, 3, 4, 5, 6, 7 );
# print ("tup1[0]: ", tup1[0])
# print ("tup2[1:5]: ", tup2[1:5])

# T = ('a', 'b', 'c', 'd', 'e', 'f')
# print(T[2:5])
# print(T[3:-1])

# tuple1 = (0 ,1, 2, 3)
# # print(tuple1[1:])
# # print(tuple1[::-1])
# print(tuple1[2:4])

# T = ('red', 'green', 'blue')
# del T

# tuple3 = ( 0, 1)
# del tuple3
# print(tuple3)

# t = ('red', 'green', 'blue')
# del (t[0])
# print(t)

# a = ['red', 'green', 'blue']
# del a[0]
# print(a)

# T = ('red', 'green', 'blue', 'cyan')
# (a,b,c,d)=T
# print(a,b,c,d)

# a = (1,2,1,3,1,3,1,2,1,4,1,5,1,5)
# print(a.count(1))
# print(a.index(5))
# abc=("Yusuf","Amit","Pooja","raj", "Pritesh","Priya","Yusuf")
# print(abc.count('Yusuf'))
# print(abc.index('Yusuf'))
# print(abc.index('Yusuf',1,7))
# print(abc.index('Yusuf',-7,-1))
# print(abc.index('Yusuf',-1,-7))

# a = (1,2,1,3,1,3,1,2,1,4,1,5,1,5)
# print(a.count(1))
# print(a.index(5))
# abc=("Yusuf","Amit","Pooja","raj", "Pritesh","Priya","Yusuf")
# print(abc.count('Yusuf'))
# print(abc.index('Yusuf'))
# print(abc.index('Yusuf',1,7))
# print(abc.index("Yusuf",-7,-1))
# print(abc.index('Yusuf',-1,-7))

# a_list = [1,2,3,4,5]
# b_tuple = tuple(a_list)
# print(type(b_tuple))

# tup2 = ("Yusuf","yusuf")
# print(max(tup2))
# print(min(tup2))

# tuple_ = (5, 2, 24, 3, 1, 6, 7)
# sorted_=tuple(sorted(tuple_))
# print('Sorted tupel',sorted_)
# sorted_=tuple(sorted(tuple_,reverse=True))
# print("Sorted tuple:",sorted_)

# a = (1,2,3,4,5)
# print(len(a))

# a_list = [1,2,3,4,5]
# print(a_list)
# print(type(a_list))
# b_tuple=tuple(a_list)
# print(b_tuple)
# print(type(b_tuple))

# a="Yusuf"
# a=tuple(a)
# print(a)
# print(type(a))
# a=list(a)
# print(a)
# print(type(a))

# x = ("apple", "banana", "cherry")
# y=list(x)
# y[1]='kiwi'
# x=tuple(y)
# print(x)

# thistuple = ("apple", "banana", "cherry")
# y=list(thistuple)
# y.append('orange')
# thistuple=('apple','banana','cherry')
# y=('orange',)
# thistuple+=y
# print(thistuple)

# tuple1 = (5, 3, 2, 8, 4, 4, 6, 2)
# list=list(tuple1)
# list[2]=63
# tuple1=tuple(list)
# print(tuple1)

# tuple1 = (5, 3, 2, 8, 4, 4, 6, 2)
# list1 = list(tuple1)
# list1.remove(2)
# tuple1=tuple(list1)
# print(tuple1)

# x = {1,2.3, "py", (1,2,3)}
# print(x)

# x = set("python")
# print('by set constructor',x)

# y={'y', 'n', 't', 'p', 'h', 'o'}
# print("Curly {} brackets",y)

# Days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
# print(Days)
# print(type(Days))

# student_id = {112, 114, 116, 118, 115}
# print("Student Id",student_id)

# vowel_letters = {'a', 'e', 'i', 'o', 'u'}
# print('Volwel Letters',vowel_letters)
# mixed_set = {'Hello', 101, -2, 'Bye'}
# print('Set of mixed data types:', mixed_set)

# student_id = set[112, 114, 116, 118, 115]
# print('Student Id:',student_id)

# vowel_letters = set['a', 'e', 'i', 'o', 'u']
# print('Vowel Lettes:',vowel_letters)

# mixed_set = set['Hello', 101, -2, 'Bye']
# print('Set of mixed data types :',mixed_set)
# Days = set(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
# print(Days)
# print(type(Days))

# x = set("python","vish")
# print(x)

# y={'y', 'n', 't', 'p', 'h', 'o'}
# print('curly {}brackets: ', y)

# empty_set = set()
# empty_dictionary = {}
# print('Data type of empty_set:', type(empty_set))
# print('Data type of empty_dictionary', type(empty_dictionary))

# for element in set:
#  print(element)

# x={'p','h','t','n','o'}
# for y in x:
#     print(y)

# fruits = {"Apple", "Peach", "Mango"}
# for fruit in fruits:
#     print(fruit)

# numbers = {2, 4, 6, 6, 2, 8}
# print(numbers)

# numbers = {21, 34, 54, 12}
# print('iniial set:',numbers)
# numbers.add(32)
# print('Updated set',numbers)

# companies = {'Lacoste', 'Ralph Lauren'}
# tech_companies = ['apple', 'google', 'apple']
# companies.update(tech_companies)
# print(companies)

# y={2,3,4,5}
# print('Set',y)

x={'Python','Java','PHP','Angular'}
# print('set x',x)
# x.remove('Java')
# print('Set x after remove',x)
# x.discard('PHP')
# print('Set x after discard:',x)

# x={1,2,"py"}
# print('print set x',x)
# z=x.pop()
# print('print first element of set',z)
# x.clear()
# print('Print set after clear:',x)

# languages = {'Python', 'Java', 'English'}
# languages.remove('English')
# print(languages)

# numbers = {2, 3, 4, 5}
# numbers.discard(3)
# print(numbers)

# A = {'a', 'b', 'c', 'd'}
# removed_item=A.pop()
# print(removed_item)

# primeNumbers = {2, 3, 5, 7}
# primeNumbers.clear()
# print(primeNumbers)

# A = {1, 3, 5,2}
# B = {0, 2, 4,1}
# print('union using |',A|B)
# print('Union using union:',A.union(B))

# first set
# A = {1, 3, 5}
# # second set
# B = {1, 2, 3}
# print('intersection using &: ',A&B)
# print('intersection usig intersection()',A.intersection(B))

# A = {2, 3, 5}
# # second set
# B = {1, 2, 6}
# print('Differce using&',A-B)
# print("Difference using difference(),",A.difference(B))

# # first set
# A = {2, 3, 5}
# # second set
# B = {1, 2, 6}
# # print('using ^:',A^B)
# print('using symmetric_differce()',A.symmetric_difference(B))

# x={1,2}
# y={3,4}
# z=x.isdisjoint(y)
# print(z)

# x={1,2}
# y={1,2,3,4}
# z=x.issubset(y)
# print(z)

x = {'a','b','c'}
y = {'a','b','c'}
# print('Set x',x)
# print('Set y:',y)
# print('set x==y',x==y)
# print('Set x!=y',x!=y)

# x = {1,2}
# y = {1,2,3,4}
# print('Set x',x)
# prints\('Set y',y)
# print('Set x',x<=y)
# print('set x<y',x<y)

# x = {1,2,3,4}
# y = {1,2,3}
# # print('Set x',x)
# # print('Set y',y)
# print('Set x superset y:',x>=y)
# print('Set x proper superset y:',x>y)
# print('intersection x& y',x&y)
# print("Union of x | y",x|y)
# print('Differce of of x-y:',x-y)
# print("symmetric diffrecence of x &y",x^y)

# x={20,1,2,3,4,10}
# z=x.copy()
# print('Copy set x to set z',z)
# print('Print lenth of set z:',len(z))
# print('Print min of set z:',min(z))
# print('Print max of set ',max(z))
# print('Print sum of set z',sum(z))
# print(sorted(z))
# print(sorted(z,reverse=True))
# print(all(z))
# print(any(z))
# print(5 in x)
# print(5 not in x)
# b = False
# print(type(b))

# a=10
# b=20
# print(a>b)
# print(type(a>b))

# vowels = ('a', 'e', 'i', 'o', 'u')
# fSet=frozenset(vowels)
# # print('The frozen set is ',fSet)
# # print('The empty frozen set is:',frozenset())
# fSet.add('v')
# print(fSet)

# person = {"name": "John", "age": 23, "sex": "male"}
# fSet=frozenset(person)
# print('The frozen set is',fSet)

# A = frozenset([1, 2, 3, 4])
# B = frozenset([3, 4, 5, 6])
# C=A.copy()
# print(C)
# print(A.union(B))
# # print(A.intersection(B))
# print(A.difference(B))
# print(A.symmetric_difference(B))

# A = frozenset([1, 2, 3, 4])
# B = frozenset([3, 4, 5, 6])
# C = frozenset([5, 6])
# # print(A.isdisjoint(C))
# # print(C.issubset(B))
# print(B.issubset(C))

# D = {'name': 'Bob',
#  'age': 25,
#  'job': 'Dev',
#  'city': 'New York',
#  'email': 'bob@web.com'}
# D1 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})

# L = [('name', 'Bob'),
#  ('age', 25),
#  ('job', 'Dev')]
#
# D=dict(L)
# print(D)

# T = (['name', 'Bob'],
#  ['age', 25],
#  ['job', 'Dev'])
#
# D=dict(T)
# print(D)

# keys = ['name', 'age', 'job']
# values = ['Bob', 25, 'Dev']
# D=dict(zip(keys,values))
# print(D)

# keys = ['a', 'b', 'c']
# defaultValue=0
# D=dict.fromkeys(keys,defaultValue)
# print(D)

# D = {'name': 'Bob',
#  'age': 25,
#  'name': 'Jane'}
# print(D)

# D = {(2,2): 25,
#  True: 'a',
#  'name': 'Bob'}
# print(D)

# D = {[2,2]: 25,
#  'name': 'Bob'}
#
# D = {'a':[1,2,3],
#  'b':{1,2,3}}
#
# D = {'a':[1,2],
#  'b':[1,2],
#  'c':[1,2]}

# D = {'name': 'Bob',
#  'age': 25,
#  'job': 'Dev'}
# # print(D['name'])
# print(D.get('name'))

# Dict = {'Dict1': {1: 'Geeks'},
#  'Dict2': {'Name': 'For'}}
# print(Dict['Dict2']['Name'])
# print(Dict['Dict1'])
# print(Dict['Dict1'][1])

# D = {'name': 'Bob',
#  'age': 25,
#  'job': 'Dev'}
# D['name']='Sam'
# print(D)

D = {'name': 'Bob',
 'age': 25,
 'job': 'Dev'}

# D = {'name': 'Bob',
#  'age': 25,
#  'job': 'Dev'}
# D['city']='NEw york'
# print(D)

# Dict = {}
# print("Empty Dictionary: ")
# print(Dict)
# #
# Dict[0] = 'Geeks'
# Dict[2] = 'For'
# Dict[3] = 1
# print("\nDictionary after adding 3 elements: ")
# print(Dict)
#
# Dict['Value_set'] = 2, 3, 4
# print("\nDictionary after adding 3 elements: ")
# print(Dict)
#
# # Updating existing Key's Value
# Dict[2] = 'Welcome'
# print("\nUpdated key value: ")
# print(Dict)

# D1 = {'name': 'Bob',
#  'age': 25,
#  'job': 'Dev'}
# D2 = {'age': 30,
#  'city': 'New York',
#  'email': 'bob@web.com'}
#
# D1.update(D2)
# print(D1)

# D = {'name': 'Bob',
#  'age': 25,
#  'job': 'Dev'}
# x=D.pop('age')
# print(D)
# print(x)

# D = {'name': 'Bob',
#  'age': 25,
#  'job': 'Dev'}
#
# del D['age']
# print(D)

# D = {'name': 'Bob',
#  'age': 25,
#  'job': 'Dev'}
# x=D.popitem()
# print(D)
# print(x)

# D = {'name': 'Bob',
#  'age': 25,
#  'job': 'Dev'}
#
# D.clear()
# print(D)

# D = {'name': 'Bob',
#  'age': 25,
#  'job': 'Dev'}
#
# print(list(D.keys()))
# print(list(D.values()))
# print(list(D.items()))

# D = {'name': 'Bob',
#  'age': 25,
#  'job': 'Dev'}
#
# for x in D:
#  print(x)


# D = {'name': 'Bob',
#  'age': 25,
#  'job': 'Dev'}
#
# for x in D:
#  print(D[x])

# D = {'name': 'Bob',
#  'age': 25,
#  'job': 'Dev'}
# print('name' in D)
# print('salary' in D)

# D = {'name': 'Bob',
#  'age': 25,
#  'job': 'Dev'}
#
# print('Bob' in D.values())
# print('Sam' in D.values())

# D = {'name': 'Bob',
#  'age': 25,
#  'job': 'Dev'}
# print(len(D))

# dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}
# # copy() method
# dict2 = dict1.copy()
# print(dict2)
# dict1.clear()
# print(dict1)
# print(dict2.get(1))
# print(dict2.items())
# print(dict2.keys())
# print(dict2.pop(4))
# print(print(dict2))
# dict2.popitem()
# print(dict2)
# dict2.update({3:"C++"})
# print(dict2.values())

# dict = {1: "Ayan", 2: "Bunny", 3: "Ram", 4: "Bheem"}
# print(len(dict))

# dict = {1: "Ayan", 2: "Bunny", 3: "Ram", 4: "Bheem"}
# print(any({'':'','':'',3:''}))

# dict = {1: "Ayan", 2: "Bunny", 3: "Ram", 4: "Bheem"}
# print(all({1:'',2:'','':''}))
# print(all({1:'',2:'',3:'',4:''}))

# dict = {7: "Ayan", 5: "Bunny", 8: "Ram", 1: "Bheem"}
# print(sorted(dict))

# dict = {1: "Microsoft", 2: "Google", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}
# dict.clear()
# print(dict)

# dict = {1: "Microsoft", 2: "Google", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}
# dict_demo=dict.copy()
# print(dict_demo)

# dict = {1: "Microsoft", 2: "Google", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}
# dict_demo=dict.copy()
# x=dict_demo.pop(1)
# print(x)

# dict = {1: "Microsoft", 2: "Google", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}
# print(dict.keys())

# dict = {1: "Microsoft", 2: "Google", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}
# print(dict.items())

# dict = {1: "Microsoft", 2: "Google", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}
# print(dict.get(3))

# dict = {1: "Microsoft", 2: "Google", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}
# dict.update({3:'TCS'})
# print(dict)

# dict = {1: "Microsoft", 2: "Google", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}
# print(dict.values())

# kitchen='Apple'
# # if kitchen=='Apple':
# #  print("Hai hai apply")
# # print('Thik hai')
#
# # if (kitchen == "Mango"):
# #  print("Ha Hai Mango")
# # print("Thik hai ")
#
# if (kitchen == "Mango"):
#  print("Ha Hai Apple")

# num = 5
# if (num < 10):
#  print('Num is smaller than 10')

# a=7
# b=0
# if (a>b):
#  print('a is greater than b')

# num=-7
# if num !=0:
#  if num>0:
#   print("NUmber is positive")
#  else:
#   print("Number is negative")
# else:
#  print("Number is zero")

# i=10
# if i==10:
#  print('i si smaller than 15')
# if i<12:
#  print("I is smaller than 12 too")
# else:
#  print("I is greater than 15")

# num=5
# if num<4:
#  print('Num is smaller than 5')
#  if num<4:
#   print("Num is less than 4 ")
#   if num <5:
#    print("Number is less than 5")
#   else:
#    print("Num is less than 5")
#  else:
#   print("Num is less than 5")
# else:
#  print("Num is not less than 8")
#
# my_marks=90
# if my_marks<35:
#  print("Sorry ! You failed the exam")
# elif my_marks>60 and my_marks>100:
#  print('Passed in First class')
# else:
#  print('Passed in first class with distinction')

# a=10
# if (a):
#  print('The given value of a')
#  print(a)

# currentYear=int(input("Enter the Year: "))
# month=int(input("Enter the month: "))
# if currentYear%4==0:
#
#  print("Leap Year")
#  if month==1 or month==3 or month==5 or month==7 or month==8 or month==12:
#   print("There are 31 days in this months")
#  elif month==4 or month==6 or month==9 or month==11:
#   print("There are 30 days in this month")
#  elif month==2:
#   print("There are 29 days in this month")
# elif (currentYear%4)!=0:
#  print('Non Leap Year')
#  if month==1 or month==3 or month==5 or month==7 or month==8 or month==12:
#   print("There are 31 days in this months")
#  elif month==4 or month==6 or month==9 or month==11:
#   print("There are 30 dayes in this month")
#  elif month==2:
#   print("There are 28 dayes this month")
#  else:
#   print("Invalid Month")
# else:
#  print("Invalid Year")

# kichen='Apple'
# while 'Apple' in kichen:
#  print("Apple")
# kichen='Apple'
# while 'Apple' in kichen:
#  print("Apple")
#  kichen='Banana'

# count=0
# while count<3:
#  count=count+1
#  print('Credence')

# kichen='Apple'
# while 'Apple' in kichen:
#  print(kichen)
#  kichen='Banana'
# else:
#  print("Not found in kitchen")

# count=0
# while count<3:
#  print('Credece')
#  count=count+1
# else:
#  print("Not found")

count=0
# while count<3:
#  print("Credence")
#  count+=1
# else:
#  print("Not found")

# while count<3:
#  count+=1
#  print("Apple")
# kitchen ='Apple'
# count=0
# while count<3:
#  count+=1
#  print("Apple")

# i=0
# # while i<6:
# #  print(i)
# #  i+=1

# i = 1
# while i <= 10:
#  print(i)
#  i = i+1

# i=1
# while i<6:
#  print(i)
#  i+=1

# i=2
# while i<6:
#  print(i)
#  i=+1

# count=0
# while count<5:
#  count+=1
#  print("Hello Geek", "Entered", count, "thtimes")

# count=0
# while count<3:
#  count+=1
#  print("Hello Geek")

# count = 0
# while count<3:
#  count+=1
#  print("hello Geek")
# else:
#  print("In Else Block")

# age=32
# while age>18:
#  print("You can vote")

# i=1
# n=5
# while i<=n:
#  print(i)
#  i+=1


# total=0
# number=int(input("Enter a number: "))
# while number!=0:
#  total+=number
#  number=int(input("Enter a number: "))
#
# print('Total= ',total)

# count = 0
# while (count < 5): count += 1; print("Hello Geek")

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#  print(x)

# for x in 'banana':
#  print(x)

# a=5
# for i in range(0,a):
#  print(i)

# values = range(4)
# for i in values:
#  print(i)

# for x in range(6):
#  print(x)

# numbers=range(2,5)
# print(list(numbers))

# numbers=range(-2,4)
# print(list(numbers))

# numbers = range(4, 2)
# print(list(numbers))

# numbers=range(2,10,3)
# print(list(numbers))

# numbers=range(2,10,3)
# print(list(numbers))

# for x in range(6):
#  print(x)

# number=range(2,5)
# print(list(number))

# number=range(-2,4)
# print(number)

# numbers = range(4, 2)
# print(list(numbers))

# numbers=range(2,10,3)
# print(numbers)

# numbers = range(4, -1, -1)
# print(list(numbers))
# numbers = range(0, 5, 1)
# print(list(numbers))

# for x in range(2,30,3):
#  print(x)

# digits = [0, 1, 5]
# for i in digits:
#  print(i)
# else:
#  print("No item lelt.")

# for x in range(6):
#  print(x)
# else:
#  print("Finally finished!")

# fruits = ['banana', 'apple', 'mango']
# for index in range(len(fruits)):
#  print("Current fruit: ",fruits[index])
# print("Good bye!")
# nums=(1,2,3,4)
# sum_nums=0
# for num in nums:
#  sum_nums=sum_nums+num
# print(f'Sum of number is {sum_nums}')

# for i in range(4):
#  print(i)
list1 =[1,2,3,4,5]
# for item in list1:
#  print('For loop')

# item=1
# while item in list1:
#  print('While loop')

# item=1
# while item in list1:
#  print('While loop')
#  item+=1

# for i in range(11):
#  print(i)

# i = 0
# while i <= 10:
#  print(i)
#  i+=1

# for i in range(1, 5):
#  for j in range(i):
#   print(i, end=' ')
#  print()

list1 =[1,2,3,4,5]
# for item in list1:
#  print("for loop")

# item=1
# while item in list1:
#  print("while")

# item=1
# while item in list1:
#  print("While loop")
#  item+=item

# for i in range(11):
#  print(i)


# i=0
# while i<=10:
#  print(i)
#  i+=1

# for i in range(1,5):
#  for j in range(i):
#   print(i,end=' ')
#  print()

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
# for x in adj:
#  for y in fruits:
#   print(x,y)




