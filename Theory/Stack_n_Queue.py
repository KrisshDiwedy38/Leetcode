"""
Basic Stack Operations:
- Push element
- Pop element
- Peek/top element
- Check if stack is empty
- Get size of stack
- Traverse stack
- Clear stack

Advanced Stack Operations:
- Balanced parentheses checker
- Evaluate postfix expression
- Evaluate prefix expression
- Infix to postfix conversion
- Implement min stack (O(1) getMin)
- Sort a stack
- Reverse a stack
- Stack using two queues
- N stacks in array
- Largest rectangle in histogram
- Monotonic stack problems
"""
class Stack:
   def __init__(self):
      self.items = []

   def push(self,val):
      self.items.append(val)
   
   def pop(self):
      popped = self.items[-1]
      self.items.remove(popped)
      return popped
   
   def peek(self):
      top = self.items[-1]
      return top
   
   def display_stack(self):
      if self.items:
         result = ' __ '.join(str(i) for i in self.items )
         print(result)
      else:
         print("Empty Stack")

      
   def clear_stack(self):
      while self.items:
         self.items.pop()
      


def stack_main():
   stk = Stack()
   stk.push(10)
   stk.push(13)
   stk.push(12)
   stk.push(11)
   stk.display_stack()
   stk.pop()
   stk.display_stack()
   stk.clear_stack()
   stk.display_stack()
   stk.push(10)
   stk.push(13)
   stk.push(12)
   stk.push(11)
   stk.display_stack()

"""
Basic Queue Operations:
- Enqueue (add to rear)
- Dequeue (remove from front)
- Peek front/rear
- Check if queue is empty
- Get size of queue
- Traverse queue

Advanced Queue Operations:
- Circular queue implementation
- Double-ended queue (deque)
- Priority queue (min/max heap)
- Queue using two stacks
- Reverse a queue
- LRU Cache using deque + map
- Sliding window max using deque
- Rotten oranges (multi-source BFS)
- Generate binary numbers using queue
- Interleave first and second halves
"""

class Queue():
   def __init__(self):
      self.items = []
      self.size = 0

   def enque(self,val):
      self.items.append(val)
      self.size += 1

   def deque(self):
      self.items.pop(0)
      self.size -= 1
   
   def peek_f(self):
      print(self.items[0])
   
   def peek_r(self):
      print(self.items[-1])

   def size(self):
      print(self.size)
   
   def display_queue(self):
      if self.items:
         result = " __ ".join(str(i) for i in self.items)
         print(result)
      else:
         print("Empty Queue")

def queue_main():
   pass

if __name__ == "__main__":
   stack_main()
   queue_main()