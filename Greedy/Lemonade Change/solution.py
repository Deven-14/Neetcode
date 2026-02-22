class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = { 5: 0, 10: 0, 20: 0 }
        for bill in bills:
            change[bill] += 1
            match bill:
                case 5:
                    continue
                case 10 if change[5] > 0:
                    change[5] -= 1
                case 20 if change[10] > 0 and change[5] > 0:
                    change[10] -= 1
                    change[5] -= 1
                case 20 if change[5] >= 3:
                    change[5] -= 3
                case _:
                    return False
        
        return True


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0

        for bill in bills:
            match bill:
                case 5:
                    five += 1
                case 10 if five > 0:
                    ten += 1
                    five -= 1
                case 20 if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                case 20 if five >= 3:
                    five -= 3
                case _:
                    return False
        
        return True