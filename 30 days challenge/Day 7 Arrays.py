n = int(input().strip())
array = list(map(int, input().rstrip().split()))
array.reverse()
for x in array:
    print(x, end=' ')

'''one liner
print(" ".join(map(str, arr[::-1])))'''
