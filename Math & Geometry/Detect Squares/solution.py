from collections import defaultdict, Counter
class CountSquares:

    def __init__(self):
        self.xaxis = defaultdict(set)
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        self.xaxis[point[0]].add(point[1])
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        squares = 0
        num_of_point = 1 if (x, y) not in point else self.points[(x, y)]

        for a in self.xaxis[x]:
            d = abs(y - a)
            if d == 0:
                continue
            
            if (x-d, y) in self.points and (x-d, y+d) in self.points and (x, y+d) in self.points:
                n = self.points[(x-d, y)] * self.points[(x-d, y+d)] * self.points[(x, y+d)] * num_of_point
                squares += n
            
            if (x-d, y) in self.points and (x-d, y-d) in self.points and (x, y-d) in self.points:
                n = self.points[(x-d, y)] * self.points[(x-d, y-d)] * self.points[(x, y-d)] * num_of_point
                squares += n

            if (x+d, y) in self.points and (x+d, y+d) in self.points and (x, y+d) in self.points:
                n = self.points[(x+d, y)] * self.points[(x+d, y+d)] * self.points[(x, y+d)] * num_of_point
                squares += n
            
            if (x+d, y) in self.points and (x+d, y-d) in self.points and (x, y-d) in self.points:
                n = self.points[(x+d, y)] * self.points[(x+d, y-d)] * self.points[(x, y-d)] * num_of_point
                squares += n
        
        return squares


from collections import defaultdict, Counter
class CountSquares:

    def __init__(self):
        self.xaxis = defaultdict(set)
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        self.xaxis[point[0]].add(point[1])
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        squares = 0
        num_of_point = 1 if (x, y) not in point else self.points[(x, y)]

        for a in self.xaxis[x]:
            d = abs(y - a)
            if d == 0:
                continue
            
            squares += self.points[(x-d, y)] * self.points[(x-d, y+d)] * self.points[(x, y+d)] * num_of_point
            
            squares += self.points[(x-d, y)] * self.points[(x-d, y-d)] * self.points[(x, y-d)] * num_of_point

            squares += self.points[(x+d, y)] * self.points[(x+d, y+d)] * self.points[(x, y+d)] * num_of_point
                
            squares += self.points[(x+d, y)] * self.points[(x+d, y-d)] * self.points[(x, y-d)] * num_of_point
        
        return squares


from collections import defaultdict, Counter
class CountSquares:

    def __init__(self):
        self.xaxis = defaultdict(set)
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        self.xaxis[point[0]].add(point[1])
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        squares = 0
        num_of_point = 1 if (x, y) not in point else self.points[(x, y)]

        for y2 in self.xaxis[x]:
            d = abs(y2 - y)
            if d == 0:
                continue
            
            x3, x4 = x + d, x - d
            squares += self.points[(x, y2)] * self.points[(x3, y)] * self.points[(x3, y2)] * num_of_point
            
            squares += self.points[(x, y2)] * self.points[(x4, y)] * self.points[(x4, y2)] * num_of_point
        
        return squares

