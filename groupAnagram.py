def groupAnagram(input):
   store = {}

   for i in input:
      key = "".join(sorted(i))
      if key in store:
         store[key].append(i)
      else:
         store[key] = []
         store[key].append(i)

   return(list(store.values()))

input = ["bat", "tam", "mat", 'eat','ate','tea']
print(groupAnagram(input))