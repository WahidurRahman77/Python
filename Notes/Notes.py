#one line comment

'''
multiple
line
comment
'''
print (123)
print ("\"Wahidur Rahman\"")

#Variables and Data Types
name = ("Wahidur Rahman")
age = 18
print ("Our new student name is " + name)
print(name + " is " , age , " years old.")
print("At the age of ", age , "he learned python.")
print(name + " lives in canad")

# Basic Numerical Operations
a = 20
b= 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)


#Getting User Input
name = input("Enter your name: ")
print(name)

#Type Casting
num1 = int(input("Enter your first number: "))
num2 = input("Enter your second number: ")
sum = num1 + int(num2)
print(sum)

#Math related Library functions

from math import *
print(max(10, 20))
print(min(10, 20))
print(abs(-4))
print(pow(2, 3))
print(sqrt(25))
print(round(3.8))
print(floor(3.8))
print(ceil(3.8))

#Formatted String | Type function
num = 3.8
print(type(num))

num1 = 2
num2 = 5
print(f"{num1} + {num2} = {num1 + num2}")

print("Wahidur Rahman", end=" ")
print("123456789")

#if, else statement
if (3 > 4):
    print(3)
else:
    print(4)

#elif
n =5
if(n>3):
    print(3)
elif(n>4):
    print(4)
else:
    print(5)

#Ternary Operator
num1 = 2
num2 = 4
print(num1 if num1<num2 else num2)

#Logical operator
if(num1<num2 and num2< 5):
    print(num1)
elif(num1<num2 or num2>2):
    print(num2)

#List
list = ["c", "c++", "java", "python", "c#", "c++", "java", "python"]
print(list)
print(list[0])
print(list[2:])
print(list[-1])

print("python" in list)

print("nodejs" not in list)

print(len(list))

list.append("TOC")
list.insert(2, "OS")
list.remove("java")

list.sort()
print (list)
list.reverse()
list.pop()
print(list)
list2 = list.copy()
list.clear()
print(list2)
print(list2.index("java"))
print(list2.count("python"))

# Range function
num = list(range(5, 10))
print(num)

num = list(range(5, 20, 2))
print(num)

#for Loop
num = {10, 30, 50, 5, 3}
sum = 0
for x in num:
    print(x)
    sum = sum + x
print("sum =",sum)

n = int(input("Enter row number:"))
for i in range(1, n + 1):
    print((n - i) * " ", i * "*")

# Guessing Game
import random
guessnumber = int(input("Guess your number(1-5):"))
randomnumber = random.randint(1, 5)
if guessnumber == randomnumber:
    print("you won!")
else:
    print("you lost!", "random number was", randomnumber)

#List as input from user
n = input("Enter a text of numbers:")
list = n.split()
sum = 0
for num in list:
    sum = sum + int(num)
print(sum)

#Matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
]
print(matrix)

#Dictionaries
studentId = {
    "101" : "Wahidur Rahman",
    "102" : "nafiz",
    "103" : "Nola saikat"
}
print(studentId["102"])
print(studentId.get("106", "Not a valid key"))

#Tuples
students = (
    "Wahidur Rahman", "Nola saikat", "nafiz"
)
print(students)

student = (
    ("Wahidur Rahman", 21, 2.0),
    ("Nola saikat", 21, 3.50),
    ("nafiz", 21, 4.00),
)
print(student)
print(student[1:])

#Set
num = {1,3,4,5,5}
print(num)

num2 = set([4,5,6,7])
print(num2)
num2.add(8)
num2.remove(5)
print(num2)
print(5 in num2)

num1 = {1,3,4,5}
num2 = set([4,5,6,7])
print(num1 | num2)
print(num1 & num2)
print(num1 - num2)

# Stack And Queue
books= []
books.append("Learn C")
books.append("Learn C++")
books.append("Learn Java")
print(books)

books.pop()
print(books)
print("Now the top book is-", books[-1])

books.pop()
print("Now the top book is-", books[-1])

books.pop()
if not books:
    print("Nothing to see here.")

from collections import deque
bank = deque(["Nola saikat", "BBB", "BBC"])
bank.popleft()
print(bank)

if not bank:
    print("Nothing to see here.")

#Function
def add (a, b):
    return a + b

x = int(input())
y = int(input())
print(add(x, y))

#xxargs and xxxargs
def student(*details):
    print (details)

student(101, "Nola")
student(101, "Nola", 3.75)

def student(**details):
    print (details)
    print(details["name"])

student(ID=101, name="Nola", CGPA=3.75)

#Lambda Functions
print((lambda a,b : a*a + 2*a*b + b*b) (2,3))

#map and filter function

def square(a):
    return a*a
num = [1,2,3,4,5,6,7,8,9]
result = list(map(square, num))
print(result)

result = list(filter(lambda x: x%2==0, num))
print(result)

#List Comprehensions
result = [x*x for x in num]
print(result)
result =[x for x in num if x%2==0]
print(result)

# Zip Function
roll = [104, 105, 106, 107, 108, 109, 110]
name = ["nola", "nafiz", "BBB", "BBC", "monkey", "dart irfan", "rivu"]
print(list(zip(roll, name)))

# Recursion
def fact (n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)
print(fact(5))

#Reading a file
file = open("student.txt", "r")

print(file.readable())
text = file.read()
print(text)
size = len(text)
print(size)
file.close()

file = open("student.txt", "r") #list
text = file.readlines()
print(text)
file.close()

file = open("student.txt", "r") #index print
text = file.readlines()[0]
print(text)
file.close()

file = open("student.txt", "r")
for line in file:
    print(line)
file.close()

#writing in a file
file = open("student.txt", "a")
file.write("\nNoman - Topper")
file.close()


#Exception Handling (part-1)
try:
    list = [10, 0, 30]
    result = list[0] / list[1]
    print(result)
    print("Done")
except ZeroDivisionError:
    print("Division by zero is not possible")

try:
    list = [10, 0, 30]
    result = list[0] / list[3]
    print(result)
    print("Done")
except ZeroDivisionError:
    print("Division by zero is not possible")
finally:
    print("successful")


try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print(result)
except (ValueError,ZeroDivisionError):
    print("you have given incorrect input")
finally:
    print("Thanks!!!")


def voter(age):
    if age < 18:
        raise ValueError("Invalid age")
    return "You are allowed to vote"

try:

    print(voter(17))
except ValueError as e:
    print(e)


#Swapping
a = 10
b = 20
a, b = b, a
print("a =", a)
print("b =", b)
