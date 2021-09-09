# https://murhafsousli.github.io/8puzzle

class State:
    def __init__(self, tiles):
        """
        Parameters
        ----------
        tiles: 2d list
            A list of list of tiles.  All are numbers except for
            the blank, which is a " "
            Ex) [[2, 6, 1], [7, " ", 3], [5, 8, 4]]
        """
        self.tiles = tiles
        self.prev = None
    
    def __str__(self):
        """
        Returns
        -------
        A printable string representation of the board
        """
        s = ""
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                s += "{} ".format(self.tiles[i][j])
            s += "\n"
        return s
    
    def copy(self):
        """
        Return a deep copy of this state
        """
        tiles = []
        for i in range(len(self.tiles)):
            tiles.append([])
            for j in range(len(self.tiles[i])):
                tiles[i].append(self.tiles[i][j])
        return State(tiles)
    
    def is_goal(self):
        """
        Returns
        -------
        True if this is a goal state, False otherwise
        """
        res = True
        N = len(self.tiles)
        ## TODO: Fill this in
        return res

    def get_neighbs(self):
        """
        Get the neighboring states

        Returns
        -------
        list of State
            A list of the neighboring states
        """
        N = len(self.tiles)
        # Find empty element
        i = 0
        j = 0
        found = False
        while not found and i < N:
            if j < N:
                if self.tiles[i][j] == " ":
                    found = True
                else:
                    j += 1
            else:
                i += 1
                j = 0
        # Enumerate all neighbors around the empty element
        # by seeing if there's a valid swap to be made below,
        # above, to the left, and to the right
        neighbs = []
        for (di, dj) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            i2 = i + di
            j2 = j + dj
            if i2 >= 0 and i2 < N and j2 >= 0 and j2 < N:
                # Be sure to make a deep copy of the board before swapping
                s = self.copy() 
                # Here's a nifty python way to swap two elements in an array
                s.tiles[i][j], s.tiles[i2][j2] = s.tiles[i2][j2], s.tiles[i][j]
                neighbs.append(s)
        return neighbs
    
    def solve(self):
        """
        Find a shortest path from this state to a goal state

        Returns
        -------
        list of State
            A path from this state to a goal state, where the first 
            element is this state and the last element is the goal
        """
        visited = {}
        expanded = 1
        queue = [self]
        finished = False
        # TODO: Fill this in
        
        solution = []
        return solution