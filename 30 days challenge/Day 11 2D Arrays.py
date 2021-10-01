

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
high = []

for l in range(4):
    for c in range(1, 5):
        sum = arr[l][c-1]+arr[l][c]+arr[l][c+1]+arr[l+1][c] + \
            arr[l+2][c-1]+arr[l+2][c]+arr[l+2][c+1]
        high.append(sum)
print(max(high))

'''res = []

for x in range(0, 4):
    for y in range(0, 4):
        s = sum(arr[x][y:y+3]) + arr[x+1][y+1] + sum(arr[x+2][y:y+3])
        res.append(s)

print(max(res))'''
