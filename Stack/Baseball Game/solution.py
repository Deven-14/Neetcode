class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for op in operations:
            match op:
                case '+':
                    scores.append(scores[-1] + scores[-2])
                case 'C':
                    scores.pop()
                case 'D':
                    scores.append(2 * scores[-1])
                case _:
                    scores.append(int(op))
        
        return sum(scores)