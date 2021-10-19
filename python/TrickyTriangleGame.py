class Peg():
    def __init__(self, id):
        self.id = id

class Hole():
    def __init__(self, id):
        self.id = id
        self.adjacents = []
        self.peg = None

    def add_adjacent(self, other):
        self.adjacents.append(other)

    def add_line(self, line):
        self.lines.append(line)

class Board:
    def __init__(self, num_levels):
        self.holes = []
        self.levels = []

        self.lines = []

        level_count = 0
        for i in range(num_levels):
            level_count = level_count + 1
            self.levels.append(level_count)

        hole_count = 0
        for level in self.levels:
            for spot in range(level):
                self.holes.append(Hole(hole_count))
                hole_count = hole_count +1

        self.holes[0].add_adjacent(self.holes[1])
        self.holes[0].add_adjacent(self.holes[2])

        self.holes[1].add_adjacent(self.holes[0])
        self.holes[1].add_adjacent(self.holes[2])
        self.holes[1].add_adjacent(self.holes[3])
        self.holes[1].add_adjacent(self.holes[4])

        self.holes[2].add_adjacent(self.holes[0])
        self.holes[2].add_adjacent(self.holes[1])
        self.holes[2].add_adjacent(self.holes[4])
        self.holes[2].add_adjacent(self.holes[5])

        self.holes[3].add_adjacent(self.holes[1])
        self.holes[3].add_adjacent(self.holes[4])
        self.holes[3].add_adjacent(self.holes[6])
        self.holes[3].add_adjacent(self.holes[7])

        self.holes[4].add_adjacent(self.holes[1])
        self.holes[4].add_adjacent(self.holes[2])
        self.holes[4].add_adjacent(self.holes[3])
        self.holes[4].add_adjacent(self.holes[5])
        self.holes[4].add_adjacent(self.holes[7])
        self.holes[4].add_adjacent(self.holes[8])

        self.holes[5].add_adjacent(self.holes[2])
        self.holes[5].add_adjacent(self.holes[4])
        self.holes[5].add_adjacent(self.holes[8])
        self.holes[5].add_adjacent(self.holes[9])
        self.holes[5].add_adjacent(self.holes[7])

        self.holes[6].add_adjacent(self.holes[3])
        self.holes[6].add_adjacent(self.holes[7])

        self.holes[7].add_adjacent(self.holes[3])
        self.holes[7].add_adjacent(self.holes[4])
        self.holes[7].add_adjacent(self.holes[7])
        self.holes[7].add_adjacent(self.holes[8])

        self.holes[8].add_adjacent(self.holes[4])
        self.holes[8].add_adjacent(self.holes[5])
        self.holes[8].add_adjacent(self.holes[7])
        self.holes[8].add_adjacent(self.holes[9])

        self.holes[9].add_adjacent(self.holes[5])
        self.holes[9].add_adjacent(self.holes[8])

        #    0
        #   1 2
        #  3 4 5
        # 6 7 8 9

        self.lines.append([self.holes[0],self.holes[1], self.holes[3]])
        self.lines.append([self.holes[0],self.holes[2], self.holes[5]])

        self.lines.append([self.holes[1],self.holes[3], self.holes[6]])
        self.lines.append([self.holes[1],self.holes[4], self.holes[8]])

        self.lines.append([self.holes[2],self.holes[4], self.holes[7]])
        self.lines.append([self.holes[2],self.holes[5], self.holes[9]])
        
        self.lines.append([self.holes[3],self.holes[1], self.holes[0]])
        self.lines.append([self.holes[3],self.holes[4], self.holes[5]])

        self.lines.append([self.holes[5],self.holes[2], self.holes[0]])
        self.lines.append([self.holes[5],self.holes[4], self.holes[3]])

        self.lines.append([self.holes[6],self.holes[3], self.holes[1]])
        self.lines.append([self.holes[6],self.holes[7], self.holes[8]])

        self.lines.append([self.holes[7],self.holes[4], self.holes[2]])
        self.lines.append([self.holes[7],self.holes[8], self.holes[9]])

        self.lines.append([self.holes[8],self.holes[4], self.holes[1]])
        self.lines.append([self.holes[8],self.holes[7], self.holes[6]])

        self.lines.append([self.holes[9],self.holes[5], self.holes[2]])
        self.lines.append([self.holes[9],self.holes[8], self.holes[7]])

if __name__ == "__main__":
    game = Board(4)
