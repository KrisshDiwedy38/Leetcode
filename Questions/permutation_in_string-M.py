def perm(str1, str2):
   str1 = sorted(str1)

   start = str1[0]
   end = len(str1)

   for i in range(len(str2)-1):
      if str2[i] == start:
         print(f"str2 : {str2[i:end]}")
         print(f"str1: {str1}")
         return str2[i:end] == str1
   
print(perm("ab","eidefbeaed"))