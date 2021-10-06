class stack_queue:

    class Node:
        def __init__(self, data, _next):
            self.data = data
            self._next = _next

    # Write your code here

    def __init__(self):
        self.heads = None
        self.headq = None
        self.tail = None
        self.size1 = 0
        self.size2 = 0

    def is_empty1(self):
        return self.size1 == 0

    def is_empty2(self):
        return self.size2 == 0

    def pushCharacter(self, ps):
        self.heads = self.Node(ps, self.heads)
        self.size1 += 1

    def enqueueCharacter(self, ps):
        new = self.Node(ps, None)
        if self.is_empty2():
            self.headq = new
        else:
            self.tail._next = new
        self.tail = new
        self.size2 += 1

    def popCharacter(self):
        result1 = self.heads.data
        self.heads = self.heads._next
        self.size1 -= 1
        return result1

    def dequeueCharacter(self):
        result2 = self.headq.data
        self.headq = self.headq._next
        self.size2 -= 1
        if self.is_empty2():
            self.tail = None
        return result2


# read the string s
s = input()


# Create the Solution class object
obj = stack_queue()

lg = len(s)
# push/enqueue all the characters of string s to stack
for i in range(lg):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(lg // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")
