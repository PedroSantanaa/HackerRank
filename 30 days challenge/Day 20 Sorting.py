if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    swaps = 0
    for i in range(n):

        for x in range(n-1):
            if (a[x] > a[x+1]):
                a[x], a[x+1] = a[x+1], a[x]
                swaps += 1
        if swaps == 0:
            break

print(f'Array is sorted in {swaps} swaps.')
print(f'First Element: {a[0]}')
print(f'Last Element: {a[-1]}')
