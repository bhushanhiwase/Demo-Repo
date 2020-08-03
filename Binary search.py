# code for binary search

def binary(lst, target):

    start = 0
    end = len(lst)

    while start <= end:
        mid = (start + end) // 2

        if lst[mid] == target:
            return True

        if target > lst[mid]:
            start = mid +  1
        else:
            end = mid - 1

        if start >= end:
            return False


print(binary([i for i in range(0,5)], 4))
