# 介绍python的字符串

# 字符串三种定义方式
people1='朱珠'
people2="朱珠"
people3="""朱珠""" #还能这么来啊！

# 字符串拼接
beautiful="漂亮"
people1=people1+beautiful
print(people1)

#通过占位的方式进行字符串拼接
star1="范冰冰"
star2="饺子"
height=170
# %s：字符串占位、%d：整数占位、%f：浮点数占位
news1="第25届台湾金马奖最佳女主角是：%s" % star1
#多个占位符
news2="第25届台湾金马奖最佳女主角是：%s，最佳导演是：%s" % (star1,star2)
print(news1)
print(news2)
news3="最佳导演%s,身高为%d" % (star2,height)
print(news3)

# f：快速格式化，不关注格式转换以及对精度的控制。
news4=f"第25届台湾金马奖最佳女主角是:{star1}，最佳导演是：{star2}，他的身高是：{height}"
print(news4)

# 对表达式进行格式化
news5=f"1*1的结果是什么类型，{type(1*1)}"
print(news5)


name="谷歌"
stock_price=19.99
stock_code="999888"
stock_price_daily_growth_factor=1.2 #股票每日增长系数
growth_days=7
growth_days_stock_price=stock_price*stock_price_daily_growth_factor*growth_days

#%7.2f：对浮点数进行精度控制，总长度7位，小数点2位。
news6=(f"公司{name},股票代码{stock_code}，当前股价{stock_price},每次增长系数是{stock_price_daily_growth_factor}"
      ,",经过%s天的增长后，股价达到了%7.2f" %(growth_days,growth_days_stock_price))
print(news6)







