from typing import List


def DeveloperPairs(strArr):

    strArr: list[int] = [int(x) for x in input().split()]

    list_of_pairs = []
    for i in range(len(strArr) - 2):
        for j in range(i + 2, len(strArr)):
            I = str(strArr[i] + strArr[j])
            list_of_pairs.append(I)
    unique_pair = []

    for number in list_of_pairs:
        temp = []
        for num in number:
            if num not in temp:
                temp.append(num)

        if len(temp) == 6:
            unique_pair.append(num)

        if len(unique_pair) == 0:
            print(-1)

    else:
        max_length = 0
        for pair in unique_pair:
            a = len(pair)
            if a > max_length:
                length = []

                max_length = a

                length.append(pair)

            elif (a == max_length):
                length.append(pair)
    No = []
    for i in range(len(length)):
        for j in range(2):
            No.append(length[i][j])

    No.sort()
    a = len(length)

    for m in range(len(length)):
        if No[0] == length[m][0] or No[0] == length[m][1]:
            print(length[0])
            break

    return strArr

print(DeveloperPairs(input()))