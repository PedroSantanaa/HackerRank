def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    counts = 0
    countk = 0
    for i in range(len(string)):
        if s[i] in vowels:
            countk += len(string)-i
        else:
            counts += len(string)-i

    if counts > countk:
        print(f'Stuart {counts}')
    elif countk > counts:
        print(f'Kevin {countk}')
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
