"""
Basic Binary Search Operations:
- Standard binary search
- Find first occurrence
- Find last occurrence
- Element existence check
- Insert position of element

Advanced Binary Search Applications:
- Search in rotated sorted array
- Find peak in mountain array
- Find square root (integer)
- Kth smallest/largest element
- Median of two sorted arrays
- Search in 2D matrix
- Count frequency of element
- Binary search on answer pattern:
    - Min pages/book allocation
    - Painters partition problem
    - Split array largest sum
    - Aggressive cows
    - Shipping packages within D days
"""


class Binary_Search():
    def __init__(self):
        self.arr = []

    def get_array(self):
        user_input = input("Enter a list of numbers seperated by space: ")
        self.arr = list(map(int, user_input.split()))

    def display_list(self):
        result = " -> ".join(str(i) for i in self.arr)
        print(result)
    
    def iterative_BS(self):
        target = int(input("Enter element to be searched: "))

        left, right = 0, len(self.arr) - 1 

        while left <= right:
            mid = left + (right - left) // 2

            if self.arr[mid] == target:
                print(f"{target} found at {mid}")
                return
            elif self.arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        print("Element not found")
        return -1 
    
    def recurr_BS(self, target = None, left = 0, right = None):
        if right is None: 
            target = int(input("Enter element to be searched: "))
            right = len(self.arr) - 1

        if left > right: 
            return -1
        
        mid = left + (right - left) // 2

        if self.arr[mid] == target:
            print(f"{target} found at {mid}")
            return
        elif self.arr[mid] < target:
            left = mid + 1
            return self.recurr_BS(target, left, right)
        else:
            right = mid - 1
            return self.recurr_BS(target, left , right)
        

if __name__ == "__main__":
    arr = Binary_Search()
    arr.get_array()
    arr.display_list()
    arr.iterative_BS()
    arr.recurr_BS()

