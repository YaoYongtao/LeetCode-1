# Time:  O(n + m)
# Space: O(m)
#
# Implement strStr().
# 
# Returns a pointer to the first occurrence of needle in haystack,
#  or null if needle is not part of haystack.
#

# Wiki of KMP algorithm:
# http://en.wikipedia.org/wiki/Knuth-Morris-Pratt_algorithm
class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        if len(haystack) < len(needle):
            return None
        
        if len(needle) == 0:
            return haystack
        
        i = self.KMP(haystack, needle)
        if i > -1:
            return haystack[i:]
        else:
            return None
    
    def KMP(self, text, pattern):
        prefix = self.getPrefix(pattern)
        j = -1
        for i in range(len(text)):
            while j > -1 and pattern[j + 1] != text[i]:
                j = prefix[j]
            if pattern[j + 1] == text[i]:
                j += 1
            if j == len(pattern) - 1:
                return i - j
        return -1
    
    def getPrefix(self, pattern):
        prefix = [-1] * len(pattern)
        j = - 1
        for i in range(1, len(pattern)):
            while j > -1 and pattern[j + 1] != pattern[i]:
                j = prefix[j]
            if pattern[j + 1] == pattern[i]:
                j += 1
            prefix[i] = j
        return prefix
    
# Time:  (n * m)
# Space: (1)
class Solution2:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return haystack[i:]
        return None
    
if __name__ == "__main__":
    print(Solution().strStr("a", ""))
    print(Solution().strStr("abababcdab", "ababcdx"))
