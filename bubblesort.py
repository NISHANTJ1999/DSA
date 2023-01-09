def bubble_sort(arr):
    n = len(arr)
    for iter_num in range(n):
        for curr_num in range(0, n - iter_num - 1):
            if arr[curr_num] > arr[curr_num + 1]:
                arr[curr_num], arr[curr_num + 1] = arr[curr_num + 1], arr[curr_num]
    return arr


if __name__ == '__main__':
    arr = [5, 4,]
    print(bubble_sort(arr))
