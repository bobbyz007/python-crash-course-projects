import numpy as np

# Create ndarray
data = np.array([[1.5, -0.1, 3], [0, -3, 6.5]])

print(data.shape)
print(data.dtype)

print(np.zeros((3, 6)))
print()

# Arithmetic operations
print(data * 10)
print(data + data)
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
print(arr2 > arr)
print()

arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# if you omit later indices, the returned object will be a lower dimensional ndarray consisting of all the data along the higher dimensions.
arr3d[0] = 42
print(arr3d)

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[:2, 1:])
print(arr2d[1, :2])
print()

# Boolean indexing
names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe"])
data = np.array([[4, 7], [0, 2], [-5, 6], [0, 0], [1, 2],[-12, -4], [3, 4]])
print(data[names == "Bob", 1])
print(data[names == "Bob", 1:])
print(data[~(names == "Bob")])
print(data[names != "Bob"])
print(data[(names == "Bob") | (names == "Will")])
copied = data[names == "Bob"]
copied *= 1000
print(copied)
print(data)
data[data<0] = 0 # Set all of the negative values in data to 0
print(data)
print()

# Fancy indexing is a term adopted by NumPy to describe indexing using integer arrays
arr = np.arange(32).reshape((8, 4))
print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])
print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])
arr[[1, 5, 7, 2], [0, 3, 1, 2]] = 0 # unlike slicing ,copies data to array
print(f"\n{arr}\n")

# transposing
arr = np.arange(15).reshape(3, 5)
print(arr.T)
arr = np.array([[0, 1, 0], [1, 2, -2], [6, 3, 2], [-1, 0, -1], [1, 0, 1]])
print(np.dot(arr.T, arr))
print(arr.T @ arr)
print()

# pseudorandom number generation
print(np.random.standard_normal(size=(4, 4)))
rng = np.random.default_rng(seed=12345)
print(rng.standard_normal((2, 3)))
print()

# Universal Functions: Fast Element-Wise Array Functions
arr = np.arange(10)
print(np.sqrt(arr)) # unary ufunc
x = rng.standard_normal(8)
y = rng.standard_normal(8)
print(np.maximum(x, y)) # binary ufunc
print()

# Array oriented programming
x = np.linspace(0, 1, 5)
y = np.linspace(0, 1, 3)
X, Y = np.meshgrid(x,y)  # 返回3*5矩阵， X的行重复x， Y的列重复y
print('x:',x)
print('Y:',y)
print('X:',X)
print('Y:',Y)
print()

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
result = np.where(cond, xarr, yarr) # conditional logic
print(result)

arr = rng.standard_normal((4, 4))
print(arr)
print(np.where(arr > 0, 2, -2))
print(np.where(arr > 0, 2, arr))

