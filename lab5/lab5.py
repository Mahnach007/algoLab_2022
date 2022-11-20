d = 256
new_list = []


def rabin_karp_algorithm(pattern, text, prime_number=13):
    M = len(pattern)
    N = len(text)
    i = 0
    j = 0
    p = 0  # hash value for pattern
    t = 0  # hash value for txt
    h = 1

    for i in range(M-1):
        h = (h*d) % prime_number

    for i in range(M):
        p = (d*p + ord(pattern[i])) % prime_number
        t = (d*t + ord(text[i])) % prime_number

    for i in range(N-M+1):
        if p == t:
            for j in range(M):
                if text[i+j] != pattern[j]:
                    break
                else:
                    j += 1


        if j == M:
            return [i]

    if i < N-M:
        t = (d*(t-ord(text[i])*h) + ord(text[i+M])) % prime_number

        if t < 0:
            t = t+prime_number


if __name__ == '__main__':
    txt = "Lorem ipsum dolor sit amet, adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    pat = "sit"

    result = rabin_karp_algorithm(pat, txt)
    print(result)
