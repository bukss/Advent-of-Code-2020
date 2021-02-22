DIR_COORDS = {
    "u": ( 0, -1),
    "d": ( 0,  1),
    "r": ( 1,  0),
    "l": (-1,  0),
}

class Tile:
    DIRECTIONS = {
        "r": "l",
        "d": "u",
        "l": "r",
        "u": "d"
    }
    def __init__(self, n, pattern):
        self.pattern = pattern
        self.oriented = False
        self.number = n
        self.edges = self.get_edges()
        self.adj_edges = {}
        self.adj_tiles = {}
    
    def get_edges(self):
        e = {"u":tuple(self.pattern[0]), "d":tuple(self.pattern[-1])}
        e["r"] = tuple([i[0] for i in self.pattern])
        e["l"] = tuple([i[-1] for i in self.pattern])
        return e

    def flip(self):
        self.pattern = self.pattern[::-1]
        self.edges = self.get_edges()

    def rotate(self):
        self.pattern = list(zip(*self.pattern[::-1]))
        self.edges = self.get_edges()

    def matches(self, tile):
        for d in Tile.DIRECTIONS:
            if self.edges[d] == tile.edges[Tile.DIRECTIONS[d]]:
                return d
        return None

    def orient(self, tile):
        #print(self.number)
        for i in range(4):
            if self.oriented:
                break

            self.rotate()
            if (d:=self.matches(tile)):
                self.oriented = True
                self.adj_tiles[d] = tile
                tile.adj_tiles[Tile.DIRECTIONS[d]] = self
                break

            self.flip()
            if (d:=self.matches(tile)):
                self.oriented = True
                self.adj_tiles[d] = tile
                tile.adj_tiles[Tile.DIRECTIONS[d]] = self
                break
            
            self.flip()
        

        if not self.oriented:
            print("CANNOT ORIENT")
            print(self.edges)
            print(tile.edges)
            exit()   

        for t in self.adj_edges.values():
            #print(t.number, t.adj_tiles.keys())
            if not t.oriented:
                t.orient(self)