from variable import Variable

class CSP():

    def __init__(self, board):
        self.variables = {}
        self.constraints = set()

        for key, value in board.items():
                self.variables[key] = Variable(key,value)

        for variable in self.variables.values():
            variable.neighbors = tuple(sorted(self.get_neighbors(variable)))
            for neighbor in variable.neighbors:
                self.constraints.add( tuple((variable,neighbor)) )


    def get_neighbors(self, variable):
        return set(filter(lambda other: self.is_peer(variable, other) ,self.variables.values()))


    def is_peer(self, variable, other):
        peer = not (other.row == variable.row and other.column == variable.column) \
            and (other.row == variable.row or other.column == variable.column or other.region == variable.region) 
        return peer