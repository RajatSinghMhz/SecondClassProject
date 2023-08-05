# #WAP to check if a given number is multiple of 3 or not, if multiple of 3 print Fizz
# checkMul=int(input("Please enter a number"))
# if checkMul%3==0:
#     print("Fizz")
# elif checkMul==0 or checkMul%3!=0:
#     print("Not a multiple of 3")
#
# print("_______________")
#
# #WAP above for 5
# checkMuls=int(input("Please enter a number"))
# if checkMuls%5==0:
#     print("Buzz")
# elif checkMul==0 or checkMul%3!=0:
#     print("Not a multiple of 3")
#
# print("_______________")
#
# #WAP to print multiple of 3 and 5
# checkMulz=int(input("Please enter a number"))
# if checkMulz%3==0 and checkMulz%5==0:
#     print("FizzBuzz")
# elif checkMulz%3==0:
#     print("Fizz")
# elif checkMulz%5==0:
#     print("Buzz")
# else:
#     print(checkMulz)
#
# print("_______________")

#WAP to ask user with a amount and display how many Bills of each notes
#Examples 1560=1000+500+50+10

Money=int(input("Enter the amount: "))
Bill1000=None
Bill500=None
Bill100=None
BIll50=None
Bill10=None
Bill5=None
Bill1=None
rem=None
if(Money>0):
    Bill1000=Money//1000
    rem=Money-Bill1000*1000

    Bill500=int(rem/500)
    rem=rem-500*Bill500

    Bill100=int(rem/100)
    rem=rem-100*Bill100

    Bill50 = int(rem/50)
    rem = rem-Bill50*50

    Bill10 = int(rem/10)
    rem = rem-10*Bill10

    Bill5 = int(rem / 5)
    rem = rem - 5 * Bill5

    Bill1=rem
else:
    print("Invalid amount")

print(f'No of bills of {Money} is: \n {Bill1000}-1000\n {Bill500}-500 \n {Bill100}-100 \n {Bill50}-50 \n {Bill10}-10 \n {Bill5}-5 \n {Bill1}-1')

print("_________________________________")
userInput = int(input("Enter the currency "))

thousand = None
fiveHundred = None
hundred = None
fifty = None
twenty = None
ten = None
five = None
1560
if userInput == 0:
    print("Please Enter Amount ")

if userInput >= 1000:
    thousand = userInput // 1000
    userInput = userInput - thousand * 1000;

if userInput >= 500:
    fiveHundred = userInput // 500
    userInput = userInput - fiveHundred * 500

if userInput >= 100:
    hundred = userInput // 100
    userInput = userInput - hundred * 100

if userInput >= 50:
    fifty = userInput // 50
    userInput = userInput - fifty * 50
if userInput >=20:
    twenty = userInput // 20
    userInput = userInput - twenty * 20

if userInput >=10:
    ten = userInput // 10
    userInput = userInput - ten * 10

if userInput >=5:
    five = userInput // 5
    userInput = userInput  - five * five


print(f'The currency has {thousand} thousand , {fiveHundred} fiveHundred, {hundred} hundred , {fifty} fifty , {twenty} twenty, {ten} ten, {five} five')