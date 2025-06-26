def topKFrequent(nums, k):
   
   store = {}

   for i in nums:
      if i in store:
         store[i] += 1
      else:
         store[i] = 1
   
   sortedDict = dict(sorted(store.items(), key = lambda item : item[1]))
   return (sorted(list(sortedDict.keys())[-1:-k-1:-1]))

topKFrequent([1],2)
