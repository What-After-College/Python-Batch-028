import numpy as np


# creating numpy arrays

# arr = np.array([1,2,3,4,5])

# print(arr)

# print(type(arr))

# arr = np.array([[1,2,3],[4,5,6]])

# lis = [[1,2,3],[4,5,6]]

# arr = np.array(lis)

# print(arr[1][1])
# print(arr.ndim)



# lis = [[1,2,3],[4,5,6]]

# arr = np.array(lis, dtype=float)

# print(type(arr[1][1]))

# print(arr.dtype)



# lis = [[1,2.2,3],[4,5,6]]

# arr = np.array(lis)

# print(type(arr[1][1]))

# print(arr.dtype)

# print(arr.shape)

# print(arr.itemsize)



# array of particular type --------------------------

# arr = np.zeros((4,4))

# arr = np.zeros((4,4), dtype=int)


# arr = np.ones((4,4))


# arr = np.ones((4,4), dtype=int)


# arr = np.arange(1, 10, 2)


# arr = np.eye(5)

# arr = np.eye(5, 6)


# arr = np.full((3,4), 9)


# arr = np.random.random((4,5))  # it will return us a matrix of random number between 0 to 1


# arr = np.linspace(5,50,10)


# arr = np.linspace(5,50,5)

# print(np.round(arr, 1))


# print(np.ceil(arr))


# print(arr)



#using mathmatical fuction and value through numpy

# print(np.pi)

# print(np.sin(np.pi/2))  # angle should be in radian


# print(np.cos(np.pi/2))  # angle should be in radian


# arr = np.arange(1,10).reshape(3,3)


# print(arr)


# print(arr[1:3,1:3])


# array manipulation------------------------------


a = np.arange(1,10).reshape(3,3)


b = np.arange(11,20).reshape(3,3)

print(a)
# print(b)

# print(a+b)
# print(np.add(a,b))


# print(b-a)
# print(np.subtract(b,a))

# print(a*b)
# print(np.multiply(a,b))

# print(a/b)
# print(np.divide(a,b))


# print(np.dot(a,b))
# print(a.dot(b))


# print(a.T)


# print(a.ravel())

# print(np.sqrt(a))


