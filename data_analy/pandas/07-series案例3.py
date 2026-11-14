import pandas as pd


# 创建某产品 2022 年 1～12 月的销量 Series。
# freq="ME" 表示每个月的月末，与旧写法 freq="M" 的日期含义相同。
# 日期索引方便按季度汇总，也方便计算相邻月份的变化。
sales = pd.Series(
    [120, 135, 145, 160, 155, 170, 180, 175, 190, 200, 210, 220],
    index=pd.date_range("2022-01-01", periods=12, freq="ME"),
    name="销量",
)

print("2022 年各月销量：")
print(sales)


# 1. 计算季度平均销量，每 3 个月为一个季度。
# sales.index.quarter 得到每个日期所属的季度：1、2、3、4。
# groupby() 按季度分组，再用 mean() 计算每组的平均销量。
quarterly_average = sales.groupby(sales.index.quarter).mean()
print("\n各季度平均销量：")
for quarter, average in quarterly_average.items():
    print(f"第 {quarter} 季度：{average:.2f}")
# 第 1 季度：133.33；第 2 季度：161.67
# 第 3 季度：181.67；第 4 季度：210.00


# 2. 找出销量最高的月份。
# idxmax() 返回最大值对应的索引（月份）；max() 返回最大销量。
best_month = sales.idxmax()
print("\n销量最高的月份：", best_month.strftime("%Y-%m"))  # 2022-12
print("该月销量：", sales.max())  # 220


# 3. 计算月环比增长率。
# 公式：(本月销量 - 上月销量) / 上月销量 × 100%。
# pct_change() 计算相邻月份的变化比例；乘 100 后显示为百分数。
# 1 月没有上个月的数据，因此结果是 NaN。
monthly_growth_percent = (sales.pct_change() * 100).round(2)
print("\n月环比增长率（单位：%）：")
print(monthly_growth_percent)
# 2 月为 12.50%，5 月按 pandas 的 round(2) 显示为 -3.12%；负数表示销量下降。


# 4. 找出“环比连续增长超过 2 个月”的月份。
# 这里把它理解为：至少连续 3 次出现“本月销量 > 上月销量”。
# diff() 计算本月销量减去上月销量，gt(0) 判断是否增长。
is_increasing = sales.diff().gt(0)

# 每次遇到没有增长的月份，分组编号加 1，相当于重新开始计数。
# 在每个分组中累计 True（按 1 计），得到到当前月为止的连续增长月数。
group_number = (~is_increasing).cumsum()
growth_streak = is_increasing.astype(int).groupby(group_number).cumsum()

print("\n各月截至当月的连续增长月数：")
for month, count in growth_streak.items():
    print(f"{month:%Y-%m}：{count} 个月")
# 4 月达到连续增长 3 个月；5 月下降后重新从 0 开始计数。
# 11 月达到连续增长 3 个月，12 月达到连续增长 4 个月。

qualifying_months = growth_streak[growth_streak > 2].index
print("\n连续增长超过 2 个月的月份：")
for month in qualifying_months:
    print(month.strftime("%Y-%m"))
# 2022-04、2022-11、2022-12
# 完整增长区间分别为 2～4 月（连续增长 3 个月）和 9～12 月（连续增长 4 个月）。
