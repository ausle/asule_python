import numpy as np

# 创建0维的ndarray数组
arr0 = np.array(5)
# 一维
arr1 = np.array([1,2,3,4,5])
# 二维，二维数组中的元素，元素个数必须一致
arr2 = np.array([[1,2,3],[4,5,6]])

# 输出数组的维度  numpy of dimensions
print('arr0的维度：',arr0.ndim)
print('arr1的维度：',arr1.ndim)
print('arr2的维度：',arr2.ndim)
#元素数组形状：
print('arr0元素数组形状：',arr0.shape)
print('arr1元素数组形状：',arr1.shape)
print('arr2元素数组形状：',arr2.shape)
#元素数组类型：int64，后面64表示占用的内存空间。
print('arr0元素数组类型：',arr0.dtype)
print('arr1元素数组类型：',arr1.dtype)
print('arr2元素数组类型：',arr2.dtype)

#0维，1维数组，进行元素转置是没有效果的。2维数组元素转置：行变列，列变行。
print('arr2元素转置：',arr2.T)