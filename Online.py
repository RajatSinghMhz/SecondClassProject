#Online for password account block system
our_password="pass123"
your_answer=None
number_of_try=0
number_of_max_try=8
max_try="Not reached"

while your_answer!=our_password and max_try!="reached":
    if number_of_try<number_of_max_try:
        your_answer=input("Please enter your password :")
        number_of_try=number_of_try+1
    else:
        max_try="reached"
if max_try=="reached":
    print("Account is blocked")
else:
    print("Access granted")

print("_______________________________________________________________")

#By ChatGpt
password = "pass123"
max_attempts = 8
attempts = 0

while attempts < max_attempts:
    user_input = input("Please enter your password: ")
    if user_input == password:
        print("Access granted")
        break
    else:
        attempts += 1

if attempts == max_attempts:
    print("Account is blocked")

print("_______________________________________________________________")

#Example for how for Loops works
meal=["pizza","burger","sphagetti"]
drink=["water","juice","cola"]
dessert=["cake","icecream","chips"]

for m in meal:
    for d in drink:
        for ds in dessert:
            print(f'I will have {m} as a meal and {d} as a drink and {ds} as a dessert')

print("_______________________________________________________________")

#Create encrpt app (much easier using dictionary)
def crypted (sentence):
    encryption=""
    for element in sentence:
        if element in"Aa":
            encryption=encryption+"1"
        elif element in "Bb":
            encryption = encryption + "2"
        elif element in "Cc":
             encryption = encryption + "-"
        elif element in "Dd":
            encryption = encryption + "="
        elif element in "Ee":
            encryption = encryption + ")"
        elif element in "Ff":
            encryption = encryption + "("
        elif element in "Gg":
            encryption = encryption + "*"
        elif element in "Hh":
            encryption = encryption + "&"
        elif element in "Ii":
            encryption = encryption + "^"
        elif element in "Jj":
            encryption = encryption + "%"
        else:
            encryption=encryption+element
    return encryption
result=""
result=crypted(input("Enter the sentence you want to encrypt :"))
print(result)

print("_______________________________________________________________")

