from typing import List


def search(nums: List[int], target: int) -> int:
    l_index = 0
    r_index = len(nums) - 1
    t_index = -1
    if r_index == 0:
        if nums[0] == target:
            return 0
        return t_index
    while l_index <= r_index:
        t_index = (l_index + r_index) // 2
        if nums[t_index] == target:
            return t_index
        if nums[t_index] > target:
            r_index = t_index - 1
        else:
            l_index = t_index + 1
    return -1


if __name__ == '__main__':
    arr = [2, 5]
    print(search(arr, 5))
