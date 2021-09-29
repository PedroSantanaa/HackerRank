def swap_case(s):
    s = list(s)
    for x in range(len(s)):
        if s[x].isupper():
            s[x] = s[x].lower()
        else:
            s[x] = s[x].upper()
    s_new = ''.join(s)
    return s_new


print(swap_case(input()))
