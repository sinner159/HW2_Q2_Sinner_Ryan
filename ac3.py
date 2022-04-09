from queue import Queue
from csp import CSP


class AC3():

    def ac3(self, csp : CSP):
        
        queue = Queue()

        for constraint in csp.constraints:
            queue.put(constraint)

        while not queue.empty():
            (xi,xj) = queue.get()

            if self.revise(xi, xj):
                if len(xi.domain) == 0: 
                    return False
                
                other_neighbors = set(xi.neighbors) - set((xj,))
                for xk in other_neighbors:
                   queue.put((xk, xi))
        
        return True

    def revise(self, xi, xj):
        revised = False
        x_to_remove = set()
        for x in xi.domain:
            if self.no_value_to_satisfy_constraint(x, xj.domain):
                x_to_remove.add(x)
                revised = True

        if len(x_to_remove) > 0:
            xi.domain = xi.domain - x_to_remove

        return revised

    def no_value_to_satisfy_constraint(self, x, xj_domain):
        for y in xj_domain:
            if y != x:
                return False
        return True
