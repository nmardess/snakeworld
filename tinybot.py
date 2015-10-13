from common import Direction, Point
from client import BaseClient


class tinyBot(BaseClient):

    def __init__(self, name):
        super().__init__(name)
        self.plateau = set((x, y) for x in range(200) for y in range(100))
        self.direction = [(-1, 0), (+1, 0), (0, -1), (0, +1)]

    def evaluate(self):
        myhead = (self.mysnake.position.x, self.mysnake.position.y)

        plusProcheFruit = min([(fruit.position.manathan_distance(self.mysnake.position),
                                (fruit.position.x, fruit.position.y))
                               for fruit in self.state.fruits])[1]

        obstacles = set()
        for snake in self.state.snakes:
            for point in self.state.snakes[snake].body:
                obstacles.add((point.x, point.y))

        plateauSansObstacles = self.plateau - obstacles

        directionVoisines = {'l': (-1, 0), 'r': (+1, 0), 'u': (0, -1), 'd': (0, +1)}

        directionsViables = [(Point(myhead[0] + c[0], myhead[1] + c[1]).manathan_distance(Point(plusProcheFruit[0], plusProcheFruit[1])), d) for (d, c) in directionVoisines.items() if (myhead[0] + c[0]) >= 0 and (
            myhead[1] + c[1]) >= 0 and (myhead[0] + c[0], myhead[1] + c[1]) in plateauSansObstacles]

        if not directionsViables:
            # screwed up
            return None
            
        directionFruitPlusProche = min(directionsViables)
        direction = Direction(directionFruitPlusProche[1])

        return direction

bot = tinyBot('KhamaBot')
bot.run_until_complete()
