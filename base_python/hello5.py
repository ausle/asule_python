# python的break、continue
import random
for x in range(10):
    if x%2==0:
        # continue结束本次循环，跳到下一个循环
        continue
    else:
        print(x,end=' ')
print()
for x in range(10):
    for y in range(10):
        if y%2==0:
            # for嵌套循环时，只针对本次循环
            continue
        else:
            print(y,end=' ')
    print()
    print(f"x is {x}")

print("==============")

# 实例：公司余额为10000，给公司20个人根据绩效score发工资。工资发完为止
money=10000
for employee in range(1,21):
    print(f"公司余额为：{money}")
    if money >0:
        score = random.randint(1, 10)
        if score >= 5:
            money = money - 1000
            print(f"员工编号：{employee}，绩效为：{score}，可领取工资为：1000元")
        else:
            print(f"员工编号：{employee}，绩效为：{score}，不可领取工资")
            continue
    else:
        print("公司余额不足")
        break