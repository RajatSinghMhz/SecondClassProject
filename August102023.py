import re
file=open(r'FileDirectory/August102023','r')
fileContents=file.read()
filew=open(r'FileDirectory/August102023Result','w')
pattern=re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')
matches=pattern.finditer(fileContents)
for match in matches:
    filew.write(match.group())
    filew.write("\n")
file.close()
filew.close()

print("=================================================")

#Emergency Number 100, 101, 102, 104
#Pan Number=606651925, 100902834, 39099009090

file=open(r'FileDirectory/August102023','r')
fileContent=file.read()
pattern= re.compile(r'\b10[0124]\b')
patternPAN=re.compile(r'\b[613]\d{8}\b')
matches=pattern.finditer(fileContent)
matchesPAN=patternPAN.finditer(fileContent)
print("Emergency numbers are: ")
for match in matches:
    print(f'{match.group()}')

print("PAN Numbers are ")
for matchPAN in matchesPAN:
    print(f'{matchPAN.group()}')
file.close()

emails='''
PrayushShrestha@gmail.com
rajat.mhz.5@gmail.com
prayush.shrestha@logisparktech.org
prayush-321-shrestha@deerwalk.edu.np
prayush1234@my-work.net
'''
pattern=re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.(com|org|np|edu|net)(\.np)?')
matches=pattern.finditer(emails)
for match in matches:
    print(match)

url='''
https://google.com
http://logisparktech.com
https://logisparktech.com
https://www.ioost.gov
'''
pattern=re.compile(r'http(s)?://(w{3}\.)?[a-zA-Z0-9]+\.(com|gov)')
patterns=re.compile(r'http(s)?://(w{3}\.)?(\w+)(\.\w+)')
#Using groups to extract data to subpattern, it has iterable like in maps
subbedUrl=patterns.sub(r'\3\4',url)
print(subbedUrl)
matches=pattern.finditer(url)
for match in matches:
    print(match)