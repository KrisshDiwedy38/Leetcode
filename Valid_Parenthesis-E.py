def isvalid(paraString):
   stack = []
   brackets = { ")" : "(", "]" : "[", "}" : "{" } #closing to opening parenthesis

   for para in paraString:
      if para in brackets:
            if stack and stack[-1] == brackets[c]: #If stack is not emply and stack top is the opening parenthesis. Pop
               stack.pop()
            else:
               return False   #If closing parenthesis is encountered without an opening return false
      else:
            stack.append(para)
   
   return True if not stack else False #By end of loop if stack is empty, return true else false

