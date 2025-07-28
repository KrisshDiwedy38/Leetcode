"""
Singly Linked List Operations 

Basic Operations:

Insert at beginning
Insert at end
Insert at specific position
Delete from beginning
Delete from end
Delete at specific position
Delete by value
Search/Find element
Traverse/Display
Get size/length
Check if empty

Advanced Operations:

Reverse the list
Find middle element
Detect cycle
Remove duplicates
Merge two sorted lists
Split list at position
Find nth node from end
Check if palindrome
Sort the list
Clone/Copy list

"""

# Singly Linked List Node
class SLL_Node:
   def __init__(self, val):
      self.val = val
      self.next = None

   def __str__(self):
      return str(self.val)
   
# Singly Linked List Functions
class SinglyLinkedList:
   def __init__(self):
      self.head = None
      self.size = 0

   def insert_at_start(self,val):
      newNode = SLL_Node(val) 
      newNode.next = self.head
      self.head = newNode
      self.size += 1
      return
   
   def insert_at_end(self,val):
      newNode = SLL_Node(val) 
      curr = self.head
      while curr.next:
         curr = curr.next
      curr.next = newNode
      self.size += 1
      return

   def insert_at_any(self,val,posn):
      newNode = SLL_Node(val)
      if posn >= self.size:
         self.insert_at_end(val)
      pointer = 0
      curr = self.head
      while pointer < posn-1:
         curr = curr.next
         pointer += 1
      
      temp_next = curr.next
      curr.next = newNode
      newNode.next = temp_next

      self.size += 1
      return

   def delete_at_end(self):
      curr = self.head
      while curr.next.next:
         curr = curr.next

      del curr.next
      curr.next = None
      return
      
      
   def delete_at_any(self,posn):
      if posn >= self.size:
         self.delete_at_end()
         return
      pointer = 0
      curr = self.head
      while pointer < posn-1:
         curr = curr.next
         pointer += 1
      
      temp = curr.next.next
      del curr.next
      curr.next = temp
      return

   def search_n_empty(self,val):
      if not self.head:
         return f"No List"
      curr = self.head
      posn = 0
      while curr:
         if curr.val == val:
            print(f"Element exists at {posn}")
            return
         curr = curr.next
         posn += 1
      
      print(f"Element does not exist")
      return

   def display_list(self):
      curr = self.head
      elements = []
      while curr:
         elements.append(curr)
         curr = curr.next
      result = " -> ".join(str(i) for i in elements)
      print(result)
      return
   
   def display_rev_list(self):
      pass
      

"""
Doubly Linked List Operations

Basic Operations:

Insert at beginning
Insert at end
Insert at specific position
Insert before a node
Insert after a node
Delete from beginning
Delete from end
Delete at specific position
Delete by value
Delete a specific node
Search/Find element
Forward traversal
Backward traversal
Get size/length
Check if empty

Advanced Operations:

Reverse the list
Find middle element
Remove duplicates
Merge two sorted lists
Split list at position
Find nth node from end
Find nth node from beginning
Check if palindrome
Sort the list
Clone/Copy list
Find pairs with given sum
Rotate list by k positions
Convert to circular doubly linked list
"""

# Doubly Linked List Node
class D_Node:
   def __init__(self, val):
      self.val = val
      self.next = None
      self.prev = None
   
   def __str__(self):
      return str(self.val)
   

if __name__ == "__main__":
   listt = SinglyLinkedList()
   listt.insert_at_start(10)
   listt.insert_at_start(11)
   listt.insert_at_start(12)
   listt.insert_at_start(13)
   listt.insert_at_end(9)
   listt.insert_at_any(5,2)
   listt.display_list()
   listt.search_n_empty(5)
   listt.delete_at_any(10)
   listt.display_list()
   