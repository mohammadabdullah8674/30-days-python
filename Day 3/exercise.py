# --------->>>>>   Day 3 -- Exercise ---- >>>>>
from math import sqrt
# Que 1: Declare your age as integer variable
age = 21
# Que 2: Declare your height as a float variable
my_height = 5.4
# Que 3: Declare a variable that store a complex number
complex_number = 1 + 2j
# Que 4: Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
    # Enter base: 20
    # Enter height: 10
    # The area of the triangle is 100
# base = int(input("Enter base of a triangle : "))
# height = int(input("Enter height of a triangle : "))
# area_of_triangle = 0.5 * base * height
# print(area_of_triangle)
# Que 5: Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
    # Enter side a: 5
    # Enter side b: 4
    # Enter side c: 3
    # The perimeter of the triangle is 12
# side_a = int(input("Enter first side of triangle : "))
# side_b = int(input("Enter second side of triangle : "))
# side_c = int(input("Enter third side of triangle : "))
# perimeter = side_a + side_b + side_c
# print(perimeter)
# Que 6: Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width)) 
# length = float(input("Enter length of Rectangle : "))
# width = float(input("Enter width of Rectangle : "))
# area_of_rectangle = length * width
# perimeter_rectangle = 2 * (length + width)
# print(area_of_rectangle, perimeter_rectangle)
# Que 7: Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
# radius = float(input("Enter radius of Circle : "))
# area_of_circle = 3.14 * radius * radius
# circumference = 2 * 3.14 * radius
# print(area_of_circle, circumference)
# Que 8: Calculate the slope, x-intercept and y-intercept of y = 2x -2
# Que 9: Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1 = 2
x2 = 6
y1 = 2
y2 = 10
slope = (y2 - y1) / (x2 - x1)
Euc_distance = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
print("Slope is : ", slope)
print("Euclidian Distance is : ", Euc_distance)
# Que 10: Compare the slopes in tasks 8 and 9.
# Que 11: Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# x = int(input("Enter value of x : "))
# y = (x ** 2) + (6 * x) + 9
# print("Solution of quadratic is : ", y)
# Que 12: Find the length of 'python' and 'dragon' and make a falsy comparison statement.
py = "python"
dr = "dragon"
print(len(py) != len(dr))  # False --- both lengths are equal
# Que 13: Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("on" in py and "on" in dr)
# Que 14: I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon."
print("jargon" in sentence)
# Que 15: There is no 'on' in both dragon and python
print("on" not in py and dr)
# Que 16: Find the length of the text python and convert the value to float and convert it to string
str_length = len(py)
print(str_length)
print(float(str_length))
print(str(float(str_length)))
# Que 17: Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num1 = 252224
num2 = 2523
print(num1%2 is 0)
print(num2%2 is 0)
# Que 18: Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7//3 is int(2.7))  # True
print(7//3 == int(2.7))  # True
# Que 19: Check if type of '10' is equal to type of 10
print(type('10') is type(10))  #False
print(type('10') == type(10))  #False
# Que 20: Check if int('9.8') is equal to 10
# n = int('9.8')
# print(n == 10)
# print(n is 10)    # ----> gives error b/c int()-->give an int value but here is 9.8 which is float
# to correct :
n = int(float("9.8"))
print(n)  # 9
print(n == 10)  # False
print(n is 10)  # False
# Que 21: Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
    # Enter hours: 40
    # Enter rate per hour: 28
    # Your weekly earning is 1120
# hours = int(input("Enter hours : "))
# rate_per_hour = int(input("Enter rate per hours : "))
# weekly_earning = hours * rate_per_hour
# print("Your weekly is ", weekly_earning)
# Que 22: Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
    # Enter number of years you have lived: 100
    # You have lived for 3153600000 seconds.
# years = int(input("Enter number of years you have lived : "))
# years_in_second = years * 365 * 24 * 60 * 60
# print(f"You have lived for {years_in_second} seconds.")
# Que 23: Write a Python script that displays the following table
            # 1 1 1 1 1
            # 2 1 2 4 8
            # 3 1 3 9 27
            # 4 1 4 16 64
            # 5 1 5 25 125

values = range(6)
for i in values:
    if i is 0:
        continue
    print(i, "1", i, i*i, i*i*i )
