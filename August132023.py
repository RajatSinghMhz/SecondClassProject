import numpy as np

#Pseudorandom array
pseudoRandom=np.random.randint(1,100,(5,2))
print(pseudoRandom)
print("====================================")

#Generation of random Array based on seeds/ so as long as seed is same, random value generated is same.
rng=np.random.default_rng(seed=101)
randomArray=rng.integers(1,100,size=(3,5),dtype=int,endpoint=True)
print(randomArray)
print("====================================")

seedRandomArray=np.random.default_rng(seed=1012)
randomArray=seedRandomArray.integers(1,10,size=(3,6),dtype=int,endpoint=True)
print(randomArray)
print(randomArray[0][3])
print("====================================")

x1=np.array([1.1,1.2,1.3,1.34,5.0])
x2=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x1)
print(x2)

#Shape
print(f'Shape of x1 is {x1.shape}')
print(f'Shape of x2 is {x2.shape}')
#size
print(f'Size of x1 is {x1.size}')
print(f'Size of x2 is {x2.size}')
#dimension
print(f'Dimension of x1 is {x1.ndim}')
print(f'Dimension of x2 is {x2.ndim}')
#Bytes
print(f'Byte of x1 is {x1.nbytes}')
print(f'Byte of x2 is {x2.nbytes}')
#datatype
print(f'Datatype of x1 is {x1.dtype}')
print(f'Datatype of x2 is {x2.dtype}')

print("====================================")

multidimensionalArray=np.array([
    [12,1,2,3],
    [4,5,6,7],
    [8,9,10,11]
])
print(multidimensionalArray[:2:,0:3:])
print("====================================")
print(multidimensionalArray[1:2:,0:1:])
print("====================================")
print(multidimensionalArray[::-1,::-1])
print("====================================")

#View vs copy// changing data from sub to main // so use copy to not affect main array data
x1=np.array([
    [12,1,2,3],
    [4,5,6,7],
    [8,9,10,11]
])
# xcopy=x1[:2,:2]
xsubcopy=x1[:2,:2].copy()
# print(xcopy)
print(xsubcopy)
# xcopy[0,0]=500
xsubcopy[0,0]=500
# print(xcopy)
print(xsubcopy)
print(x1)

#arange// reshape
x2=np.arange(1,10)
print(x2)
x3=x2.reshape(3,3)
print(x3)

#axis changing (1D to 2D)
x4=np.array([1,2,3])
x5=x4[np.newaxis,:]
x6=x4[:,np.newaxis]
print(x4)
print(x4.ndim)
print(x5)
print(x5.ndim)
print(x6)
print(x6.ndim)
