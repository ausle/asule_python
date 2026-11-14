import pandas as pd


# 创建一周每天的最高温度 Series。
# index 是星期几，值是当天的最高温度，单位为摄氏度。
temperatures = pd.Series(
    [28, 31, 29, 32, 30, 27, 33],
    index=["周一", "周二", "周三", "周四", "周五", "周六", "周日"],
    name="最高温度（℃）",
)

print("一周每天的最高温度：")
print(temperatures)


# 1. 找出温度严格超过 30℃ 的天数。
# temperatures > 30 会逐个比较，得到 True/False；sum() 把 True 按 1 计数。
# 周五恰好是 30℃，因此不计入“超过 30℃”。
hot_days = temperatures[temperatures > 30]
print("\n超过 30℃ 的天数：", (temperatures > 30).sum())  # 3 天
print("超过 30℃ 的日期和温度：")
print(hot_days)  # 周二 31℃、周四 32℃、周日 33℃


# 2. 计算这一周每天最高温度的平均值。
average_temperature = temperatures.mean()
print("\n平均温度：", average_temperature, "℃")  # 30.0℃


# 3. 按温度从高到低排序。
# sort_values() 默认从低到高；ascending=False 改为从高到低。
# 它返回新的 Series，不会修改原来的 temperatures。
sorted_temperatures = temperatures.sort_values(ascending=False)
print("\n温度从高到低排序：")
print(sorted_temperatures)
# 顺序：周日 33、周四 32、周二 31、周五 30、周三 29、周一 28、周六 27


# 4. 找出相邻两天中温度变化最大的那一对。
# diff() 计算“当天温度 - 前一天温度”：周一没有前一天，因此结果是 NaN。
# 变化可能是升温，也可能是降温；abs() 取绝对值后才能比较变化幅度。
daily_change = temperatures.diff()
absolute_change = daily_change.abs()
print("\n每天相对前一天的温度变化：")
print(daily_change)  # 周二 +3、周三 -2、周四 +3、周五 -2、周六 -3、周日 +6

# idxmax() 找到最大温差对应的“后一天”；这里是周日。
later_day = absolute_change.idxmax()
later_position = temperatures.index.get_loc(later_day)
earlier_day = temperatures.index[later_position - 1]
largest_change = absolute_change.loc[later_day]

print("\n温度变化最大的相邻两天：", earlier_day, "和", later_day)  # 周六 和 周日
print("两天的温度：", temperatures.loc[earlier_day], "℃ →", temperatures.loc[later_day], "℃")
# 27℃ → 33℃
print("最大温差：", largest_change, "℃")  # 6.0℃
