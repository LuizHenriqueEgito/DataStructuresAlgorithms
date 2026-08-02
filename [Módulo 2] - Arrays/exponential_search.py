def binary_search(nums: int, n: int, l, r) -> int:
    while l < r:
        mid = int((l + r) / 2)
        if nums[mid] == n:
            return mid
        elif nums[mid] < n:
            l = mid + 1
        else:
            r = mid
    return -1


def exponential_search(array: list[int], target: int) -> int:
    if array[0] == target:
        return 0
    n = len(array)
    i = 1
    while i < n and array[i] < target:
        i *= 2
    if array[i] == target:
        return i
    l = i // 2
    r = min(i, n - 1)
    return binary_search(array, target, l, r)

if __name__ == '__main__':
    array = list(range(1, 40, 1))
    print(array)
    target = 32
    print(exponential_search(array, target))