
def timsort():
    """
    timsort其实就是插入排序和归并排序的结合体
    选取一个长度（一般是32），然后每32个元素进行一次插入排序
    插入排序结束之后，对已经排序了的片段，一一进行归并排序
    另外一些小的优化就是对归并的优化，具体参见归并排序的优化。
    """
