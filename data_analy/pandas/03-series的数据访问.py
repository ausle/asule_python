import pandas as pd


series = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"], name="销量")
print("原 Series：", series.to_dict())  # {'a': 10, 'b': 20, 'c': 30, 'd': 40}


# 1. 访问单个元素：loc/at 按索引标签；iloc/iat 按整数位置（从 0 开始）。
print("\n=== 访问单个元素 ===")
print("标签 b 对应的值：", series.loc["b"])  # 20：通过显示索引访问
print("用 at 访问标签 b：", series.at["b"])  # 20

print("位置 1 对应的值：", series.iloc[1])  # 20
print("用 iat 访问位置 1：", series.iat[1])  # 20


print("========", series[1])     # 取数据；[1] 的含义可能受索引类型影响，建议明确写成 series.iloc[1]，不太推荐这种写法
print("========", series["c"])   # 取索引标签为 "c" 的元素，建议明确写成 series.loc["c"]，不太推荐这种写法
print("========", series.head(1))  # 返回前 1 个元素，默认5行
print("========", series.tail(2))  # 返回后 2 个元素，默认5行


# 2. 访问多个元素；to_dict() 让输出更容易看出标签和值的对应关系。
print("\n=== 访问多个元素 ===")
print("按标签选 a、c：", series.loc[["a", "c"]].to_dict())  # {'a': 10, 'c': 30}
print("按位置选 0、2：", series.iloc[[0, 2]].to_dict())   # {'a': 10, 'c': 30}


# 3. 标签切片包含终点 d；位置切片不包含终点位置 3。
print("\n=== 切片 ===")
print("标签 b 到 d：", series.loc["b":"d"].to_dict())  # {'b': 20, 'c': 30, 'd': 40}
print("位置 1 到 3：", series.iloc[1:3].to_dict())  # {'b': 20, 'c': 30}


# 4. 条件筛选：比较得到布尔 Series，再用它挑选数据。
print("\n=== 条件筛选 ===")
mask = series > 20
print("筛选条件：", mask.to_dict())  # {'a': False, 'b': False, 'c': True, 'd': True}
print("大于 20 的值：", series.loc[mask].to_dict())  # {'c': 30, 'd': 40}
print("不存在的标签，返回默认值：", series.get("x", 0))  # 0


# 5. 索引标签也可能是整数。即使用同一个数字，loc 与 iloc 的含义也不同。
print("\n=== 整数标签与整数位置 ===")
number_index = pd.Series([100, 200, 300], index=[1, 2, 3])
print("loc[1]，标签 1：", number_index.loc[1])   # 100
print("iloc[1]，位置 1：", number_index.iloc[1])  # 200
