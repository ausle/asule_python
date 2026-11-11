# 定义函数
"""
多行注释：
    函数的语法
         def 函数名:
           函数体
          return 返回值
"""

def my_len(data):
    count = 0
    for i in data:
        count += 1
    return count

myLen = my_len("hello world")
print(myLen)


def my_add(a,b):
    count = a+b
    return count
myAdd = my_add(11,11)
print(myAdd)

# 方法内没有return，方法会返回：None
# 在if判断中，None等于false。
def my_print(a,b):
    if a==b:
        return None
    else:
        print("function not return  %s %s" % (a, b))
        return a+b
my_print = my_print(11,11)
print(my_print)

# 也可以声明变量的初始值为None
house=None
money=None


# 函数的嵌套调用
def fun_a():
    print("fun_a")

def fun_b():
    fun_a()
    print("fun_b")

def fun_c():
    fun_b()
    print("fun_c")
fun_c()

# 局部变量、全局变量
#全局变量
global_num=20

def fun_d():
    # 局部变量local_num
    local_num=9
    # 该global_num在方法体内，是局部变量，不是指的同名的全局变量
    global_num=21
    print(global_num)
    print("fun_d %s" % local_num)

#全局变量
fun_d()
print(global_num)

def fun_e():
    # 设置该内部变量为全局变量
    global global_num
    global_num=22

fun_e()
print(global_num)

# 函数练习案例

cash=500000
record=None

print('------------主菜单------------')
print('周桀伦，欢迎你来ATM机器，请操作：')
print('')
option=input("请输入您的选择")

def qu(data):
    global cash
    cash = cash - data

def cun(data):
    global cash
    cash = cash + data















