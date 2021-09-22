scores = []
for _ in range(int(input())):
    scores.append([input(), float(input())])

scores = sorted(scores)
second_high = sorted(set([score for name, score in scores]))[1]

names = [name for name, score in scores if score == second_high]

for name in names:
    print(name)
