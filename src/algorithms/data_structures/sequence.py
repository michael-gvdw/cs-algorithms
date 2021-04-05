
# Array
class Array(object):
    def __init__(self, array=[]):
        self.array = array

    def is_empty(self):
        return len(self.array) == 0

    # add an item at the end
    def push(self, item):
        return self.array.append(item)
    
    # remove an item at index 0
    def pop(self, index=-1):
        if not self.is_empty():
            return self.array.pop(index)

    def peek(self, index):
        if not self.is_empty():
            return self.array[index]


    def __len__(self):
        return self._size()
    
    def _size(self):
        return len(self.array)
    

# Queue FIFO
class Queue(Array):
    
    # remove an item at index 0
    def enqueue(self, item):
        self.push(item)

    
    def dequeue(self):
         if not self.is_empty():
            return self.array.pop(0)

    def peek(self):
        if not self.is_empty():
            return self.array[0]



# Stack LIFO
class Stack(Array):

    # remove an item at index -1
    def pop(self):
        if not self.is_empty():
            return self.array.pop(-1)
    
    def peek(self):
        if not self.is_empty():
            return self.array[-1]
    