'''
x="Python is pOwerful"
#Upper lower
print(x.capitalize())
print(x.upper())
print(x.lower())
print(x.title())
print(x.swapcase())

#length
print(len(x))

#Fill
print(x.zfill(28))

#Count characters
print(x.count("Python"))

#Know about indexing
print(x.find("o"))
print(x.find("is"))        #reads first position of is i.e. of "i"
print(x.find("isly"))      #no position found then -1
print(x[8])

y="Python is powerful , python is fast"
print(y[5])                #Positive Indexing
print(y[-7])               #negative indexing
print(y.find("python"))
'''
z=input("Enter a string")
k=len(z)
print(f' The first character is {z[0]}')
print(f' The last character is {z[k-1]}')
print(f'The middle character is{z[(k-1)//2]}')

#Math.ceil used to use upper value