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

def insertSort(nums): # Insertion Sorting : Swapping  TC - O(n2) SC - O(1) 
   for i in range(1, len(nums)): # O(n)
      for j in range(i,0,-1): #O(n)
         if nums[j] < nums[j-1]:
            swap(nums,j,j-1)
   return nums

def insertion_sort(nums): # Insertion Sorting : Shifting TC - O(n2) SC - O(1)
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums

def mergeSort(nums): # TC - O(n log n) SC - O(n)
   high = len(nums) - 1
   low = 0
   mergeSortDivide(nums,low,high)
   return nums

def mergeSortDivide(arr, low, high): 
	if low >= high:
		return
	mid = (low + high) // 2
	mergeSortDivide(arr, low, mid) # TC - O(log n)
	mergeSortDivide(arr,mid+1,high) # TC - O(log n)
	merge(arr, low, mid, high) # TC - O(n) 

def merge(arr, low, mid, high):
   temp = [] # SC - O(n) - New Array
   left = low
   right = mid + 1
   
   while left <= mid and right <= high: # TC - O(n)
      if arr[left] <= arr[right]:
         temp.append(arr[left])
         left += 1 
      else:
         temp.append(arr[right])
         right += 1

   temp.extend(arr[left:mid+1])
   temp.extend(arr[right:high+1])

   arr[low:high+1] = temp

def quickSort(nums: list[int]) -> list[int]:
   high = len(nums)-1
   low = 0
   quickSorting(nums,low,high)
   return nums

def quickSorting(arr,low,high): # TC - O(n log n) SC - O(n)
   if low < high:
      pivot_index = partition(arr,low,high) # TC - O(n) SC - O(n)
      quickSorting(arr, low, pivot_index-1)  # O(log n)
      quickSorting(arr, pivot_index+1, high) # O(log n)
   
def partition(arr,low,high): 
   pivot = arr[high] # SC - O(n)
   i = low - 1

   for j in range(low,high): # TC - O(n)
      if arr[j] <= pivot:
         i += 1
         arr[i] , arr[j] = arr[j], arr[i]

   arr[i+1], arr[high] = arr[high], arr[i+1]
   return i + 1


if __name__ == "__main__":
   # user_input = input("Enter a list of numbers seperated by space: ")
   # nums = list(map(int, user_input.split()))

   nums = [34,32,27,24,19,21,15,10,8,5,2,1]
   print(quickSort(nums))