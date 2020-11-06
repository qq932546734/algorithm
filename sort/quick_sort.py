from random import shuffle
from random import randint

count = 0

def quick_sort(nums, i, j):
    """

    简单描述：选第一个元素为pivot（如果想随机选取pivot的话，可以先将第一个元素
    与其它随机一个元素交换），然后初始化双指针：第一个元素（对，与pivot重复）为
    左指针，最后一个元素为右指针。
    一次操作：先处理右指针，如果当前数大于或等于pivot，那么左移，直到找到小于pivot
    的数，或者达到越界条件；
    然后处理左指针，如果当前数小于或等于pivot，那么右移，直到找到大于pivot的数，
    此时，左边是一个本该放到右边的数，右边是一个本该放到左边的数，交换之。
    一次操作之后，虽然交换了左指针和右指针的值，但是此时指针不增减（左指针不加一，
    右指针不减一，这样的好处是处理一些边界情况比较方便）。然后继续上述操作，
    直到越界，即i==j。
    最后，还需要将结束位置i和pivot的数进行交换。
    然后分别对左边和右边的进行同样的操作。
    """

    if i >= j: return                       # 如果越界了 
    
    pivot = nums[i]
    start, end = i, j
    while i < j:                            # 不能取等号，相等的时候，表示两个指针相遇了
        
        while i < j and nums[j] >= pivot:   # 大于或等于都继续，之所以等号的时候也继续，是因为
            j -= 1

        while i < j and nums[i] <= pivot:   # 小于或等号的时候都继续
            i += 1

        if i < j: nums[i], nums[j] = nums[j], nums[i]


    if i != start:
        nums[i], nums[start] = pivot, nums[i]           # 结束之后，记得将pivot放到应该放置的位置

    if start < i-1: quick_sort(nums, start, i-1)        # 注意，因为i位置的数字已经肯定是在对的index上，所以只需要对之前和之后的进行排序
    if i+1 < end: quick_sort(nums, i+1, end)            # 因此，需要i-1 和 i+1

    return nums


def quick_sort_s(nums, i, j):
    if i >= j: return
    start, end = i, j 
    rand_idx = randint(0, j-i+1)
    nums[i], nums[rand_idx] = nums[rand_idx], nums[i]
    pivot = i
    while i < j:
        while i < j and nums[j] >= nums[pivot]:
            j -= 1
        while i < j and nums[i] <= nums[pivot]:
            i += 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    
    nusm[pivot], nums[i] = nums[i], nums[pivot]
    quick_sort_s(nums, start, i-1)
    quick_sort_s(nums, i+1, end)

       

nums = [randint(0, 80) for i in range(100)]
shuffle(nums)

#nums = [5, 2, 1, 9, 8, 7, 6, 10, 4, 3]
print(nums)
print(quick_sort(nums, 0, len(nums)-1))
