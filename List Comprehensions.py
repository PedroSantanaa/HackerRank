x, y, z, n = (int(input()) for i in range(4))
sequence = [[a, b, c] for a in range(x+1)
            for b in range(y+1) for c in range(z+1) if sum([a, b, c]) != n]
print(sequence)
