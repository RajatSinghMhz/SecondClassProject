import re
text='''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

logisparktech.com

321-555-4321
123.444.1234
456*697*5566
800-123-234
900-234-123
700-123-234


192.168.1.91

Mr Rohit
Mr. Raunak
Ms. Anushka
Mrs. Nisha
Mr. T


cat
mat
pat
bat
'''
sentence='Start a sentence and bring it to Start'
print("=========================================")


pattern=re.compile(r'def')
# pattern khojna paryo, compile garda
matches=pattern.finditer(text)
# finding match using finding it in iterate 'text file'
for match in matches:
    print(match)
print("=========================================")


pattern=re.compile(r'.')
# finds all characters except new line
matches=pattern.finditer(text)
# finding match using finding it in iterate 'text file'
for match in matches:
    print(match)
print("=========================================")


pattern=re.compile(r'\.')
# finds only . character
matches=pattern.finditer(text)
# finding match using finding it in iterate 'text file'
for match in matches:
    print(match)
print("=========================================")


pattern=re.compile(r'logisparktech\.com')
# finds only . character
matches=pattern.finditer(text)
# finding match using finding it in iterate 'text file'
for match in matches:
    print(match)
print("=========================================")


pattern=re.compile(r'\bHa')
# finds "Ha" character with empty strings like \n or " "
matches=pattern.finditer(text)
# finding match using finding it in iterate 'text file'
for match in matches:
    print(match)
print("=========================================")


pattern=re.compile(r'\BHa\b')
# finds "Ha" character with empty strings like \n or " "
matches=pattern.finditer(text)
for match in matches:
    print(match)
print("=========================================")


pattern=re.compile(r'\bHa\B')
matches=pattern.finditer(text)
for match in matches:
    print(match)
print("=========================================")


pattern=re.compile(r'\BHa\b')
matches=pattern.finditer(text)
for match in matches:
    print(match)
print("=========================================")


#Matching from first
pattern=re.compile(r'^Start')
matches=pattern.finditer(sentence)
for match in matches:
    print(match)
print("=========================================")


#Matching from end
pattern=re.compile(r'Start$')
matches=pattern.finditer(sentence)
for match in matches:
    print(match)
print("=========================================")


#Matching phone number
pattern=re.compile(r'\d\d\d\.\d\d\d\.\d\d\d\d')
# Note \. then only . match, /// . used all characters except \n matched
matches=pattern.finditer(text)
for match in matches:
    print(match)
print("=========================================")


#Matching Two pattern
pattern=re.compile(r'\d\d\d[*.-]\d\d\d[*.-]\d\d\d\d')
matches=pattern.finditer(text)
for match in matches:
    print(match)
print("=========================================")


#Matching specific pattern
pattern=re.compile(r'[89]00-\d\d\d-\d\d\d')
matches=pattern.finditer(text)
for match in matches:
    print(match)
print("=========================================")


#Matching specific pattern
pattern=re.compile(r'[a-zA-Z0-9]')
matches=pattern.finditer(text)
for match in matches:
    print(match)
print("=========================================")


#Matching specific pattern
pattern=re.compile(r'[^a-zA-Z0-9]')
matches=pattern.finditer(text)
for match in matches:
    print(match)
print("=========================================")


#Matching actual names
pattern=re.compile(r'(Mr|Mrs|Ms)\.?\s[A-Z]\w*')
matches=pattern.finditer(text)
for match in matches:
    print(match)

