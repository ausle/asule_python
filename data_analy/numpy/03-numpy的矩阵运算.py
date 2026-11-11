
import numpy as np

'''
广播机制，为了让不同维度的数据进行运算。

1、不同维度的数组，什么情况可以广播，什么情况不可以广播？
记住一个结论：
得到两个数组的形状后，从右往左进行判断，每一对的维度要么相等，或者其中一个是1。如果都不满足，则不能进行广播。

'''


array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([[1], [2], [3], [4]])

print(array1.shape)
print(array2.shape)
print(array1*array2)
'''
(1, 4)
(4, 1)
从右往左判断，4和1，其中有一个维度为1。1和4，其中有一个维度为1。所以可以进行广播。
得到的结果：
[[ 1  2  3  4]
 [ 2  4  6  8]
 [ 3  6  9 12]
 [ 4  8 12 16]]
'''



# 一种特殊情况：一维数组和二维数组进行计算
# 一维数组，形状是(4,)，注意不是一行四列。会给左侧加上缺少的维度，最后的形状是（1,4）
# 所以array3*array4：这种情况也是可以广播的。
array3 = np.array([1, 2, 3, 4])
array4 = np.array([[1], [2], [3], [4]])
print(array3.shape)
print(array4.shape)
print(array3*array4)


# 典型错误的情况  （1,3）和（4,2）无法进行广播
array5 = np.array([1, 2, 3, 4])
array6 = np.array([[1,1], [2,2], [3,3], [4,4]])
print(array5.shape)
print(array6.shape)
print(array5*array6)