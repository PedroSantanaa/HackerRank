def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1

    return count


s = input().lower()
ss = input().lower()
print(count_substring(s, ss))
