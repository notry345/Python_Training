def simple_sort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a
#리스트 a를 정렬하는 간단한 알고리즘

import random
import time
large_list = list(range(200000))
random.shuffle(large_list)
st = time.time()
simple_sort(large_list)
print("Running time: %f sec"%(time.time()-st))

def merge_sort(a):
    front = a[0:(len(a)/2)-1]
    end = a[len(a)/2:len(a)-1]
    sorted_fornt = simple_sort(front)
    sorted_end = simple_sort(end)
    for i in range(len
