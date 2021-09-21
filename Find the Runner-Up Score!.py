n = int(input())
score = map(int, input().split())

scores = []
for i in score:
    if i not in scores:
        scores.append(i)

scores = sorted(scores)
scores.pop()
print(max(scores))
