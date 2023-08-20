import numpy as np
zeroes=np.zeros(20,dtype=int)
print(zeroes)
print("====================================")
ones=np.ones(13,dtype=int)
print(ones)
print("====================================")
customArray=np.full(10,5,dtype=float)
print(customArray)
print("====================================")
customArray=np.full(10,'*')
print(customArray)
print("====================================")

#multidimension array
myArray=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
myMultiArray=np.array(myArray)
print(myMultiArray)
print("====================================")
customArray=np.zeros((3,5),dtype=int)
print(customArray)
print("====================================")
customArray=np.ones((2,3),dtype=float)
print(customArray)
print("====================================")
customArray=np.full((5,10),"Ram")
print(customArray)
print("====================================")

#Evenlyspaced array
evenlySpace=np.linspace(1, 15, num=27, endpoint=True, retstep=True, dtype=float,axis=0)
print(evenlySpace)
print("====================================")

#Pseudorandom array
pseudoRandom=np.random.randint(1,100,(5,2))
print(pseudoRandom)
print("====================================")

#Identity array
identityArray=np.eye(3,dtype=int)
print(identityArray)
print("====================================")

#Homogeneous property of numpy Array
myArray=[1,2,3,4,5]
newArray=np.array(myArray)
print(myArray[0])
print(newArray[0])
myArray[0]=25.8
newArray[0]=25.8
print(myArray[0])
print(newArray[0])
print(newArray[0:2])
print("====================================")

#Reversing numpy Array
print(newArray[::-1])

#Extraction
extractionArray=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(extractionArray[2][1])
print(extractionArray[-1][-3])

