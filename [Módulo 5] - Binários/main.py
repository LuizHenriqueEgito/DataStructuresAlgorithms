# Binarion:
'''
Dada uma sequência de números fale qual falta para
fechar a sequencia, por exemplo: [0, 1, 3] falta o 2.
'''

def missing_number(nums: list[int]) -> int:
    x = 0
    for num in nums:
        x ^= num
    for i in range(len(nums) + 1):
        x ^= i
    return x

print(missing_number([0, 1, 3]))
print(missing_number([0, 1, 2, 3, 5]))

"""
Dado um numero, retorne o numero de etapas necessarias
para reduzir ele para 0
"""
def number_of_steps(n: int) -> int:
    steps = 0
    while n > 0:
        if n & 1:
            n -= 1
        else:
            n >>= 1
        steps += 1
    return steps

print(number_of_steps(14))
        