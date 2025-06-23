input = [10,5,10,15,10,5]

store = {}

for i in input:
   if i in store:
      store[i]+=1
   else:
      store[i] = 1

maxi = max(store.values())
mini = min(store.values())
for i in store:
   if store[i] == maxi:
      print(i)
   elif store[i] == mini:
      print(i)