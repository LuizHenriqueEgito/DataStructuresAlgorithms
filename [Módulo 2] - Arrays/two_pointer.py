# Reverse words in a String
# input: 'Mr Ding'
# output: 'rM gniD'
def reverse_words(string: str) -> str:  # O(n) both
    res = ''
    l, r = 0, 0  # pointers
    while r < len(string):
        if string[r] != ' ':
            r += 1
        else:
            res += string[l:r + 1][::-1]
            r += 1
            l = r
    # Aqui ele está na ultima letra e não cai mais dentro do else
    res += ' '
    res += string[l:][::-1]
    return res[1:]

if __name__ == '__main__':
    string = 'Mr Doing'
    print(reverse_words(string))
