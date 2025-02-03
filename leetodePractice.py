class MinStack(object):

   def __init__(self):
      self.stack = []
      

   def push(self, val):
      """
      :type val: int
      :rtype: None
      """
      self.stack.append(val)

   def pop(self):
      """
      :rtype: None
      """
      self.stack.pop(-1)

   def top(self):
      """
      :rtype: int
      """
      return self.stack[-1]  

   def fullStack(self):
      return self.stack

   def getMin(self):
      """
      :rtype: int
      """
      return min(self.stack)
      

obj = MinStack()
obj.push(2)
obj.push(0)
obj.push(3)
obj.push(0)
print(obj.fullStack())
print(obj.getMin())
obj.pop()
print(obj.fullStack())
print(obj.getMin())
obj.pop()
print(obj.fullStack())
print(obj.getMin())
obj.pop()
print(obj.fullStack())
print(obj.getMin())