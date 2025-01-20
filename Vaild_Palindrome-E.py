def isPalindrome(s):
   if s == "":
      return True
   new_string = "".join(letters for letters in s if letters.isalnum())
   return new_string.lower() == new_string.lower()[::-1]

