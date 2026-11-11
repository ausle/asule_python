import numpy as np


# 1. 比较会逐元素进行，结果是布尔数组
print("=== 逐元素比较 ===")
a = np.array([1, 2, 3, 4])
b = np.array([2, 2, 2, 2])
print("a == b：", a == b)  # [False  True False False]
print("a != b：", a != b)  # [ True False  True  True]
print("a > b：", a > b)    # [False False  True  True]
print("a >= b：", a >= b)  # [False  True  True  True]
print("a < b：", a < b)    # [ True False False False]
print("a <= b：", a <= b)  # [ True  True False False]


# 这些 NumPy 函数分别对应上面的 ==、!=、>、>=、<、<=
print("\n=== 对应的 NumPy 比较函数 ===")
print("equal：", np.equal(a, b))                  # [False  True False False]
print("not_equal：", np.not_equal(a, b))          # [ True False  True  True]
print("greater：", np.greater(a, b))              # [False False  True  True]
print("greater_equal：", np.greater_equal(a, b))  # [False  True  True  True]
print("less：", np.less(a, b))                    # [ True False False False]
print("less_equal：", np.less_equal(a, b))        # [ True  True False False]


# 2. 多个条件：数组使用 &、|、~，每个条件要加括号
print("\n=== 组合条件与筛选 ===")
between_2_and_3 = (a >= 2) & (a <= 3)
print("在 2 到 3 之间：", between_2_and_3)  # [False  True  True False]
print("筛选后的元素：", a[between_2_and_3])  # [2 3]
print("小于 2 或大于 3：", (a < 2) | (a > 3))  # [ True False False  True]
print("不是偶数：", ~(a % 2 == 0))           # [ True False  True False]


# 3. any / all 把布尔数组汇总成一个布尔值
print("\n=== any 和 all ===")
print("是否存在大于 3 的数：", np.any(a > 3))  # True
print("是否全部大于 0：", np.all(a > 0))    # True
print("是否全部等于 2：", np.all(a == 2))   # False


# 4. 按条件选择值；比较整个数组；比较浮点数
print("\n=== where、array_equal、isclose ===")
print("小于等于 2 的位置填 0：", np.where(a > 2, a, 0))  # [0 0 3 4]
print("两个数组是否完全相同：", np.array_equal(a, [1, 2, 3, 4]))  # True
print("0.1 + 0.2 == 0.3：", 0.1 + 0.2 == 0.3)  # False
print("浮点数是否近似相等：", np.isclose(0.1 + 0.2, 0.3))  # True
