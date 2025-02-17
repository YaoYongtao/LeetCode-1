# Time:  O(logn)
# Space: O(1)
#
# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
# 
# For example:
# 
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 
#

class Solution:
    # @return a string
    def convertToTitle(self, num):
        result, dvd = "", num
        
        while dvd:
            result += chr((dvd - 1) % 26 + ord('A'))
            dvd = (dvd - 1) / 26
        
        return result[::-1]
        
if __name__ == "__main__":
    for i in range(1, 29):
        print(Solution().convertToTitle(i))