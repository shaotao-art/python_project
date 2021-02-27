import random
"""
 #选择排序类似冒泡排序  都是将最大的挑出放到后面
 不同的是挑出最大元素的方法不一样，具体操作为：
    1选择第一个数作为最大数：
    2依次比较最大数与未排序的数的大小
        2.1如果最大数小于某个数，酒吧这个数设为最大数
    3将最大数与一个合适的数交换位置

"""
def xuanze_sort(data_to_sort):
    times=len(data_to_sort)-1
    for i in range(times):
        max_num=data_to_sort[0]
        for j in range(times-i):
            if max_num<data_to_sort[j+1]:
                max_num,data_to_sort[j+1]=data_to_sort[j+1],max_num
        max_num,data_to_sort[times-i]=data_to_sort[times-i],max_num


waiting_sort=[]
for i in range(100):
    waiting_sort.append(random.randint(0,1000))
print(waiting_sort)
xuanze_sort(waiting_sort)
print(waiting_sort)