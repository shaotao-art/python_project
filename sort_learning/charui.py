import random
import time
"""
插入排序：
    插入排序：即将未排序的第一个数据插入到已经有序的数中（插入时可以利用二分法）
    步骤：将第i+1个数据插入到前i个已经拍好的数据中
        第一个数据我们将其看成已经有序的只有一个数据的列表
    12.688257694244385
"""

def charui_sort(data_to_sort):
    start=time.time()
    times=len(data_to_sort)-1
    for i in range(times):
        j=i+1
        while(data_to_sort[j]<data_to_sort[j-1] and j>=1):
            data_to_sort[j],data_to_sort[j-1]=data_to_sort[j-1],data_to_sort[j]
            j=j-1
    end=time.time()
    print(end-start)

waiting_sort=[]
for i in range(10000):
    waiting_sort.append(random.randint(0,1000))

charui_sort(waiting_sort)
print(waiting_sort)
