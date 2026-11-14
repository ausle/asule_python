import numpy as np      # 用 NumPy 生成随机成绩
import pandas as pd     # 用 pandas 创建 Series，并计算统计结果


# 设置随机种子：每次运行都会生成同一组成绩，方便核对结果
np.random.seed(42)

# randint(50, 101, 10)：
# 50 是最小值，包含 50；
# 101 是上限，不包含 101，因此最大可能值是 100；
# 10 表示生成 10 个整数。
random_scores = np.random.randint(50, 101, 10)

# 为 10 名学生生成索引标签：学生1、学生2、……、学生10
student_names = ["学生" + str(i) for i in range(1, 11)]

# 将成绩和学生姓名组合成一个 Series
# index：每个成绩对应的学生姓名
# name：这个 Series 的名称
scores = pd.Series(random_scores, index=student_names, name="数学成绩")

# 固定随机种子后，成绩依次为：
# 学生1: 88，学生2: 78，学生3: 64，学生4: 92，学生5: 57
# 学生6: 70，学生7: 88，学生8: 68，学生9: 72，学生10: 60


# mean()：计算 10 名学生的平均分
average = scores.mean()  # 73.7

# max()：找出最高分
highest = scores.max()    # 92

# min()：找出最低分
lowest = scores.min()     # 57

# scores > average 会逐个比较成绩，得到 True/False
# 只有严格高于平均分才是 True，等于平均分不算
# 对布尔值求和时，True 按 1 计算，False 按 0 计算
above_average_count = (scores > average).sum()  # 4 人


print("10 名学生的数学成绩：")
print(scores)

print("平均分：", average)                  # 73.7
print("最高分：", highest)                 # 92
print("最低分：", lowest)                  # 57
print("高于平均分的学生人数：", above_average_count)  # 4