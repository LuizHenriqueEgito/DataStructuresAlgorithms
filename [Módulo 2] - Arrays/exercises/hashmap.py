# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

def two_sum(list_nums: list[int], target: int) -> list[int]:
    num_hash = {}  # crio o hashmap
    for i, num in enumerate(list_nums):  # passo em cada elemento da lista
        delta = target - num  # vejo quem falta para chegar ao target
        if num in num_hash:  # vejo se quem falta está no hashmap
            return [num_hash[delta], i]  # se existir concluimos
        # se não existir salvamos como chave e seu index
        num_hash[delta] = i  # isso faz com que o algoritmo seja otimizado
    return []