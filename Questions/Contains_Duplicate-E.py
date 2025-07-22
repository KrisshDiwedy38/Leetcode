#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def containsDuplicate(self, nums: list[int]) -> bool:
   visited = set()
   for i in nums:
      if i in visited:
            return True
      else:
            visited.add(i)
   return False

