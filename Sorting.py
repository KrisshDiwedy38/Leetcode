def swap(nums,first,second):
   nums[first], nums[second] = nums[second] , nums[first]

def selectSort(nums): # Selection Sorting TC- O(n2) SC - O(1) 
   for i in range(len(nums)): # O(n)
      pos = i
      for j in range(i + 1, len(nums)): # O(n)
         if nums[j] < nums[pos]:
            pos = j
      if pos != i:
         swap(nums,i,pos)
   return nums

def bubbleSort(nums): # Bubble Sorting TC- O(n2) SC - O(1) 
   for i in range(len(nums)): # O(n)
      swapped = False
      for j in range(len(nums)-1): # O(n-1)
         if nums[j] > nums[j+1]:
            swap(nums,j,j+1)
            swapped = True
      if not swapped: 
         break
   return nums

def insertSort(nums): # Insertion Sorting  TC - O(n2) SC - O(1) 
   for i in range(1, len(nums)): # O(n)
      for j in range(i,0,-1): #O(i * n)
         if nums[j] < nums[j-1]:
            swap(nums,j,j-1)
   return nums

if __name__ == "__main__":
   # user_input = input("Enter a list of numbers seperated by space: ")
   # nums = list(map(int, user_input.split()))

   nums = [34,32,27,24,19,21,15,10,8,5,2,1]
   print(insertSort(nums))