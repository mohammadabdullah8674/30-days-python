# -------------   >>>>>>    Level 1    >>>>>>>>>>

# Que 1 : Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables_exercise.py

# Que 2 : Write a python comment saying 'Day 2: 30 Days of python programming'

#       "Day 2 : 30 Days of python programming"

# Que 3 : Declare a first name variable and assign a value to it
first_name = "Mohammad"
# Que 4 : Declare a last name variable and assign a value to it
last_name = "Abdullah"
# Que 5 : Declare a full name variable and assign a value to it
full_name = first_name + " " + last_name
# Que 6 : Declare a country variable and assign a value to it
country = "India"
# Que 7 : Declare a city variable and assign a value to it
city = "Azamgarh"
# Que 8 : Declare an age variable and assign a value to it
age = 21
# Que 9 : Declare a year variable and assign a value to it
year = 2022
# Que 10 : Declare a variable is_married and assign a value to it
is_married = False
# Que 11 : Declare a variable is_true and assign a value to it
is_true = True
# Que 12 : Declare a variable is_light_on and assign a value to it
is_light_on = True
# Que 13 : Declare multiple variable on one line
father_name, mother_name, brother_name = "Zubair Ahmad", "Noorana Khatoon", "Mohammad Shafiullah Zubair" 

# print(full_name, country, city, age, year, is_married, father_name, mother_name, brother_name)

# -------------   >>>>>>    Level 2    >>>>>>>>>>

# Que 1 : Check the data type of all your variables using type() built-in function
# print(type(full_name))
# print(type(country))
# print(type(city))
# print(type(age))
# print(type(is_married))
# print(type(is_light_on))
# print(type(father_name))
# Que 2 : Using the len() built-in function, find the length of your first name
length_first_name = len(first_name)
# print(length_first_name)
# Que 3 : Compare the length of your first name and your last name
length_last_name = len(last_name)
# print(length_last_name)
# print(length_first_name - length_last_name)
# Que 4 : Declare 5 as num_one and 4 as num_two
num_one, num_two = 5, 4
# i) Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
# ii) Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
# iii) Multiply num_two and num_one and assign the value to a variable product 
product = num_one * num_two
# iv) Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
# v) Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
# vi) Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
# vii) Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
# print(total, diff, product, division, remainder, exp, floor_division)
# Que 5 : The radius of a circle is 30 meters
radius = 30
pi = 3.14159
#  i) Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = pi * radius ** 2
print(area_of_circle)
#  ii) Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * pi * radius
print(circum_of_circle)
#  iii) Take radius as user input and calculate the area.
# input_radius = float(input("Enter the value of radius : "))
# area_of_circle = pi * input_radius ** 2
# print("Area of circle is :",area_of_circle)

# Que 6 : Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Enter your first name : ")
last_name = input("Enter your last name : ")
age = input("Enter your age : ")
country = input("Enter your country name : ")
greeting = "Hello, Mr. " + first_name + ' ' + last_name + ". You are " + age + " years old and you are living in " + country
print(greeting)

# Que 7 : Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

# Here is a list of the Python keywords.  Enter any keyword to get more help.

# False               class               from                or
# None                continue            global              pass
# True                def                 if                  raise
# and                 del                 import              return
# as                  elif                in                  try
# assert              else                is                  while
# async               except              lambda              with
# await               finally             nonlocal            yield
# break               for                 not