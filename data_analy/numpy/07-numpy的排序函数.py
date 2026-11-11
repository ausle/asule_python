import numpy as np


# 1. 升序、降序：np.sort 返回新数组，原数组不变
print("=== 一维数组排序 ===")
values = np.array([5, 2, 8, 2, 1])
print("原数组：", values)                    # [5 2 8 2 1]
print("升序：", np.sort(values))            # [1 2 2 5 8]
print("降序：", np.sort(values)[::-1])      # [8 5 2 2 1]
print("原数组仍然是：", values)              # [5 2 8 2 1]


# 2. argsort 返回排序后的原位置，不是排序后的数值
# kind="stable" 保证相同元素保持原来的先后顺序
print("\n=== 排序后的下标 ===")
order = np.argsort(values, kind="stable")
print("排序后的原下标：", order)             # [4 1 3 0 2]
print("用下标取出升序结果：", values[order])  # [1 2 2 5 8]


# 3. 二维数组：axis=1 每行分别排序；axis=0 每列分别排序
print("\n=== 二维数组按行、按列排序 ===")
matrix = np.array([[9, 1, 7],
                   [3, 5, 2]])
print("原矩阵：\n", matrix)
# [[9 1 7]
#  [3 5 2]]
print("每行升序：\n", np.sort(matrix, axis=1))
# [[1 7 9]
#  [2 3 5]]
print("每列升序：\n", np.sort(matrix, axis=0))
# [[3 1 2]
#  [9 5 7]]
print("每行升序对应的原列下标：\n", np.argsort(matrix, axis=1))
# [[1 2 0]
#  [2 0 1]]


# 4. ndarray.sort() 会直接修改数组本身
print("\n=== 原地排序 ===")
in_place = values.copy()
in_place.sort()
print("原地排序后的数组：", in_place)         # [1 2 2 5 8]
print("最初的 values：", values)           # [5 2 8 2 1]
