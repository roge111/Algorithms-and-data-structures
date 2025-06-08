class Solution(object):
    def longestPalindrome(self, s):
        dp = [[False] *len(s) for _ in range(len(s))]
        start = 0
        max_len = 0
        for i in range(len(s)):
            start = i
            max_len = 1
            dp[i][i] = True
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                max_len = 2
            
        for l in range(3, len(s)+1):
            for i in range(len(s) - l + 1):
                j = i + l -1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if l > max_len:
                        max_len = l
                        start = i
        return s[start:start+max_len]


                         
        
