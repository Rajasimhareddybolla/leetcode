class CountSquares:

    def __init__(self):
        self.points = []
        self.x = {}
        self.y = {}

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        x , y = point
        if x not in self.x:
            self.x[x] = []
        if y not in self.y:
            self.y[y] = []
        self.x[x].append(y)
        self.y[y].append(x)


    def count(self, point: List[int]) -> int:
        x , y = point
        possy , possx = self.x.get(x ,[]) , self.y.get(y , [] )

        found , res= {} , 0
        if not possy or not possx: return 0
        for x1 in possx:
            dist = x1 - x
            if dist not in found :
                found[dist] = [x1 , 0]
            found[dist][1] +=1

        for y1 in possy:
            dist = y1 - y
            if dist in found:
                x1 , count = found[dist]

                if [x1, y+dist ] in self.points:
                    res += count
            if dist*-1 in found:
                dist = dist*-1
                x1 , count = found[dist]

                if [x1, y+dist ] in self.points:
                    res += count

                if [x1, y-dist ] in self.points:
                    res += count
        return res