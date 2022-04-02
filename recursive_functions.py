from typing import List


def recursive_sum_of_arr_elements(arr: List[int], n: int) -> int:
    if n <= 0:
        return 0

    return recursive_sum_of_arr_elements(arr, n - 1) + arr[n - 1]


def sum_of_arr_elements(arr: List[int], n: int) -> int:
    result = 0

    for el in arr:
        result += el

    return result


print(recursive_sum_of_arr_elements([1, 2, 3, 4], 4))
print(sum_of_arr_elements([1, 2, 3, 4], 4))
