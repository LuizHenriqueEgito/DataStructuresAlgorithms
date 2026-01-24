def bubble_sort(nums: list[int]) -> list[int]:
    size = len(nums)
    for _ in nums:
        is_sorted = True
        print(f'{nums=}')
        for i in range(size - 1):
            if nums[i] > nums[i + 1]:
                is_sorted = False
                nums[i + 1], nums[i] = nums[i], nums[i + 1]
        if is_sorted:
            break
bubble_sort([5, 4, 3, 2, 1])
bubble_sort([11, 22, 33, 44, 55])