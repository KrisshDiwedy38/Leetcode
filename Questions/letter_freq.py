# aabbbcdddde -> a2b3c1d4e1


stringg = "aabbbcdddde"
store = [0]*26

for i in stringg:
   idx = ord(i) - ord('a')
   store[idx] += 1

result = ""
for i,value in enumerate(store):
   if value != 0:
      char = chr(i + ord('a'))
      result += (char + str(value))

print(result)
