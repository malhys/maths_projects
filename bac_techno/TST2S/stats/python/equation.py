class equation(object):
    
    def __init__(self, coeff, ord_origine):
        self.coeff = coeff
        self.ord_origine =  ord_origine
        
    def get_coeff(self):
        return self.coeff
        
    def get_ordonee_orgine(self):
        return self.ord_origine
        
    def check_point(self, x, y):
        return y == x*self.coeff + self.ord_origine
        
    def __str__(self):
        
        res = "y = "
        
        if self.coeff != 0 :
            res += "{}x  ".format(self.coeff)
         
        if self.ord_origine < 0 :
            res += "{}".format(self.ord_origine)
        
        elif self.ord_origine > 0 :
            res += "+ {}".format(self.ord_origine)
        
        return res
        
    # def __repr__(self):
    #     res = "y = {}x  ".format(self.coeff)
    #     
    #     
    #     if self.ord_origine < 0 :
    #         res += "{}".format(self.ord_origine)
    #     
    #     elif self.ord_origine > 0 :
    #         res += "+ {}".format(self.ord_origine)
    #     
    #     return res
        