import numpy as np


# 1. 一维数组的常用统计函数
print("=== 一维数组的统计 ===")
data = np.array([2, 4, 4, 4, 5, 5, 7, 9])
print("数据：", data)                         # [2 4 4 4 5 5 7 9]
print("元素个数：", data.size)               # 8
print("总和：", np.sum(data))                # 40
print("平均值：", np.mean(data))             # 5.0
print("中位数：", np.median(data))           # 4.5
print("最小值：", np.min(data))              # 2
print("最大值：", np.max(data))              # 9
print("极差：", np.ptp(data))                # 7，最大值减最小值
print("总体方差：", np.var(data))            # 4.0，默认 ddof=0
print("总体标准差：", np.std(data))          # 2.0
print("样本方差：", np.var(data, ddof=1))    # 4.571428571428571
print("25%、50%、75% 分位数：", np.percentile(data, [25, 50, 75]))
# [4.  4.5 5.5]


# 2. 最大值和最小值的位置：下标从 0 开始
print("\n=== 统计值的位置 ===")
print("最小值的下标：", np.argmin(data))       # 0
print("最大值的下标：", np.argmax(data))       # 7


# 3. 二维数组：axis=0 按列统计，axis=1 按行统计
print("\n=== 二维数组按行、按列统计 ===")
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
print("矩阵：\n", matrix)
# [[1 2 3]
#  [4 5 6]]
print("每列求和：", np.sum(matrix, axis=0))   # [5 7 9]
print("每行求和：", np.sum(matrix, axis=1))   # [ 6 15]
print("每列平均值：", np.mean(matrix, axis=0))  # [2.5 3.5 4.5]
print("每行平均值：", np.mean(matrix, axis=1))  # [2. 5.]


# 4. 累计求和与缺失值
print("\n=== 累计求和与缺失值 ===")
print("累计求和：", np.cumsum([1, 2, 3, 4]))  # [ 1  3  6 10]
with_nan = np.array([1.0, np.nan, 3.0])
print("普通平均值：", np.mean(with_nan))       # nan
print("忽略 nan 求平均：", np.nanmean(with_nan))  # 2.0
