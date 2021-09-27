n = int(input())
phone_book = {}

for _ in range(n):
    name, phone = input().split()
    phone_book[name] = phone


# Query names unknown
while(1):
    try:
        query_name = input()
        if query_name in phone_book:
            print(f'{query_name}={phone_book[query_name]}')
        else:
            print('Not found')
    except EOFError:
        break
