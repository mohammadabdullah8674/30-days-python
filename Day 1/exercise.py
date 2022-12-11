# Level 2
from cmath import sqrt
from platform import python_version

# question 1
print(python_version)

# question 2
num1 = 4
num2 = 3

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
modulus = num1 % num2
floor_divison = num1 // num2
exponent = num1 ** num2

print(addition, subtraction, multiplication, division,modulus,floor_divison, exponent)

# question 3
my_name = "Abdullah"
family_name = {
    "Father" : "Zubair Ahmad",
    "Mother" : "Noorana Khatoon",
    "Brother" : ["Shafiullah", "Aebadullah"],
    "Sister" : ["Iffat", "Sadaf"],
}
my_country = "India"
challenge = "I am enjoying 30 days of python"

print(my_name)
print(family_name)
print(my_country)
print(challenge)

# question 4

print(type(10))  #int
print(type(9.8))  # float 
print(type(3.14))  #float
print(type(4-4j))  #complex
print(type(['Asabeneh', 'Python', 'Finland']))   #list
print(type(my_name))  #str
print(type(family_name)) #dictionary
print(type(my_country)) #str


# Level 3
# Question 1 : Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.

integer_number = 5
float_number = 5.55
complex_number = 5+5j
str1 = "This is string"
bool = False
my_list = ["This", "is", "list", "25", 2.55]
my_tuple = ("This", "is", "tuple")  # just like list but it is immutable
my_set = {2, 5, 6}  #set in Python stores only unique items.
my_dict = {
    "first_Name" : "Mohd",
    "last_Name" : "Abdullah",
}

# Question 2 : Find an Euclidian distance between (2, 3) and (10, 8)
x1 = 2
x2 = 3
y1 = 10
y2 = 9

euclidian_distance =sqrt(((x2 - x1)**2) + ((y2 -y1)**2))
print("This is answer : ", euclidian_distance)
print(sqrt(100))