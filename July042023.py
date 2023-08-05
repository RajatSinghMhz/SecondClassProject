'''
#Data_type
a=2
b=3
c="2"
d="3"
e=True
f=False
g=None
print(f'a+b is {a+b}')
print(f'c+d is {c+d}')
print(f'e+f is {e+f}')
print(f'g is {g}')

#Type_Casting
name=input("Enter your name ")
age=input("Enter your age ")
add_value1=input("Enter first value")
add_value2=int(input("Enter first value"))
print(f'Your name is {name}\n You are {age} years old.')
print(f'Sum of add_value1 and add_value2 is {int(add_value1)+add_value2}')


#For Simple Interest
principle=int(input("Input Principle"))
time=int(input("Input time in years"))
rate=int(input("Input Rate %"))
print(f'The interest of principle Rs. {principle}, rate{rate}% and time{time} years is Rs.{(principle*time*rate)/100}')

#For area of circle
radius=input("Enter the radius of a circle in mm ")
area=(int(radius)**2)*3.14
print(f'The area of a circle of radius {radius}mm is {area} mm2')
'''

#String
text="Ram is a boy"
text1="Ram is a boy's name"
text2='''Ram
            is
                a
                    boy's
                        name'''
print(text)
print(text1)
print(text2)

