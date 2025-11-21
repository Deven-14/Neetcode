class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)

        i, j = 0, n-1
        char_removed = False
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            elif not char_removed and s[i+1] == s[j]:
                j -= 1
                i += 2
                char_removed = True
            else:
                break
        
        if i >= j:
            return True
        
        i, j = 0, n-1
        char_removed = False
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            elif not char_removed and s[i] == s[j-1]:
                j -= 2
                i += 1
                char_removed = True
            else:
                break

        if i >= j:
            return True

        return False



class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)

        i, j = 0, n-1
        while i < j and s[i] == s[j]:
            i += 1
            j -= 1
        
        if i >= j:
            return True
        
        l, r = i+1, j
        while l < r and s[l] == s[r]:
            l += 1
            r -= 1
        
        if l >= r:
            return True
        
        l, r = i, j-1
        while l < r and s[l] == s[r]:
            l += 1
            r -= 1

        if l >= r:
            return True

        return False
