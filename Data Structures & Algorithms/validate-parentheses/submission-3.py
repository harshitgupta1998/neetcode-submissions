class Solution:
    def isValid(self, s: str) -> bool:
        t={']':'[','}':'{',')':'('}
        stack=[]
        for i in range(len(s)):
            if s[i] not in t:
                stack.append(s[i])
            elif stack and stack[-1]==t[s[i]]:
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True
