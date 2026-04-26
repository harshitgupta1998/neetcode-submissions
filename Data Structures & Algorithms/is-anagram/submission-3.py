class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count1={}
        count2={}
        for i in s:
            count1[i]=1+count1.get(i,0)
        for j in t:
            count2[j]=1+count2.get(j,0)
        return count1==count2