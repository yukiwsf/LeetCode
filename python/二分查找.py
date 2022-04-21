def BinarySearch(array, item):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = int((start + end) / 2)
        if array[mid] == item:
            return True
        elif array[mid] > item:
            start = mid + 1
        else:
            end = mid - 1
    return False


def BinarySearch_Recursive(array, item):
    if len(array) == 0:
        return False
    else:
        mid = len(array) // 2
        if array[mid] == item:
            return True
        elif array[mid] < item:
            return BinarySearch_Recursive(array[mid+1:], item)
        else:
            return BinarySearch_Recursive(array[:mid], item)


if __name__ == "__main__":
    l = [1, 3, 7, 4]
    print(BinarySearch(l, 3))
    print(BinarySearch_Recursive(l, 3))


