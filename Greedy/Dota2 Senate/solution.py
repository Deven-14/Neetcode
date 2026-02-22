class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rcount, dcount = senate.count('R'), senate.count('D')
        rskip, dskip = 0, 0
        i, n = 0, len(senate)

        while rcount and dcount:
            party = senate[i]
            if party == 'R':
                if rskip > 0:
                    rcount -= 1
                    rskip -= 1
                else:
                    dskip += 1
            elif party == 'D':
                if dskip > 0:
                    dcount -= 1
                    dskip -= 1
                else:
                    rskip += 1
            
            i = (i + 1) % n
        
        return "Radiant" if rcount > 0 else "Dire"