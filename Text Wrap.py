
def wrap(s, m):
    s = list(s)
    count = m
    for i in range(len(s)):
        if s[i] != s[len(s)-1]:
            s.insert(m, '\n')
            m += count+1
        else:
            break

    s = ''.join(s)

    return s


s = input()
m = int(input())

print(wrap(s, m))
