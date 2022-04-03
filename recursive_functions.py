from typing import List


def recursive_sum_of_arr_elements(arr: List[int], n: int) -> int:
    if n <= 0:
        return 0

    return recursive_sum_of_arr_elements(arr, n - 1) + arr[n - 1]


def recursive_number_range(start: int, end: int) -> List[int]:
    if end == start:
        return [start]

    result = recursive_number_range(start, end - 1)
    result.append(end)
    return result


def recursive_countdown(n: int) -> List[int]:
    if n < 1:
        return []

    count_array = recursive_countdown(n - 1)
    count_array.insert(0, n)
    return count_array


print(recursive_sum_of_arr_elements([1, 2, 3, 4], 4))
print(recursive_number_range(1, 5))
print(recursive_countdown(5))
