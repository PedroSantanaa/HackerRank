n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

for k, v in student_marks.items():
    if k == query_name:
        average = sum(v)/len(v)
        print(f'{average:.2f}')
