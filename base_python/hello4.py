# python的for循环
# for
str1='Elon Musk showing Gayle King the Boring Company tunnels'
count=0
for x in str1:
    if x=='e':
        count+=1
print(f"一共有{count}个e")


#   待处理的数据集，称为：序列类型。序列类型的元素可以是：字符串、列表、元组等。
#   for循环遍历的数据集，就是序列。
# range取值范围，是左闭右开，[a,b)，即：a<=x<b
# range(10)，可以认为[0,10)
num1=range(10)
num2=range(1,5)
num3=range(5,10,2)  # 2可以声明步长，最后结果是：5 7 9
for x in num1:
    print(x,end=' ')
print()
for x in num2:
    print(x,end=' ')
print()
for x in num3:
    print(x,end=' ')
print()
# for循环外部实际上可以访问x，但这是不被建议的。下面IDE已经给出警告提示
print(x,end=' ')