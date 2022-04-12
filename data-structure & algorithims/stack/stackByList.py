class Stack:
    def __init__(self,maxSize):
        self.list = [];
        self.maxSize = maxSize
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    def push(self,value):
        self.list.append(value)
        return  'The element is added successfully'
    def pop(self):
        if self.isEmpty():
            return 'The stack is empty'
        else:
            return self.list.pop()
    def peek(self):
        if self.isEmpty():
            return 'the list is empty'
        else:
            return self.list[len(self.list)-1]
    def delete(self):
        self.list = None;
    def isFull(self):
        if len(self.list) == self.maxSize:
            return 'The stack is full'
        else:
            return False

    def push(self,value):
        if self.isFull():
            return 'The stack is full'
        else:
            self.list.append(value)
            return 'The item is added suceesfully'


# s = Stack()
# s.push(23)
# s.push(34)
# s.push(3335)
# print(s.pop())
# print('----------------')
# print(s)
# print("--------")
# print(s.peek() )
customStack = Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(12)
customStack.push(1223)
customStack.push(467)
customStack.push(334)
customStack.push(222)
customStack.push(1234)
print(customStack)