def binary_search(nums: int, n: int) -> int:
    l = 0
    r = len(nums)
    steps = 0
    while l < r:
        steps += 1
        mid = int((l + r) / 2)
        if nums[mid] == n:
            print(f'{steps=}')
            return mid
        elif nums[mid] < n:
            l = mid + 1
        else:
            r = mid
    return -1  # número não foi encontrado

if __name__ == '__main__':
    array_1 = list(range(1, 6, 1))
    array_1_2x = list(range(1, 11, 1))
    array_1_3x = list(range(1, 21, 1))
    array_1_4x = list(range(1, 41, 1))
    print(array_1)
    print(array_1_2x)
    print(array_1_3x)
    print(array_1_4x)
    print(binary_search(array_1, 3))
    print(binary_search(array_1_2x, 3))
    print(binary_search(array_1_3x, 3))
    print(binary_search(array_1_4x, 3))