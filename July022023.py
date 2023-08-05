print("Hello World")
print("Bye World")

# +     addition
# -     subtraction
# *     multiplication
# /     division
# //    integer division
# %     modulus
# **    exponent or power

a = 5
b = 2
print(
    f'Add is {a + b}, subtract is {a - b}, divide is {a / b}, int divide is {a // b}, modulus is {a % b}, exponent is {a ** b}')
print(
    f"Add is {a + b}, subtract is {a - b}, divide is {a / b}, int divide is {a // b}, modulus is {a % b}, exponent is {a ** b}")

print("apple", "banana", "orange", sep=",, ")

# In a python class there are 3 boys and 4 girls, give the total students as output

boys = 3
girls = 4
total_student = boys + girls
print("The total number of students is", total_student)

# in a meeting hall chairs are arranged in rows and columns, if there are three rows and 4 columns, how many chairs
rows = 3
columns = 4
total_chairs = rows * columns
print("The total number of chairs is", total_chairs)

# int rows // then after 10 lines rows=10 can be done in C and Javascript //
# Here in python we do declaration and assignment hand in hand.


boys = 3
girls = 4
total_student = boys + girls
print("The total number of students is", total_student)

print(f'The total number of students is {total_student} out of which {boys} are boys & {girls} are girls.')
print(f'The total number of students is {boys + girls}')

import math

# write a program to swap two numbers
a=2
b=5
print(f'Value of a is {a}, and b is {b}')
c=a
a=b
b=c
print(f'Value of a is {a}, and b is {b}\n')

# WAP to calculate simple interest of money of 3000 at 2% interest for 5 years
p=3000
irate=2
year=5
i=(p*year*irate)/100
print(f'The interest rate of principle {p}, interest rate {irate}% and {year} years is {i}\n')

#WAP to calculate area of cirlce with radius 24
r = 24
area = int(math.pi*(r**2))
print(f'Area of circle of radius {r} is {area}')

#WAP to convert npr 23 into usd
npr = 23
usd = double (npr/133)
print(f'Npr {npr} equivalent is ${usd}')

#WAP to convert usd 23 into npr
ussd = 23
nppr = ussd*133
print(f'USD {ussd} equivalent is Npr{nppr}')


