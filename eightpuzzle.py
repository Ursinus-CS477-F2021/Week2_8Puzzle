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
        N = len(self.tiles)
        # Step 1: Create a new 1D list with the elements
        # in row major order
        rowmajor = []
        for i in range(N):
            for j in range(N):
                if self.tiles[i][j] != " ":
                    rowmajor.append(self.tiles[i][j])
        # Step 2: If a single pair of elements is out of order
        # then this isn't a goal state
        res = True
        for i in range(len(rowmajor)-1):
            if rowmajor[i+1] < rowmajor[i]:
                res = False
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
        # Enumerate all neighbors around this element
        neighbs = []
        for (di, dj) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            i2 = i + di
            j2 = j + dj
            if i2 >= 0 and i2 < N and j2 >= 0 and j2 < N:
                s = self.copy()
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
        visited = set([])
        expanded = 1
        queue = [self] # We start the search from the state that this method
        # is called on, so that should be the first in the queue
        finished = False
        end = None
        while len(queue) > 0 and not finished:
            expanded += 1
            state = queue.pop(0) #this makes it so the first element goes from the left
            if state.is_goal():
                end = state
                finished = True
            else:
                neighbs = state.get_neighbs()
                for move in neighbs:
                    if not str(move) in visited:
                        move.prev = state
                        expanded += 1
                        queue.append(move)
                        visited.add(str(move)) # This is like Java's tostring method
        print("Expanded: ", expanded)
        # We now trace back from the goal state, following all of the "prev"
        # arrows until we get back to the start
        states = [end]
        state = end
        while state.prev:
            state = state.prev
            states.append(state)
        # If we want to show the solution from the beginning, we reverse the list we've
        # constructed
        states.reverse()
        return states