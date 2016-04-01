

class Stack:

    def __init__(self):
        self.items = []
    # push
    def push(self, item):
        self.items.append(item)
    # pop
    def pop(self):
        return self.items.pop()
    # peek
    def peek(self):
        return self.items[len(self.items) - 1]
    # size
    def size(self):
        return len(self.items)
    # is empty
    def is_Empty(self):
        # more simplified version
        return self.items == []

        # if len(self.items) == 0:
        #     return True
        # return False


# Write a function revstring(mystr) that uses a stack to reverse the characters in a string.

def revstring(mystr):
    s = Stack()
    rev_str = ""
    for char in mystr:
        s.push(char)
    while not s.is_Empty():
    # while s.size() > 0:
        rev_str = rev_str + s.pop()

    return rev_str

print revstring("apple")
print revstring("banana")
