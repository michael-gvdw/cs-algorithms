
# Array
class Array(object):
    def __init__(self, array=[]):
        self.array = array

    # add an item at the end
    def push(self, item):
        return self.array.append(item)
    
    # remove an item at index 0
    def pop(self, index=-1):
        return self.array.pop(index=index)

# Queue FIFO
class Queue(Array):
    
    # remove an item at index 0
    def pop(self):
        return self.array.pop(index=0)

# Stack LIFO
class Stack(Array):
    # remove an item at index -1
    def pop(self):
        return self.array.pop(index=-1)