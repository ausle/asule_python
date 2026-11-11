"""
介绍了ndarray的一些特点
numpy数组————ndarray的特点：
    多维性:支持0维、1维、2维以及更高维度数组。
    同质性：所有元素类型必须一致。
    高效性：基于连续空间存储，支持向量化运算。
"""

import numpy as np

#1、创建了一个0维的数组
array0=np.array(5)
# 1维数组
array1=np.array([1,2,3,4,5])
# 2维数组
array2=np.array([[1,2,3],[4,5,6]])
#输出数组的维度
print('array0的维度',array0.ndim)
print('array1的维度',array1.ndim)
print('array2的维度',array2.ndim)


#2、ndarray数组中的元素类型需保持一致
# 如果数组中有不同类型，其他类型会自动转换。
# 比如下面的数组，整数1会自动转换为字符串和浮点数。因为字符串和小数无法转换为整数。
array3=np.array([1,'x1'])
array4=np.array([1,2.5])
print('array3数组',array3)
print('array4数组',array4)


#3、ndarray的一些属性
array5=np.array([[1,2,3],[4,5,6]])
# 数组的行和列的数量，上面这个二维数组的行和列就是2、3。
print('array5数组的形状',array5.shape)

print('array5数组的维度',array5.ndim)
print('array5数组的个数',array5.size)

# int64：int是整数，64代表64位(bit)，1byte=8位，占用8个字节。
print('array5数组的类型',array5.dtype)

# 转置的意思是：行变列，列变行。
print('array5数组的转置',array5.T)


#4、ndarray数组的创建
# (1)基础的创建方法
list0=[1,2,3]

# 强制指定数组的类型为float
carray0=np.array(list0,dtype=np.float64)
# copy一个数组，数组和原始数组是相同的内容，但不是同一个对象。
# 比如你改变数组的值，不会影响原始数组。
carray1=np.copy(carray0)
print('carray0数组的类型',carray0.dtype)
print('carray1数组的类型',carray1.dtype)
carray1[0]=9
print('carray0数组和carray1数组的值',carray0,carray1)


#（2）预定义形状来创建数组
# 创建一个行为2，列为3的形状的二维数组，值指定为0。
carray2=np.zeros((2,3))
print('carray2',carray2)

# 创建一个一维数组，数组长度为5，类型指定为int。
carray3=np.zeros((5,),dtype=int)
print('carray3',carray3)

# ones指定形状，不同的是，值是1
carray4=np.ones((2,3),dtype=int)

# 不初始化元素的值，元素的对应的值没有意义。
carray5=np.empty((2,3))

# 填充指定的值。
carray6=np.full((2,3),5)

# copy指定数组的形状，填充指定的值。
carray7=np.full_like(carray6,2026)
print('carray4',carray4)
print('carray5',carray5)
print('carray6',carray6)
print('carray7',carray7)


#（3）基于数值范围生成数组
# 等差数列
# 指定开始的值、结束的值、步长的值。包括开始的值，不包括结束的值。
# 数组的值为：0 2 4 6 8
darray0=np.arange(0,10,2)

# 指定开始和结束的值，num表示生成的元素个数。会生成一个等间距的数字集合。包含开始和结束的值。
# 数组的值为：[1  12  23  34  45  56  67  78  89 100]
darray1=np.linspace(1,100,10,dtype=int)

# 等对数数列
#先确定元素的值，1~10之间，元素个数是2。则对应的数组是[1,10]
#计算对数，2的1一次方，2的10次方。对应的数组是[2,1024]
darray2=np.logspace(1,10,2,base=2,dtype=int)

print('darray0',darray0)
print('darray1',darray1)
print('darray2',darray2)


#（4）特殊矩阵生成
# 零矩阵：矩阵的全部数字都为0
earray0=np.zeros((2, 2), dtype=int)

# 单位矩阵：主对角上的数字为1，其他数字为0。
earray1=np.eye(2, dtype=int)

# 对角矩阵：主对角上数字是非零，其他数字为0。
earray2=np.diag([1,5,2, 3])

print('earray0',earray0)
print('earray1',earray1)
print('earray2',earray2)

# （5）随机数组生成
# 默认会生成0~1之间的，随机浮点数的数组。
earray3=np.random.rand(2,3)
# 也可以指定数字范围为2~10
earray4=np.random.uniform(2,10,(2,3))

# randn生成正态分布的数组，数字范围是在（-3~3）之间
# 所谓正态分布是：两边小，中间大。
earray5=np.random.randn(2,3)

# 设置随机种子
# 设置种子后，每次生成的随机数组都会相同。
np.random.seed(1)
earray6=np.random.randint(1,10,(2,2))


# 布尔数组
# 指定数组类型为布尔，0为false，非0为true。
earray7=np.array([1,2,3,4,0],dtype=np.bool)

print('earray3',earray3)
print('earray4',earray4)
print('earray5',earray5)
print('earray6',earray6)
print('earray7',earray7)

