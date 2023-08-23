
class Stack(object):
    def __init__(self):
        self.item = []
        
    def isEmpty(self):
        return self.item == []
        
    def push(self,item):
        value = self.item.append(item)

    def pop(self):
        self.item.pop()
        
    def peek(self):
        return self.item[len(self.item)-1]
    
    def size(self):
        return len(self.item)
        
obj1 = Stack()
print(type(obj1))
print(obj1.isEmpty())
print(obj1.push(3))
print(obj1.push("Nimish"))
print(obj1.peek())

print(obj1.isEmpty())
print(obj1.size())
print(obj1.pop())

print(obj1.size())





class Queue(object):
    
    def __init__(self):
        self.item = []
        
    def enqueue(self,item):
        return self.item.insert(0,item)
    
    def dequeue(self):
        return self.item.pop()
        
    def size(self):
        return len(self.item)
    
    def isEmpty(self):
        return self.item == []
        
obj2 = Queue()
print("In")
print(obj2.isEmpty())
print(obj2.enqueue("Nimish"))
print(obj2.isEmpty())
print(obj2.size())
print(obj2.dequeue())
print(obj2.enqueue("coolboy"))

print(obj2.size())

