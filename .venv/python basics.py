# python for non-programmers by Nick Walter
# first line of code
print("Hello World")

# variables
account = 100
print(account)

# variables can be +ve or -ve. It can be Integers (Whole number) or Floats (with decimal)
print(3 * 6)
print(account + 2)

# variables can be strings,and it can be written in double or single quote
color = "white"
print(color)

# variables in strings (f string)
name = "Mohanish"
surname = "Shah"
age = 34
print(f"my name is {name} {surname} and my age is {age}")

# Variables in Boolean (True or False) and if statement
health_is_good = True
if health_is_good:
    print("Healthy")
else:
    print("Not Healthy")

# comparison
age = 34
if age >= 18:
    print("Adult")
else:
    print("Child")

# modulo
number = 11
remainder = number % 2
if remainder == 1:
    print("Odd")
else:
    print("Even")

# random
import random

print(random.randint(1, 10))
print(random.random())

# combination of random & if else
import random

number = random.randint(1, 3)
if number == 1:
    print("Yes")
if number == 2:
    print("No")
if number == 3:
    print("Maybe")

# f string with random and if else statement
import random

lucky_number = random.randint(1, 100)
fortune_number = random.randint(1, 3)
fortune_text = ""
if fortune_number == 1:
    fortune_text = "You are good"
if fortune_number == 2:
    fortune_text = "You are bad"
if fortune_number == 3:
    fortune_text = "You are ok"
print(f"Your lucky number is {lucky_number}. {fortune_text}")

# lists (zero based counting means it starts from 0)
passwords = [1, 100.4, "Good", True, 48]
print(passwords[1])

# lists - length
print(len(passwords))
# lists - add
passwords.append("Hello")
print(passwords)
# lists - insert
passwords.insert(2, 150.6)
print(passwords)
# lists - delete
del(passwords[3])
print(passwords)

# for loops
for number in range(5):
    print(number*2)
for number in range(2):
    print("hello")
    print("hi")
# for loops and lists
for pwd in passwords:
    print(pwd)

# dictionaries
name = {"mohanish":34, "shriya":30, "zeeya":7}
print(name)
name["rajeshree"] = 58
print(name)

# sum of all even numbers - total variable -> then for loop -> find even numbers by modulo -> run total in loop -> print
numbers = [35, 46, 48, 84, 71, 79, 102]

total = 0
for number in numbers:

    remainder = number % 2
    if remainder == 0:
        total = total + number

print(total)

# splitting large text and counting total number of words or characters in it
text = """
Did you know that learning Python is one of the easiest ways to learn to code? It’s true. And in this course you can avoid the jargon and make learning how to code a lot more fun. You don’t have to be an expert technician, either. Join instructor Nick Walter and find out what you need to get started now.

In this course, Nick teaches the fundamentals of Python to you: a non-programmer, a user with little to no coding experience. Learn more about what Python is, and what it is and isn’t used for. Explore how Python works with numbers and how you can interact with simple programs such as a simple number-guessing game. Find out how to work with text in Python by building a reusable function to count the words in a block of text. And along the way, tackle quick challenges and other games that allow you to put your new skills to the test.
"""
print(len(text.split()))

# counting the particular word in the phrase
text = """
a b a a b c c a
"""
print(text.split())
# above statement is to split the words in the phrase
word_count = {}

for word in text.split(): # for loop word in text split
    if word in word_count: # giving count 1 to word if it occurred first time in the phrase
        word_count[word] += 1 # adding one more if it occurs more than once
    else:
        word_count[word] = 1
print(word_count)

# functions
def name():
    print("mohanish")
    print("shriya")
name()
# functions with for loop
def name():
    print("mohanish")
    print("shriya")
for x in range(10):
    name()

# parameters
def name(age, name):
    print(f"Hi my name is {name} and my age is {age} years old")
name(34, "mohanish")

# while loop - it combines for loop and if statement means until the time the condition is not fulfilled it will for loop
# while loop is described in another file