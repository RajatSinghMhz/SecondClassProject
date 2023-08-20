myFilePath = r'FileDirectory/August062023'
myFilePath2 = r'FileDirectory/August062023Generated'
file = open(myFilePath, 'r')

fileContent = file.read()
print(fileContent)
file.close()

##Writing to a file
file = open(myFilePath, 'w')
file.write("Hello Hello")
file.close()

##Appending to a file
file = open(myFilePath2, 'a')
file.write("\n This is appended file")
file.close()

#WAP to ask user id and password and store in a file
userName=input("Enter your username: ")
userPass=input("Enter your password: ")
savingFilePath=r'FileDirectory/August062023'

savingFile=open(savingFilePath,'w')
savingFile.write(userName)
savingFile.write('\n')
savingFile.write(userPass)
savingFile.close()

#WAP to read same userId and Password in variable
readingFile=open(savingFilePath,'r')
inputUserData=readingFile.readlines()
userNameFromFile=inputUserData[0].strip()
userPassFromFile=inputUserData[1].strip()
print(f'Username is {userPassFromFile}')
print(f'Password is {userPassFromFile}')
readingFile.close()


