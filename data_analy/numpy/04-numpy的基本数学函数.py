import numpy as np


# 1. 加、减、乘、除
print("=== 加、减、乘、除 ===")
a = np.array([10, 20, 30])
b = np.array([2, 4, 5])

print("a + b =", a + b)  # a + b = [12 24 35]
print("a - b =", a - b)  # a - b = [ 8 16 25]
print("a * b =", a * b)  # a * b = [ 20  80 150]
print("a / b =", a / b)  # a / b = [5. 5. 6.]


# 2. 绝对值、平方、平方根
print("\n=== 绝对值、平方、平方根 ===")
x = np.array([-4, -1, 0, 1, 4])
y = np.array([1, 4, 9])

print("绝对值：", np.abs(x))             # [4 1 0 1 4]
print("平方：", np.power(y, 2))         # [ 1 16 81]
print("平方（另一种写法）：", y ** 2)     # [ 1 16 81]
print("平方根：", np.sqrt(y))           # [1. 2. 3.]


# 3. 指数与对数
print("\n=== 指数与对数 ===")

print("e 的exp计算：", np.exp(1)) # e的一次方： 2.718281828459045

print("e 的幂：", np.exp([0, 1]))
# [1.         2.71828183]

print("自然对数：", np.log([1, np.e]))
# [0. 1.]

print("以 10 为底的对数：", np.log10([1, 100]))
# [0. 2.]


# 4. 取整
print("\n=== 取整 ===")
numbers = np.array([-2.7, -1.2, 1.2, 2.7])

print("向下取整：", np.floor(numbers))  # [-3. -2.  1.  2.]
print("向上取整：", np.ceil(numbers))   # [-2. -1.  2.  3.]
print("四舍五入：", np.round(numbers))  # [-3. -1.  1.  3.]


# 5. 三角函数：使用弧度
print("\n=== 三角函数 ===")

print("sin(π/2) =", np.sin(np.pi / 2))  # 1.0
print("cos(π) =", np.cos(np.pi))        # -1.0


# 6. 汇总计算
print("\n=== 求和、平均值、最大值 ===")
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

print("矩阵：")
print(matrix)
# [[1 2 3]
#  [4 5 6]]

print("所有元素求和：", np.sum(matrix))    # 21
print("所有元素求平均：", np.mean(matrix))  # 3.5
print("最大值：", np.max(matrix))         # 6
print("最小值：", np.min(matrix))         # 1

print("每列求和：", np.sum(matrix, axis=0))  # [5 7 9]
print("每行求和：", np.sum(matrix, axis=1))  # [ 6 15]