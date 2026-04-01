from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.x = defaultdict(list)
        self.y = defaultdict(list)
        self.points = defaultdict(int)

    def add(self, point):
        x, y = point
        self.x[x].append(y)
        self.y[y].append(x)
        self.points[(x, y)] += 1

    def count(self, point):
        x, y = point
        res = 0

        possy = self.x.get(x, [])
        possx = self.y.get(y, [])

        if not possy or not possx:
            return 0

        for x1 in possx:
            if x1 == x:
                continue

            side = abs(x1 - x)

            for y1 in possy:
                if y1 == y:
                    continue

                if abs(y1 - y) == side:
                    # diagonal point
                    res += self.points[(x1, y1)]

        return res