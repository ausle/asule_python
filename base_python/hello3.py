import random

# input语句
# print("请告诉我你是谁?")
# name=input();
# print("我的名字是：%s" % name)
# print(f"我的名字是：{name}")
#
# number=input("你的身份证号是：")
# print(f"身份证号是:{number}，输入的身份证号类型是：{type(number)}")

# 布尔类型和比较运算
hot=True
cold=False
print("类型为：%s" % type(hot))

#if语句
age = int(input("请输入你的年龄："))
if age>18:
    print("你成年了")
elif age==18:
    print("刚刚好成年")
else:
    print("未成年")


# while循环语句
i=1
sum=0
while i<=100:
    sum+=i
    print(f"循环了,{i}次数")
    i += 1
print(f"1~100的和是：{sum}")
print("1~100的和是：%s" % sum)


# 输入数字，判断是否等于生成的随机数
randomNumber=random.randint(1,100)
count=0
flag=True
print(f"生成的随机数是：{randomNumber}")
while flag:
    inputNumber = int(input("请输入一个随机数"))
    count += 1
    # if-else需要在while方法内
    if inputNumber == randomNumber:
        flag = False
    else:
        if inputNumber > randomNumber:
            print("你输入的数字大了")
        else:
            print("你输入的数字小了")
print(f"你一共输入了{count}次，才猜中结果")
# end = ''，实现print不换行的效果
print(f"你一共输入了{count}次，才猜中结果",end='')

# 通过while循环，输出 9*9乘法表
row = 1
while row <= 9:
    # 初始化内层循环变量（控制列数，从1到当前行数）
    col = 1
    while col <= row:
        # 拼接乘法表达式（格式：列×行=结果，对齐显示）
        print(f"{col}×{row}={col*row}\t", end="")
        col += 1  # 列数自增
    print()  # 每行结束后换行
    row += 1  # 行数自增



