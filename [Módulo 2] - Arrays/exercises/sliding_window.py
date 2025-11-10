# Given an integer array nums and an integer k, 
# return true if there are two distinct indices i 
# and j in the array such that nums[i] == nums[j] 
# and abs(i - j) <= k.

# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true

# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true

# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

def contains_near_by_duplicate(list_nums: list[int], k: int) -> bool:
    # coloca aqui quem já foi "visto"
    last_seen = {}

    for i, num in enumerate(list_nums):
        # se o numero já foi visto
        # e se a subtração dos idxs forem menores do que k
        # então retorna True
        if num in last_seen and (i - last_seen[num]) <= k:
            return True
        # caso contrario coloca o numero visto no hashmap
        last_seen[num] = i
    # se não encontrar o valor desejado retorna false
    return False
