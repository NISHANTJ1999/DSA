def Binary_search(num_list, num_to_find):
    left_index = 0
    right_index = len(num_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = left_index + (right_index - left_index) // 2

        mid_num = num_list[mid_index]

        if mid_num == num_to_find:
            return mid_index
        elif mid_num < num_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return -1


if __name__ == '__main__':
    num_list = [24, 25, 65, 85, 89, 758, 851]
    num_to_find = 851

    result = Binary_search(num_list, num_to_find)
    print(f" digit is at index {result} ")
