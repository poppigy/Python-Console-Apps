from typing import List


def duplicateZeros(arr: List[int]) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """
    count = 0
    trimmed = len(arr) - 1
    for i in range(len(arr)):
        if arr[i] == 0 and arr[trimmed - count] != 0:
            count += 1

    for j in reversed(range(len(arr) - count)):  # mb not -1?
        if arr[j] == 0:
            arr[j + count] = arr[j]
            count -= 1
            arr[j + count] = arr[j]
        else:
            arr[j + count] = arr[j]


if __name__ == '__main__':
    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    # [1,2,3]
    # [8,5,0,9,0,3,4,7]
    duplicateZeros(arr)
