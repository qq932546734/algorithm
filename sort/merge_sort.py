from random import shuffle, randint, seed

def compare(x, y):
    """
    注意到这里的的等号很重要，表示如果左右指针的结果相等，选左边的
    这样的话就能保证相同元素的原顺序保持不变
    """
    return x[0] <= y[0]


def merge_sort(arr, i, j):
    """
    归并排序有几个需要注意的地方：
    1. 归并排序不可能不使用额外空间，这点不同于快速排序
    2. 怎么才能减小空间复杂度：如果每次传参的时候都传递copy的话，空间复杂度会比较高；
        如果每次生成临时数组，归并之后将结果写入到原数组中，可能会更高效一些
    """
    
    if i == j: # 首先，如果只剩下一个元素的时候，就没有必要分割了
        return 

    mid = (i+j) // 2

    merge_sort(arr, i, mid)
    merge_sort(arr, mid+1, j)
    
    left = arr[i:mid+1]
    right = arr[mid+1:j+1]
    x, y = 0, 0
    num_idx = i
    while x < len(left) or y < len(right):
        
        # 什么情况下选左边的值呢？
        # 首先左边必须不为空。然后右边为空，或者右边不为空但值更大
        if x < len(left) and (y >= len(right) or (y < len(right) and compare(left[x], right[y]))):
        #if x < len(left) and (y >= len(right) or (y < len(right) and left[x] < right[y])):
            arr[num_idx] = left[x]
            x += 1
        else:
            arr[num_idx] = right[y]
            y += 1
        num_idx += 1

#关于优化
# 1. 因为不是原位排序，所以需要另外开辟空间。比较常用的就是每次合并之前，先用临时数组复制left和right，然后排序结果写到原数组。
# 当然，假设left的长度是5，right的长度是10，那么没有必要开辟left和right两份空间。只需要开辟较小长度的那个数组的空间。如果该
# 数组是left，那么就从小到大合并；如果长度较小的数组是right，那么就从大到小合并；
# 2. 合并之前，先扫描两个数组，分别判断right的第一个元素在left中的位置，和left的最后一个元素在right中的位置，这样在合并的时候，
# 只需要合并以上求得的两个位置之前的元素，其他的都已经在正确的位置了。



seed(1)
a = [randint(0,10) for _ in range(20)]
shuffle(a)
b = list(range(20,0, -1))
a = list(zip(a,b))

print(a)
merge_sort(a, 0, len(a))
print(a)

