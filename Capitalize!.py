def solve(s):
    new_s = s.split(' ')
    new_s = ' '.join(word.capitalize() for word in new_s)
    return new_s


if __name__ == '__main__':

    s = input()

    result = solve(s)
    print(result)
