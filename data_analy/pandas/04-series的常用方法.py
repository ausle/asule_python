import pandas as pd


scores = pd.Series([80, 90, None, 90, 70], index=["a", "b", "c", "d", "e"], name="成绩")


# 1. 查看开头、结尾与汇总统计
print("=== 查看与统计 ===")
print("前 2 个：", scores.head(2).to_dict())  # {'a': 80.0, 'b': 90.0}
print("后 2 个：", scores.tail(2).to_dict())  # {'d': 90.0, 'e': 70.0}
print("非缺失值个数：", scores.count())      # 4
print("总和：", scores.sum())             # 330.0
print("平均值：", scores.mean())          # 82.5
print("最大值：", scores.max())           # 90.0
print("统计摘要（节选）：", scores.describe().loc[["count", "mean", "min", "max"]].to_dict())
# {'count': 4.0, 'mean': 82.5, 'min': 70.0, 'max': 90.0}


# 2. 缺失值：isna 检查，fillna 填充，dropna 删除。
# 这些方法默认返回新 Series，原来的 scores 不变。
print("\n=== 缺失值处理 ===")
print("缺失值位置：", scores.isna().tolist())  # [False, False, True, False, False]
print("缺失值个数：", scores.isna().sum())   # 1
print("缺失值填 0 后转整数：", scores.fillna(0).astype(int).to_dict())
# {'a': 80, 'b': 90, 'c': 0, 'd': 90, 'e': 70}
print("删除缺失值：", scores.dropna().to_dict())
# {'a': 80.0, 'b': 90.0, 'd': 90.0, 'e': 70.0}


# 3. 排序：sort_values 按值排序，sort_index 按索引标签排序。
print("\n=== 排序 ===")
print("成绩降序：", scores.dropna().sort_values(ascending=False).tolist())
# [90.0, 90.0, 80.0, 70.0]
other = pd.Series([30, 10, 20], index=["c", "a", "b"])
print("按索引排序：", other.sort_index().to_dict())  # {'a': 10, 'b': 20, 'c': 30}
print("按值降序：", other.sort_values(ascending=False).to_dict())
# {'c': 30, 'b': 20, 'a': 10}


# 4. 去重、计数，以及逐个元素转换
print("\n=== 去重、计数和转换 ===")
fruits = pd.Series(["苹果", "香蕉", "苹果", "橙子", "香蕉"])
print("不同的值：", fruits.unique().tolist())  # ['苹果', '香蕉', '橙子']
print("不同值的个数：", fruits.nunique())       # 3
print("每个值出现的次数：", fruits.value_counts().to_dict())
# {'苹果': 2, '香蕉': 2, '橙子': 1}
print("每个非缺失成绩加 5：", scores.dropna().map(lambda value: value + 5).tolist())
# [85.0, 95.0, 95.0, 75.0]
