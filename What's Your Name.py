def print_full_name(first, last):
    full_name = first+' '+''.join(last)
    print(f'Hello {full_name}! You just delved into python.')


first_name = input()
last_name = input()
print_full_name(first_name, last_name)
