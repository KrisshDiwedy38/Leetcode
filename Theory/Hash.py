"""
Basic Hash/Map/Set Operations:
- Insert key-value pair
- Update value by key
- Retrieve value by key
- Delete key
- Check if key exists
- Get all keys, values, items
- Clear map
- Get size of map
- Check if empty
- Copy map
- Remove item using pop(key)
- Use get(key, default)
- Use setdefault()

Set-specific Operations:
- Add element
- Remove element
- Discard element (safe remove)
- Pop arbitrary element
- Check membership
- Union
- Intersection
- Difference
- Symmetric difference
- Subset/Superset check

Advanced Hash/Map/Set Operations:
- Frequency counter
- Grouping items (e.g., anagrams)
- Invert dictionary
- Merge dictionaries
- Custom hash table with chaining
- Key with max/min value
- Word count using Counter
"""

from collections import defaultdict, Counter, OrderedDict

def freq_counter(arr):
   freq = {}
   for num in arr:
      freq[num] = freq.get(num, 0)+ 1
   return freq

def remove_dupli(arr):
   return set(arr)

def are_anagrams(arr1,arr2):
   return Counter(arr1) == Counter(arr2)



if __name__ == "__main__":
   arr = [1,3,4,13,57,23,4,2,1,23,1,23,1]
   print(remove_dupli(sorted(arr)))