
print("hello python")

# （1）变量的使用
# 定义一个变量，变量用于记录数据。变量名 = 变量值
money = 100
print("钱包还有：",money,"元")

money=money-10
print("钱包还有：",money,"元")

# type，输出变量的类型
print("money的数据类型是：",type(money))

# （2）数据类型的转换：数字转字符串、字符串转数字

people=10
strPeople=str(people)
floatPeople=float(people)
print("转换为字符串：",strPeople,"转换后的类型为：",type(strPeople))
print("转换为float类型：",floatPeople,"转换后的类型为：",type(floatPeople))

people="100"
intPeople=int(people)
print("转换为int类型：",intPeople,"转换后的类型为：",type(intPeople))


#（3）标识符：给变量、方法、类起的名字，这些统一称为标识符。
# （3.1）标识符的命名规则：
## 不可使用关键字
## 区分大小写
## 只允许出现（英文、下划线、数字（不允许出现开头）、中文（不推荐使用））
# （3.2）标识符的命名规范：
## 下划线命名：多个字母组成的，用下划线隔开。


#（4）运算符
## +、-、*、/、%、**、//


