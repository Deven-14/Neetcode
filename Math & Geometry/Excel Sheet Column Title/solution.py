class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber <= 26:
            return chr(64 + columnNumber)

        title = []
        q = columnNumber

        while q > 26:
            q, r = divmod(q, 26)
            title.append(chr(64 + r))
        
        if q > 0:
            title.append(chr(64 + q))
        
        return "".join(title[::-1])
        
        