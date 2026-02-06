def isPalindrome(s):
   s = s.replace(" ", "")
   if s == "":
      return True
   print(s)
   pali = True
   l = 0 
   r = len(s)-1
   while l <= r:
      if not s[l].isalnum():
            l += 1
      if not s[r].isalnum():
            r -= 1
      elif s[r].lower() != s[l].lower():
            pali = False
            break
      else:
            r -= 1
            l += 1
   return pali

print(isPalindrome("Marge, let's \"[went].\" I await {news} telegram."))


