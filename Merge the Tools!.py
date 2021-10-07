from collections import OrderedDict


def merge_the_tools(string, k):
    # your code goes here

    for x in range(0, len(string), k):
        s = list(OrderedDict.fromkeys(string[x:x+k]))
        s = ''.join(s)
        print(s)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
