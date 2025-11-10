def maximum_length_substring(string: str) -> str:
    l, r = 0, 0
    max_ = 1
    counter = {}
    # inicializa o countes
    counter[string[0]] = 1
    while r < len(string) - 1:
        r += 1
        if counter.get(string[r]):
            counter[string[r]] += 1
        else:
            counter[string[r]] = 1
        while counter[string[r]] == 3:
            counter[string[l]] -= 1
            l += 1
        # r - l + 1: pega o tamanho da sequencia acrescenta 1 pois o indice começa em 0 então é preciso corrigir
        max_ = max(max_, r - l + 1)
    return max_

if __name__ == '__main__':
    string = ['b', 'c', 'b', 'b', 'b', 'c', 'b', 'a']
    print(maximum_length_substring(string))