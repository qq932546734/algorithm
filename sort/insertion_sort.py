from random import shuffle, randint, seed

def insertion_sort(arr):

    for i in range(1, len(arr)):    #外层循环从第二个元素开始
        tmp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > tmp:  # 如果当前索引有效，且当前值大于待插入值
            arr[j+1] = arr[j]           # 将当前值右移，给插入挪地方
            j -= 1
        arr[j+1] = tmp
    

seed(1)
a = [randint(0,10) for _ in range(20)]
shuffle(a)
b = list(range(20,0, -1))
a = list(zip(a,b))

print(a)
insertion_sort(a)
print(a)

