from csp import CSP
from variable import Variable
import sys


class BackTrackingSearch():

    def backtrack(self, csp: CSP, assignment: dict):
        
        if self.is_complete(csp,assignment):
            # file = open("result.txt",'a')
            # board = ""
            # for letter in "ABCDEFGHI":
            #     for num in range(1,10):
            #         board+= f"{assignment[letter + str(num)]}"
            # file.write(board + "\n")
            return assignment

        variable: Variable = self.get_var_with_mrv(csp, assignment)
        orig_domain = variable.domain.copy()
        for value in variable.order_domain_values():
            
            if self.is_consistent(assignment, variable, value):
               
                assignment[variable.key] = value
                variable.domain = set((value,))
                failure = self.forward_check(csp,assignment,variable,value)
               
                if not failure:

                    result = self.backtrack(csp, assignment)
                    if result != False:
                        return result
                    
                    del assignment[variable.key]
                    variable.domain = orig_domain
                
        return False
    
    def forward_check(self, csp, assignment, variable, value):
        #Keep track of remaining legal values for the unassigned
        #variables. Terminate when any variable has no legal values.
        for neighbor in variable.neighbors:
            if neighbor.key not in assignment and value in neighbor.domain:
                if len(neighbor.domain) == 1:
                    return True
                
        return False

    
    def get_var_with_mrv(self, csp: CSP, assignment):
        min = sys.maxsize
        mrv_var = None
        for var in csp.variables.values():
            if var.key not in assignment and len(var.domain) < min:
                mrv_var = var
        
        if mrv_var == None:
            raise Exception
        return mrv_var

    def is_complete(self, csp, assignment):
        for x,y in csp.constraints:
            if x.key not in assignment or y.key not in assignment or assignment[x.key] == assignment[y.key]:
                return False
        
        return True
    
    def is_consistent(self, assignment, variable, value):
        for neighbor in variable.neighbors:
            if neighbor.key in assignment.keys() and assignment[neighbor.key] == value:
                return False
        return True