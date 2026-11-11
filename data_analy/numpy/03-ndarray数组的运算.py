
import numpy as np


# （一）一维数组
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

# 1. 两个数组对应位置运算
print(a + b)   # [11 22 33]
print(a - b)   # [ 9 18 27]
print(a * b)   # [10 40 90]
print(a / b)   # [10. 10. 10.]
print(a ** 2)  # [100 400 900]

# 2. 数组与单个数字运算：数字会作用于每个元素
print(a + 5)   # [15 25 35]
print(a * 2)   # [20 40 60]

# 3. 比较运算：得到布尔数组
print(a > 15)       # [False  True  True]
print(a[a > 15])    # [20 30]，取出满足条件的值

# 4. 统计运算
print(a.sum())      # 60，总和
print(a.mean())     # 20.0，平均值
print(a.max())      # 30，最大值


# （二）二维数组
c = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(c * 2)
# [[ 2  4  6]
#  [ 8 10 12]]

# axis=0：按列求和
print(c.sum(axis=0))  # [5 7 9]：按列求和

# axis=1：按行求和
print(c.sum(axis=1))  # [ 6 15]：按行求和

