
#even
"abba"

#odd
"ybbaiabbx"
"baiab"

#mixed
"aiabba"

def longestPalindrome(s):
    
    longest_pad = ""
    longest_pad_len = 0
    
    #iter through each char in s
    for i in range(len(s)):
        
        l, r = i, i
        
        #odd: initiate L = R = i, increment window outwards L--, R+ ; Condition while L>=0 and R<= len(s)-1
        while l >= 0 and r < len(s) and s[l] == s[r]: # palindrome identified
            padlindrome = s[l:r+1]
            
            # Check palindrome: if s[L] == s[r] and compared len of longest
            if len(padlindrome) > longest_pad_len:
                longest_pad_len = len(padlindrome)
                longest_pad = padlindrome
        
            l -=1
            r +=1
        
    
        l, r = i, i+1
        #even: initiate L = i , R = i+1, 
        while l >= 0 and r < len(s) and s[l] == s[r]: # palindrome identified
            padlindrome = s[l:r+1]
            
            # Check palindrome: if s[L] == s[r] and compared len of longest
            if len(padlindrome) > longest_pad_len:
                longest_pad_len = len(padlindrome)
                longest_pad = padlindrome
        
            l -=1
            r +=1
            # Check palindrome and compared len of longest
    

    
    return longest_pad


print(longestPalindrome("cbbd"))

from collections import Counter
nums = [-5, -5, 1, 2, 3, 3, 4]
print(Counter(nums))

       



def getFinalString(s):
    l, r = 0, 2
    while r<len(s):
        if s[l:r+1] == "AWS":
            sub_string = s[0:l] + s[r+1:]
            l, r = 0, 2
            s = sub_string
            continue
            
        l+=1
        r+=1
    
    return s if len(s) != 0 else "-1"


print(getFinalString("AAWSWS"))