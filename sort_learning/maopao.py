import random
import  time
'''
冒泡排序 ：
    每次选出最大的一个数放在数组的后面
    eg：
        第一次选出最大的数，放在最后一个。
        第二次选出剩余的数中的最大的数，放在倒数第二个
        依次类推
        
    比较的次数是len（list）-1  20个数就要冒泡19次 即挑出19次最大的数
    比较的方法是，从第一个数依次开始比较，如果前一个数大于后一个数 则交换位置
    
tips
    >>>range(10)        # 从 0 开始到 10
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    参数是几就比几次
'''


def maopao_sort(data_to_be_sort):
    start=time.time()
    times = len(data_to_be_sort) - 1
    for i in range(times):
        for j in range(times - i ):#第一次一共20个数 比较的次数是19次
            if data_to_be_sort[j] > data_to_be_sort[j + 1]:
                data_to_be_sort[j], data_to_be_sort[j + 1] = data_to_be_sort[j + 1], data_to_be_sort[j]
    end=time.time()
    print(end-start)

waiting_sort=[]
for i in range(10000):
    waiting_sort.append(random.randint(0,1000))
maopao_sort(waiting_sort)