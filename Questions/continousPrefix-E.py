strs = ["cir","car"]

def bleh(strs):
   if len(strs) == 0:
      print("")

   base = strs[0]
   for i in range(len(base)):
      for word in strs[1:]:
            if i == len(word) or word[i] != base[i]:
               return base[0:i]

   return base

bleh(strs)





