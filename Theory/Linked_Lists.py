# Singly Linked List Node
class S_Node:
   def __init__(self, val, next=None):
      self.val = val
      self.next = next

   def __str__(self):
      return str(self.val)
   
# Singly Linked List Functions



# Doubly Linked List Node
class D_Node:
   def __init__(self, val, next=None, prev=None):
      self.val = val
      self.next = next
      self.prev = prev
   
   def __str__(self):
      return str(self.val)
   

if __name__ == "__main__":
   pass