

import pandas as pd

'''

1、numpy和pandas

    numpy擅长处理数组数据。
    pandas擅长处理，带列名的表格数据。
    pandas中最重要的两个数据结构，分别是：Series和DataFrame
    
    Series可以理解为：表格数据的字段，字段类型，字段约束。
    

'''


# 创建series

# (1)、最简单一种Series的创建
s0=pd.Series([10,2,3,4,5])

# (2)、自定义索引
s1=pd.Series([10,2,3,4,5],index=['a','b','c','d','e'])

# （3）、声明name，name属性标记，Series的这一列，数据是做什么的。
s2=pd.Series([10,2,3,4,5],index=['a','b','c','d','e'],name='月份')

#（4）、通过字典的方式创建

# 通过字典来创建
s3 = pd.Series({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5})
# 从一个series中取一部分，创建一个新的series
s4 = pd.Series(s3, index=["a", "c"])

print(s0)
print(s1)
print(s2)
print(s3)
print(s4)

