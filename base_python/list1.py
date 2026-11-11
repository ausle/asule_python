# python列表

# 定义一个列表
my_num_list=[1,2,34,4]
my_lesson_list=["math","physics","chemistry"]

# 列表中可嵌套列表，列表中的元素类型可以不相同
my_complex_list=["1",99,"chemistry",my_num_list]
print(my_complex_list)
print(my_complex_list[2])
print(my_complex_list[3][1])

# 居然还能反向索引，最右的元素的索引是-1，从右往左递减：-1、-2、-3....
print(my_complex_list[-1][-1])
print(my_complex_list[-1][-2])