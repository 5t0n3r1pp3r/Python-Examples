# ################################## #
'''  4 Levels of Python Examples   '''
# ################################## #

#####################
# Level 1 Beginner  #
#####################
print("Level 1: ")

# These examples cover fundamental concepts in Python programming,
# including outputting text, variables and arithmetic, conditional statements,
# looping, and function definition.
# You can build upon these examples to explore more advanced topics and develop your Python skills further.


# 1. Hello, World!:

print("Hello, World!")

# This is a classic introductory program that prints the message "Hello, World!" to the console. It demonstrates the basic syntax of a Python program and how to use the `print()` function to output text.
print()



# 2. Basic Arithmetic:

x = 5
y = 3
sum = x + y
print("The sum is:", sum)

# In this example, we declare two variables (`x` and `y`), assign them values,
# perform addition using the `+` operator, and store the result in another variable (`sum`).
# Finally, we print the result.
print()



# 3. Conditional Statement:

age = 25
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# This example demonstrates the use of an `if-else` statement.
#  If the condition `age >= 18` is true, it prints "You are an adult.
# " Otherwise, it prints "You are a minor."
print()



#4. Looping:

for i in range(1, 6):
    print("Current number:", i)

# This code utilizes a `for` loop to iterate over a range of numbers from 1 to 5 (inclusive).
# In each iteration, it prints the current number.
print()



# 5. Function Definition:

def greet(name):
    print("Hello,", name)

greet("Alice")

# Here, we define a function called `greet()` that takes a parameter `name`. Inside the function, it prints a personalized greeting. We then call the function and pass the argument "Alice" to greet the specific person.






####################
# Level 2 Advanced #
####################
# These advanced examples cover topics such as file manipulation, exception handling,
# object-oriented programming, regular expressions, and data visualization.
# They provide a glimpse into more advanced concepts and techniques in Python programming.
print("Level 2: ")
print()



# 1.File Manipulation:

# Read contents from a file
with open("data.txt", "r") as file:
    contents = file.read()
    print(contents)

# Write data to a file
data = "This is some data."
with open("data.txt", "w") as file:
    file.write(data)

# This example demonstrates file manipulation in Python.
# The first part reads the contents of a file named "data.txt" and prints it to the console.
# The second part writes a string to a file named "output.txt". The with statement ensures that the file is properly closed after use.
print()



# 2. Exception Handling:

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# In this example, we use a try-except block to handle an exception.
# The code inside the try block attempts to divide 10 by 0, which raises a ZeroDivisionError.
# The except block catches the exception and prints a custom error message.
print()



# 3. Object-Oriented Programming (OOP):

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(5, 3)
print("Area:", rect.area())

# Here, we define a Rectangle class with an __init__ method to initialize the object's attributes (width and height).
# The class also has an area method that calculates the area of the rectangle.
# We create an instance of the Rectangle class and call the area method to compute and print the area.
print()



# 4. Regular Expressions:

import re

text = "The quick brown fox jumps over the lazy dog."
pattern = r"\b\w{5}\b"  # Matches five-letter words

matches = re.findall(pattern, text)
print(matches)

# This example demonstrates the use of regular expressions with the re module.
# We define a pattern that matches five-letter words (\b\w{5}\b).
# Using the re.findall() function, we find all occurrences of the pattern in the given text and print the matches.
print()



# 5. Data Visualization with Matplotlib:

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Plot')
plt.show()

# In this example, we use the Matplotlib library to create a simple line plot.
# We provide two lists of x and y coordinates, and then use plt.plot() to create the plot.
# Additional function calls set the labels for the x and y axes, the plot title, and finally, plt.show() displays the plot.







###################
# Level 3 Expert  #
###################

# These expert-level examples cover topics such as concurrency with threads, decorators,
# context managers, asynchronous programming with async/await, and web scraping with Beautiful Soup.
# They showcase more advanced techniques and functionalities in Python programming.
print("Level 3:")
print()


# 1. Concurrency with Threads:

import threading

def count_up():
    for i in range(5):
        print("Counting up:", i)

def count_down():
    for i in range(5, 0, -1):
        print("Counting down:", i)

thread1 = threading.Thread(target=count_up)
thread2 = threading.Thread(target=count_down)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Done")

# This example demonstrates how to use threads to achieve concurrent execution.
# The count_up() and count_down() functions run in separate threads,
# printing numbers in ascending and descending order, respectively.
# The threading.Thread class is used to create threads, start() method starts the threads,
# and join() method ensures that the main thread waits for the threads to complete before proceeding.
print()



# 2. Decorators:

def uppercase_decorator(func):
    def wrapper():
        result = func().upper()
        return result
    return wrapper

@uppercase_decorator
def greet():
    return "hello"

print(greet())

# Here, we define a decorator called uppercase_decorator, which modifies the output of the decorated function
# by converting it to uppercase. The greet() function is decorated using the @ symbol.
# When greet() is called, it is wrapped by the uppercase_decorator, resulting in the output "HELLO" instead of "hello".
print()


# 3. Context Managers:

class CustomContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")

    def some_operation(self):
        print("Performing some operation")

with CustomContextManager() as manager:
    manager.some_operation()

# In this example, we create a custom context manager by defining a class with __enter__() and __exit__() methods.
# The __enter__() method sets up the context, and the __exit__() method cleans up the resources.
# The some_operation() method represents an operation performed within the context.
# The with statement is used to create an instance of the context manager, and the some_operation() method is called within the context.
print()


# 4. Asynchronous Programming with Async/Await:

import asyncio

async def greet():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

async def main():
    await asyncio.gather(greet(), greet(), greet())

asyncio.run(main())

# This example demonstrates asynchronous programming using async and await keywords.
# The greet() function is an asynchronous function that performs a series of actions with delays.
# The main() function uses asyncio.gather() to concurrently execute multiple instances of greet().
# The asyncio.run() function is used to run the main coroutine and handle the event loop.
print()


# 5. Web Scraping with Beautiful Soup:

import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

title = soup.title.text
print("Title:", title)

links = soup.find_all("a")
for link in links:
    href = link.get("href")
    print("Link:", href)

# This example demonstrates web scraping using the Beautiful Soup library.
# It sends a request to a web page, retrieves the HTML content, and parses it using Beautiful Soup.
# The example extracts the page title and finds all the links (<a> tags) on the page, printing their href attributes.



###################
# Level 4 Master  #
###################

# These master-level examples demonstrate advanced coding techniques,
# including design patterns, functional programming, generators, type hints, annotations, and unit testing.
# They represent top-quality code that adheres to best practices and promotes readability, maintainability, and reliability.
print("Level 4: ")
print()


# 1. Object-Oriented Design Patterns - Singleton:

class Singleton:
    _instance = None

    @staticmethod
    def get_instance():
        if not Singleton._instance:
            Singleton._instance = Singleton()
        return Singleton._instance

    def __init__(self):
        if Singleton._instance:
            raise Exception("Singleton instance already exists.")
        Singleton._instance = self

# Usage:
singleton = Singleton.get_instance()

# This example demonstrates the Singleton design pattern,
# ensuring that only one instance of a class can be created.
# It uses a static method, get_instance(), to provide access to the singleton instance.
# The code also includes a check to prevent the creation of multiple instances.
print()



# 2. Functional Programming - Lambda Functions and Map:

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)

# In this example, a lambda function is used with the map() function to create a new list
# containing the squares of each number in the original list.
# The use of lambda functions and higher-order functions like map() promotes functional programming principles.
print()



# 3. Generator Functions and Yield:

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib))

# This code demonstrates the use of generator functions and the yield keyword
# to create an infinite Fibonacci sequence generator.
# The generator function generates the next Fibonacci number on each iteration using yield,
# allowing efficient memory usage and lazy evaluation.
print()


# 4. Type Hints and Annotations:

from typing import List, Tuple

def multiply(numbers: List[int], factor: int) -> Tuple[int, List[int]]:
    multiplied_nums = [num * factor for num in numbers]
    total_sum = 0
    for num in multiplied_nums:
        total_sum += num
    return total_sum, multiplied_nums

nums = [1, 2, 3, 4, 5]
factor = 2
total_sum, multiplied_nums = multiply(nums, factor)
print("Total:", total_sum)
print("Multiplied Numbers:", multiplied_nums)

# This example showcases the use of type hints and annotations
# to specify the types of function parameters and return values.
# The type hints enhance code clarity and enable static type checking tools to detect potential type-related issues.
print()



# 5. Unit Testing with pytest:

def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 5) == 4
    assert add(0, 0) == 0

if __name__ == "__main__":
    print(test_add())

# This code demonstrates the use of pytest, a popular testing framework, to write unit tests.
# The test_add() function contains a set of assertions that validate the behavior of the add() function.
# Running the script with pytest will automatically detect and execute the tests.
