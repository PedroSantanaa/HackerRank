for _ in range(int(input())):
    s = input()
    for i in range(0, len(s), 2):
        print(s[i], end='')
    print(end=' ')
    for i in range(1, len(s), 2):
        print(s[i], end='')
    print(end='\n')

# another solution
'''
for i in range(int(input())):
    s = input()
    print(s[::2], s[1::2])'''
