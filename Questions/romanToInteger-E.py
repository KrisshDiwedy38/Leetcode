def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """    
    roman = { 'I' : 1 , 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000 }
    ans = 0
    for i in range(len(s)):
        if i > 0 and  roman[s[i]] > roman[s[i - 1]]:
            print(ans)
            ans += roman[s[i]] -  2 * roman[s[i - 1]]
            print(ans)
        else:
            ans += roman[s[i]]
    return(ans)
        

print(romanToInt('MCMXCIV'))
