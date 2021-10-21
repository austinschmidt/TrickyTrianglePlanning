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

    def insert_peg(self, peg):
        if self.peg is None:
            self.peg = peg
            return True
        else: 
            return False

class Board:
    def peg_in(self, peg, hole):
        if self.holes[hole.peg.id].id is peg.id:
            return True
        else:
            return False

    def peg_exists(self, peg):
        for h in self.holes:
            if h.peg is not None:
                if h.peg.id is peg.id:
                    return True
        return False

    def hole_empty(self, hole):
        if self.holes[hole.id].peg is None:
            return True
        else:
            return False

    def check_if_move_allowed(self, peg, source_hole, over_hole, destination_hole):
        if self.peg_exists(peg) and self.peg_in(peg, source_hole) and not self.hole_empty(over_hole) and self.hole_empty(destination_hole) and ([source_hole, over_hole, destination_hole] in self.lines):
           return True
        else:
            return False

    #method to detect if legal moves are present on the board
    def legal_moves(self):
        legal_moves = {}
        for h in self.holes:
            if h.peg is not None:
                for over in h.adjacents:
                    for dest in over.adjacents:
                        if over is not dest and h is not over and h is not dest:
                            if self.check_if_move_allowed(h.peg, h, over, dest):
                                print("peg"+str(h.peg.id)+" source"+str(h.id)+" over"+str(over.id)+" dest"+str(dest.id))

    def move_peg(self, peg, source_hole, over_hole, destination_hole):
        if self.check_if_move_allowed(peg, source_hole, over_hole, destination_hole):
            self.remove_peg(over_hole)
            peg_to_insert = self.remove_peg(source_hole)
            self.insert_peg(peg_to_insert, destination_hole)

    def remove_peg(self, hole):
        peg = self.holes[hole.id].peg
        self.holes[hole.id].peg = None
        return peg

    def insert_peg(self, peg, hole):
        self.holes[hole.id].peg = peg
    

    def __init__(self, num_levels):
        self.number_of_pegs = 0
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

        count = 0
        for location in self.holes:
            location.insert_peg(Peg(count))
            count = count +1
            self.number_of_pegs = self.number_of_pegs-1

        #remove the peg from hole 2
        self.remove_peg(self.holes[2])

if __name__ == "__main__":
    game = Board(4)
    
    #should be true
    print(game.peg_in(game.holes[0].peg, game.holes[0]))
    
    #should be true
    print(game.peg_exists(game.holes[0].peg))
    
    #should be false
    print(game.hole_empty(game.holes[0]))

    #shoudl be true
    print(game.hole_empty(game.holes[2]))

    #should be true
    peg = game.holes[9].peg
    source_hole = game.holes[9]
    over_hole = game.holes[5]
    destination_hole = game.holes[2]
    print(game.check_if_move_allowed(peg, source_hole, over_hole, destination_hole))

    game.legal_moves()
    print()

    game.move_peg(game.holes[9].peg, game.holes[9], game.holes[5], game.holes[2])
    game.legal_moves()
    print()
