# Time:  O(n)
# Space: O(1)
#
# Compare two version numbers version1 and version1.
# If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
#
# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.
#
# Here is an example of version numbers ordering:
#
# 0.1 < 1.1 < 1.2 < 13.37
#

# Time:  O(n)
# Space: O(n), this could be enhanced to O(1) by better but trivial string parsing
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a boolean
    def compareVersion(self, version1, version2):
        v1, v2 = version1.split("."), version2.split(".")

        if len(v1) > len(v2):
            v2 += ['0' for _ in range(len(v1) - len(v2))]
        elif len(v1) < len(v2):
            v1 += ['0' for _ in range(len(v2) - len(v1))]

        i = 0
        while i < len(v1):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
            else:
                i += 1

        return 0

if __name__ == "__main__":
    print(Solution().compareVersion("21.0", "121.1.0"))
    print(Solution().compareVersion("01", "1"))
    print(Solution().compareVersion("1", "1.0"))