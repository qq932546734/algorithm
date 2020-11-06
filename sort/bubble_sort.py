from random import shuffle

a = [i+1 for i in range(9)]
shuffle(a)


def bubble_sort(nums):
    
    m = len(nums)
    for i in range(m-1):                # 对于m个元素的数组，外层循环只需要m-1次；比如对于3个数的数组，只需要遍历两次
        for j in range(m-i-1):          # j为内层循环的点，因为是比较当前元素和下一个元素，所以j只需要到最后一个数的前一个数
            if nums[j] > nums[j+1]:     # 如果当前数比下一个数大，交换这两个元素
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


def bubble_sort(nums):
    """
    此处有两处优化：
    1. sorted记录本次内层遍历是否有交换；如果没有交换，表示完全排序了，可以提前结束了
    2. right记录本次内层遍历交换的右边界，下次遍历的时候只需要遍历到这个位置即可
    """
    
    m = len(nums)   
    right = m-1                 # 内层遍历需要遍历的右边界；这样的话，不必遍历不必要的部分

    for i in range(m-1):
        right_next = 0          # 每次内层遍历开始的时候，初始化右边界；遍历结束后，记录的便是下一次遍历的时候的右边界
        sorted = True           # 内层遍历，默认是已经排序的；如果内层遍历的过程中有交换，表示并没有完全排序，sorted变成false 
        for j in range(right):  # 因为j是要跟下一个数比较，所以j最后取到比right刚好小1
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                right_next = j
                sorted = False

        right = right_next      # 确定下一个边界
        if sorted: break        # 如果完全排序了，直接结束
    return nums

def cock_tail(nums):
    """
    鸡尾酒排序：上面的优化，我们只记录了右边界，避免右边界之后的重复比较。但如果恰巧
    最小值就在最右测，此时右边界的优化基本不起作用，还是得每次遍历到m-i。
    鸡尾酒排序的思想就是，先从左往右冒泡，然后从右往左冒泡 """ 


print(a)
nums = bubble_sort(a)
print(nums)
