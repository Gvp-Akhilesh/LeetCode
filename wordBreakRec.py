__author__ = 'KH9057'

#Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

#For example, given
#s = "leetcode",
#dict = ["leet", "code"].

#Return true because "leetcode" can be segmented as "leet code".

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        print self.myFun(s,dict,0,len(s))

    def myFun(self,s,dict,index,n):
        if(index == n):
            return True
        for i in range(index,n+1,1):
            if(s[index : i] in dict and self.myFun(s,dict,i,n)):
                return True
        return False


sol = Solution()
print sol.wordBreak("abcd",["a","abc","b","cd","leet"])