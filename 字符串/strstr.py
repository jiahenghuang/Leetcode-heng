class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #return haystack.find(needle)
        if not needle:return -1
        if not haystack:return -1 
        i,j = 0,0
        length = len(haystack)

        while i < length and j < length:
            if haystack[i]==needle[0]:
                j = i
                flag=True
                for k in needle:
                    if haystack[j] != k:        
                        flag=False
                        break
                    j += 1
                if flag:
                    return i
                else:
                    i += 1
                    j = i
            else:
                i += 1
                j += 1
        return -1

if __name__=='__main__':
    haystack = 'abcdef'
    needle = 'cd'
    print(Solution().strStr(haystack,needle))