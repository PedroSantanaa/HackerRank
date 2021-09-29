n = int(input().strip())
nb = bin(n)

nb = nb[2:].split('0')
print(len(max(nb)))
