def BubbleSort(array):
    """冒泡排序也可以看成把array分为待排序列和已排序列，
    每趟冒泡从待排序列传递出一个最大值放在待排序列末尾即已排序列开头"""
    n = len(array)
    # 如果array只有0或1个元素，return
    if n == 1 or n == 0:
        return
    # 一共至多要进行len(array)-1趟冒泡排序，
    # 因为每次待排序列中都有一个最大的被放在了末尾，排好了len(array)-1个元素则整个array完成排序
    for j in range(1, n):
        cnt = 0
        # 每趟冒泡排序要从头到尾依次比较待排序列的每一个元素和后一个元素，逆序则交换
        # 每经过一次冒泡排序，待排序列长度减一
        for i in range(n - j):
            if array[i] > array[i + 1]:
                array[i + 1], array[i] = array[i], array[i + 1]
                cnt += 1
        # 如果一趟冒泡排序没有交换任何元素，则证明排序完成
        if not cnt:
            break


def SelectionSort(array):
    """选择排序把array分成待排序列（下标0～末尾）和已排序列（下标0），
    初始化两个指针i和j，每次从待排序列中找到一个最小值放到已排序列最右端末尾即待排序列最左端开头"""
    n = len(array)
    # 遍历待排序列的所有起点（第0个元素），待排序列起点下标j，终点下标n-1
    for j in range(n - 1):
        # 初始化待排序列的最小值下标
        min_idx = j
        # 遍历待排序列从第1个元素开始到最后一个元素，指针i初始化值比指针j大1
        for i in range(j + 1, n):
            if array[min_idx] > array[i]:
                # 更新待排序列最小值下标
                min_idx = i
        # 如果最小值下标有发生变化，则把当前待排序列的最小值放到待排序列的开头
        if min_idx != j:
            array[min_idx], array[j] = array[j], array[min_idx]


def InsertionSort(array):
    """插入排序把array分成已排序列（下标0）和待排序列（下标1～末尾），
    每次从待排序列开头拿一个元素与已排序列所有元素比较"""
    n = len(array)
    # 初始化指针j遍历待排序列的每个元素，每次循环结束待排序列数量减一，
    # 因为待排序列第0个元素被放入已排序列，已排序列数量加一
    for j in range(1, n):
        # 初始化指针i从右向左遍历已排序列的每个元素，依次跟待排序列比较，逆序则交换——冒泡
        for i in range(j, 0, -1):
            if array[i - 1] > array[i]:
                array[i], array[i - 1] = array[i - 1], array[i]


def QuickSort(array, start, end):
    """快速排序选择array开头元素作为主元（pivot），
    把主元右边的所有元素依次跟主元比较，小于主元的放左边，大于主元的不动，
    找到主元的位置再依次对主元左右的序列进行递归排序"""
    # 函数出口，如果起点大于等于终点则终止
    if start >= end:
        return
    # 定义主元
    pivot = array[start]
    # 定义左右指针
    left = start
    right = end
    # 循环遍历除主元以外的每个元素，找主元的位置
    while left < right:
        # 从右向左遍历，如果元素大于等于主元，则不动，右指针往左挪一位
        while left < right and array[right] >= pivot:
            right -= 1
        # 如果小于主元，则把值赋值给左指针
        array[left] = array[right]
        # 从左向右遍历，如果元素小于等于主元，则不动，左指针往右挪一位
        while left < right and array[left] <= pivot:
            left += 1
        # 如果大于主元，则把值赋值给右指针
        array[right] = array[left]
    # 循环结束，找到主元的位置
    array[left] = pivot
    # 递归排序主元左边序列
    QuickSort(array, start, left - 1)
    # 递归排序主元右边序列
    QuickSort(array, right + 1, end)


def InsertionSort1(array, start, end):
    """插入排序把array分成已排序列（下标0）和待排序列（下标1～末尾），
    每次从待排序列开头拿一个元素与已排序列所有元素比较"""
    # 遍历待排序列的每个元素
    for j in range(start + 1, end + 1):
        # 从右向左遍历已排序列的每个元素，依次跟待排序列比较，逆序则交换——冒泡
        for i in range(j, start, -1):
            if array[i - 1] > array[i]:
                array[i], array[i - 1] = array[i - 1], array[i]


if __name__ == "__main__":
    l = [9, 9, 1, 9, 8]
    # BubbleSort(l)
    # SelectionSort(l)
    QuickSort(l, 0, len(l) - 1)
    print(l)