import numpy as np

filePath = r'FileDirectory/August16Extraction'
file = open(filePath, 'r')
var = file.readlines()
print(var)
newList = list(map(lambda x: int(x.strip()), var))
print(newList)

myNumpyArray=np.array([newList],dtype=int)
print(myNumpyArray)
print(f'The highest marks is {np.max(myNumpyArray)}')
print(f'The lowest marks is {np.min(myNumpyArray)}')
print(f'The accumulated marks is {np.add.reduce(myNumpyArray)}')
print(f'The average marks is {np.mean(myNumpyArray)}')
print(f'The median marks is {np.median(myNumpyArray)}')
print(f'The standard deviation is {np.std(myNumpyArray)}')
print(f'The Q1 is {np.percentile(myNumpyArray,25)}')