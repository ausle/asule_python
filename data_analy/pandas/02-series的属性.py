import pandas as pd


# Series 是带索引的一维数据；作为 DataFrame 的一列时，也包含这一列的所有值。
# name 和 dtype 是属性，但 Series 不会自动执行“非空、唯一”等字段约束。
series = pd.Series([10, 20, 30], index=["a", "b", "c"], name="销量", dtype="int64")

print("=== Series 的基本属性 ===")
print("名称 name：", series.name)                # 销量
print("索引 index：", series.index.tolist())   # ['a', 'b', 'c']
print("值 values：", series.values)            # [10 20 30]
print("转为 NumPy 数组：", series.to_numpy())   # [10 20 30]
print("数据类型 dtype：", series.dtype)        # int64
print("形状 shape：", series.shape)            # (3,)
print("维度 ndim：", series.ndim)              # 1
print("元素个数 size：", series.size)          # 3
print("是否为空 empty：", series.empty)       # False
print("是否含缺失值 hasnans：", series.hasnans)  # False


# pandas 的可空整数类型 Int64 可以同时存放整数和缺失值 pd.NA。
nullable = pd.Series([10, pd.NA, 30], index=["a", "b", "c"], dtype="Int64")
print("\n=== 带缺失值的 Series ===")
print("数据类型：", nullable.dtype)           # Int64
print("是否含缺失值：", nullable.hasnans)     # True
print("缺失值位置：", nullable.isna().tolist())  # [False, True, False]
