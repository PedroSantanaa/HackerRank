
s = input()
try:
    new_s = int(s)
    print(new_s)
except (TypeError, ValueError):
    print('Bad String')
