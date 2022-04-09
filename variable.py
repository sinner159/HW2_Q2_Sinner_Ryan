
class Variable():

    super_row_1 = "ABC"
    super_row_2 = "DEF"
    super_row_3 = "GHI"

    super_column_1 = "123"
    super_column_2 = "456"
    super_column_3 = "789"

    def __init__(self,key,value):
        self.key = key
        if value == 0:
            self.domain = set((1,2,3,4,5,6,7,8,9))
        else:
            self.domain = set((value,))
        
        self.row = key[0]
        self.column = key[1]   
        self.region = self.get_region()

    def order_domain_values(self):
        return self.domain
        
    def get_region(self):
        
        row = self.row

        if row in self.super_row_1:
            return self.get_super_column(0)
        elif row in self.super_row_2:
            return self.get_super_column(3)
        elif row in self.super_row_3:
            return self.get_super_column(6)
        else:
          raise Exception

    def get_super_column(self, modifier):
    
        column = self.column

        if column in self.super_column_1:
            return 1 + modifier
        elif column in self.super_column_2:
            return 2 + modifier
        elif column in self.super_column_3:
            return 3 + modifier
        else:
            raise Exception

    def __lt__(self, other):
        return self.key < other.key
    
    def __repr__(self):
        return f"{self.key} {self.domain}"