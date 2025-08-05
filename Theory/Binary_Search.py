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
            return 0
        elif self.arr[mid] < target:
            left = mid + 1
            return self.recurr_BS(target, left, right)
        else:
            right = mid - 1
            return self.recurr_BS(target, left , right)
        
    def BS_with_posn(self):
        target = int(input("Enter position to be searched: "))

        left , right = 0 , len(self.arr) - 1

        while left <= right:
            mid = left + (right-left) // 2

            if mid == target:
                print(f"Element at {target} : {self.arr[mid]}")
                return 0
            elif mid < target:
                left = mid + 1
            else:
                right = mid - 1
        
        print(f"No element as posn {target}")
        return -1

    def first_occur(self):
        target = int(input("Enter element to be searched: "))
        
        left, right = 0, len(self.arr) -1 

        while left <= right:
            mid = left + (right - left) // 2

            if self.arr[mid] == target:
                print(f"Element first found at {mid}")
                return 0
            elif self.arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        print(f"{target} not found")
        return -1
    
    def last_occur(self):
        target = int(input("Enter element to be searched: "))

        left, right = 0, len(self.arr) - 1

        store = []

        while left <= right:
            mid = left + (right - left) // 2

            if self.arr[mid] == target:
                store.append(mid)
                left += 1
            elif self.arr[mid] < target:
                left = mid + 1
            else:
                right = mid-1
        
        if store:
            print(f"{target} last occurs at index: {store[-1]}")
            return 0
        else:
            print(f"{target} not found")
            return -1

if __name__ == "__main__":
    arr = Binary_Search()
    arr.get_array()
    arr.display_list()
    arr.iterative_BS()
    arr.recurr_BS()
    arr.BS_with_posn()
    arr.first_occur()
    arr.last_occur()


