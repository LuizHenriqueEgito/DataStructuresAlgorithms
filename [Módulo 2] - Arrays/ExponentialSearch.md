# Exponential Search
Usa binary search como parte da busca, tem complexidade temporal $O(\log n)$ e espacial $O(1)$. Ela dobra a busca a cada iteração, isso porque talvez o valor buscado pode aparecer "cedo" e você não precisaria buscar por todo array como numa binary search, a exponential search sai do primeiro número e vai dobrando até englobar o valor encontrado e depois utiliza a binary search para chegar ao valor.
![ExponentialSearch](images/ExponentialSearch.jpg)
```python
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

def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    n = len(arr)
    i = 1
    while i < n and arr[i] < target:
        i *= 2
    if arr[i] == target:
        return 1
    return binary_search(arr, target, 1 // 2, min(i, n - 1))

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
```