# num_to_word = {
#     '0': 'zero',
#     '1': 'one',
#     '2': 'two',
#     '3': 'three',
#     '4': 'four',
#     '5': 'five',
#     '6': 'six',
#     '7': 'seven',
#     '8': 'eight',
#     '9': 'nine',
#     '10': 'ten',
#     '20': 'twenty',
#     '30': 'thirty',
#     '40': 'forty',
#     '50': 'fifty',
#     '60': 'sixty',
#     '70': 'seventy',
#     '80': 'eighty',
#     '90': 'ninety',
#     '100': 'hundred',
#     '1000': 'thousand'
# }
# newString = ""
# userNum = input("Enter the amount: ")
# y = len(userNum) - 1
# for x in userNum:
#     digits = str(10 ** (y))
#     if int(digits) <= 1:
#         t = str(int(x) * int(digits))
#         newString = newString + num_to_word[t]
#         y = y - 1
#         continue
#     newString = newString + num_to_word[x] + num_to_word[digits]
#     y = y - 1
# print(newString)

num_to_word = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty',
    '30': 'thirty',
    '40': 'forty',
    '50': 'fifty',
    '60': 'sixty',
    '70': 'seventy',
    '80': 'eighty',
    '90': 'ninety',
    '100': 'hundred',
    '1000': 'thousand',
    '100000':'Lakh'
}

def number_to_words(number):
    if str(number) in num_to_word:
        return num_to_word[str(number)]

    num_str = str(number)
    newString = ""
    y = len(num_str) - 1

    for i in range(len(num_str)):
        x = num_str[i]
        digits = str(10 ** y)

        if y <= 1:
            t = str(int(x) * int(digits))
            newString = newString + num_to_word[t]
            y -= 1
        else:
            newString = newString + num_to_word[x] + num_to_word[digits]
            y -= 1
    return newString
userNum = int(input("Enter the amount: "))
result = number_to_words(userNum)
print("The amount in words:", result)
