# This function adds two numbers together
def add_numbers(num1, num2):
    return num1 + num2
print(add_numbers(20, 20))  


# This function checks if a number is even
def is_even(number):
    return number % 2 == 0
print(is_even(8))  
print(is_even(11)) 


# This function shows a reverse string
def reverse_string(text):
    return text[::-1]
print(reverse_string("hello"))  


# This function counts the vowels
def count_vowels(text):
    vowels = "aeiou"
    return sum(1 for char in text if char in vowels)
print(count_vowels)  


# This function calculates the factorial of a number
def calculate_factorial(n):
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Test the calculate_factorial function
print(calculate_factorial(1))  


# This function adds a simple decorator to another function
def apply_decorator(func):
    def decorator_func(*args, **kwargs):
        return func(*args, **kwargs)
    return decorator_func
apply_decorator
def greet(name):
    print(f"Hello, {name}!")
greet("Mark")  


# This function sorts a list of tuples by age
def sort_by_age(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])
people = [("Alex", 40), ("Mark", 55), ("Charlie", 75)]
print(sort_by_age(people))  


def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged
dict1 = {'a': 4, 'b': 6}
dict2 = {'b': 5, 'c': 7}
print(merge_dicts(dict1, dict2))  


# Object-Oriented Programming for Creating a Car class
# This class represents a car with a make, model, and year
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")

# Testing the Car class
my_car = Car("G-wagon", "Camry", 2024)
my_car.display_info()
