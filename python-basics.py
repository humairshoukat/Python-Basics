# Python Programming
# Humair Shoukat (BSCS - NUML)

# Python-Fundamentals
# Operators, Variables, Data Types, Strings, Precedence, Loops, List. Tuples, Dictionary, Classes, Formatting

# Variables in Python
# Can't use name of keywords as variable names
# Keywords: False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, 
# for, from, global, if, import, in, is, lambda, not, or, pass, raise, return, try, while, with, yield
x = 'Hello World!'
my_age = 20

print(x)
print(my_age)

# Check type of a variable  
print(type(my_age))
print(type(x))
my_age = 20.0
print(type(my_age))

my_age = 1.0 + -0.5j
print(type(my_age))
print(my_age.real)
print(my_age.imag)

# Use the 'is' check to see if the type of a variable matches what we are comparing with
print(type(my_age) is bool)
print(type(my_age) is complex)

# Type Cating in Python
age = 19.5
print(type(age))

age = int(age)
print(age)
print(type(age))

age = "19.5"
# Can't do age + 10
# Solution: Typcast to float then calculate
age = float(age)
age += 10
print(age)

# Can't do this
# age = "a19.5"
# age = float(age)

# Arithmetics & Comparisons in Python
print(5+2)
print(5-2)
print(5*10)
print(5/2)
print(5//2)
print(5**2)

print(8>9)
print(12>10 and 11>10)
a = 10
print(a==10)

# Lists only have same values
list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]
print(list1 == list2)
print(list1 is list2)

# Lists have same value, and also refer to the same list
list1 = [1,2,3,4,5]
list2 = list1
print(list1 == list2)
print(list1 is list2)


# Strings in Python
# -----------------
var = "Hello World!"

# Find length of the variable (number of characters)
length = len(var)
print(length)

# Replace a particular word with another, in the string
var = var.replace("World", "Dunyia")
print(var)

print(var[0])
print(var[1])
print(var[2])
print(var[3])
print(var[4])

# Extract the word "Hello"
temp = var[0:5]
print(temp)

# Extract the word "World!"
temp = var[6:]
print(temp)

# Take the Even Position Occurences of the string
temp = var[::2]
print(temp)

# Printing
print(var, "\n")
print(var, "We're at NUST!\n")
print(var, 20, False, "\n")

age = 20
print(var+"We're at NUST!\n")
print(var+" my age is: " + str(age) + "\n")

first_name = "Humair"
last_name = "Shoukat"
full_name = first_name + " " + last_name
print(full_name)

# Lists in Python
list1 = [1,2,3,4,5]
print(list1)

#List Slicing (Same as string slicing)
print(list1[2:5])
print(list1[::2])

list2 = [1, "1", "one", 1.0]
print(list2)

list3 = [1,[2], [3,4,5],[[6,7], [8,9]]]
print(list3[3])

#Converting a string into a list of characters
word = "Hello World"
print(list(word))

#Using the .append(val) function to add to the end
list4 = []
list4.append("A")
list4.append("B")
print(list4)

#Using the .insert(index,val) to insert at a particular index
list4.insert(1,"C")
print(list4)

#Delete Values

#1) Delete Particular Index
del list4[0]
print(list4)

#2) Delete First Occurence of a Particular Value
list4.remove("C")
print(list4)

list5 = [4,9,1,2,8,7,3]
list5.sort()
print(list5)
list5.sort(reverse=True)
print(list5)

# Tuples in Python
#immutable, used for unpacking
coord = (5,10)
x, y= coord
print("X: ", x)
print("Y: ", y)

# Dictionaries in Python
dic={ "Pakistan" : 40, 
      "India"    : 145, 
      "China"    : 500, 
      "Mexico"   : "None"
    }
print(dic)

print(dic["Pakistan"])
dic["Pakistan"] = 38
print(dic)

#Print the Key and Value Pair
for i, j in dic.items():
    print(i, " : ", j)

#Add a new key value pair
dic["Turkey"] = 90
print(dic)

#remove an exisiting Key Value Pair
dic.pop("Mexico")
print(dic)

#Nested Dictionary
Family = {
    
        "child1" : {
            "name":"Humair", 
            "age":22
        }, 
    
        "child2" : {
            "name":"Ali", 
            "age": 19
        }
}

print("Family: ", Family)

# Statements in Python
# if-else, if-else-if
age = input("Enter your age: ")
age = int(age)

if (age<18):
    print("You're too young for a license")
elif (age >= 18 and age <=60):
    print("You're eligible for a license")
else:
    print("You're too old for a license")

if (True and False):
    print("1")
else:
    print("2")

if (False or True):
    print("1")
else:
    print("2")


# Loops in Python

#basic for loop
for i in range(0, 10):
    print(i)

#iterating lists
list1 = range(0,5)
list2 = list("Hello")
for x in list1:
    print(x)
print("\n\n")
for y in list2:
    print(y)

#iterate through dictionary items
countries = dic.keys()
countries = list(countries) 
for c in countries:
    print(c*3)
print("\n")

#iterate through a list by indexes, and raise it to the power of its value
list3 = [1,2,3,4,5]
for i in range(0,len(list3)):
    list3[i] = list3[i] ** list3[i]
    print(list3[i])

#iterate dictionaries

for key,value in dic.items():
    print(key, " -> ", value)


#basic while loop
i = 0
while(i<10):
    print(i)
    i+=1

count = 0
times = 10
while (count<times):
    print(count+1, ") Pakistan Zindabad")
    count = count+1

age = 30
commission = 0
while (age>18):
    commission += 100
    age-= 1
print(commission)


#list comprehension
list1 = []
for i in range(0, 5):
    list1.append(i)
    
list1

list1 = [i+3 for i in range(0,5)]
list1

# Functions in Python

#Pass a name to a function to print a Hi statement with that name
def say_hi_to(name):
    print("Hi", name)

#Say Hi to Usman
say_hi_to("Usman")
  
#Given an age, check if that age is eligible for a license, print relevant message
def eligibility(age):
    if (age<18):
        print("You're too young for a license")
    elif (age >= 18 and age <=60):
        print("You're eligible for a license")
    else:
        print("You're too old for a license")

#Check if a person aged 17 is eligible for license
eligibility(17)

#Print a given list/array in reverse
def reverse_print(list1):
    length = len(list1)
    length-=1
    while (length >= 0):
        print(list1[length])
        length -= 1

#Print the given list in reverse
reverse_print([1,2,3,4,5])

#Get details of a customer, and return as a tuple to unpack
def get_details():
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    #convert into a tuple
    dets = (name, age)
    return dets

#Get Details of a new employee
n1, a1 = get_details()
print("\nYour details are as follows:")
print(n1)
print(a1)

#check if a particular value exists in a list
def exists(list1, num):
    for val in list1:
        if (val == num):
            return True
    return False

#Check if the number '9' exists in the given list
ex = exists([9,8,4,4], 9)
ex

#return the square of a number
def get_square(val):
    return val*val

#Find the square of 9
sq = get_square(9)
sq


# Classes in Python (Object Oriented Programming)

#Basic Class Outline

class Dog:
    
    #constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.name, "has been made")
        print(self.name, "is", age, "years old")
    
    def bark():
        print("Woof Woof")
        
    def getname(self):
        return self.name
    
    def getage(self):
        return self.age
    
    def setage(self, val):
        self.age = val
    
    def setname(self, n):
        self.name = n
        
    def agenextyear(self, age):
        return age+1
    
d1 = Dog("Dog1",13)
d2 = Dog("Dog2", 9)


#Composition
class Student:
    
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        
    def getscore(self):
        return self.score
    
class Course:
    
    def __init__(self, name, maxstd):
        self.name = name; 
        self.maxstd = maxstd
        self.students = []
        
    def add_student(self, student):
        if len(self.students) < self.maxstd:
            self.students.append(student)
            print("Enrolled Successfully")
            return True
        print("Seats are full")
        return False
    
    
    def avgscore(self):
        
        val = 0
        for student in self.students:
            val += student.getscore()
            
        print("Average score:", val/len(self.students))
        return val/len(self.students)
        
        
S1 = Student("Humair", 21, 80)
S2 = Student("Mashal", 21, 96)
S3 = Student("Ali", 19, 75)

BigData = Course("Big Data Analytics", 5)
BigData.add_student(S1)
BigData.add_student(S2)
BigData.add_student(S3)
BigData.avgscore()


#Inheritance

class Pet:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def details(self):
        print(f"I am {self.name} and I am {self.age} years old")
        
class Cat(Pet):
    def speak(self):
        print("Meow")
    
    def all_details(self):
        print("I am a Catto")
        self.details()
        
class Dog(Pet):
    def speak(self):
        print("Bark")
    
P1 = Pet("Tony", 18)
P1.details()


print("\n\n")


C1 = Cat("Tom", 30)
C1.details()
C1.all_details()
C1.speak()


## Libraries / Frameworks to learn in Python

# Data Processing, Cleaning
# NumPy, Pandas

# Data Visualization
# Matplotlib, Seaborn

# Data Scraping & Automation
# BeautifulSoup, Scrapy, Selenium

# Machine Learning
# Scikit-learn, TensorFlow, Keras, Pytorch, OpenCV, NLTK

# Backend Development
# Django, Flask, FastAPI

# Game Development
# Pygame