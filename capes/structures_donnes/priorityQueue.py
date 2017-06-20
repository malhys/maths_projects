class priorityQueue(object):
    
    
    def __init__(self):
        self.list = []
        self.size = 0
        
    def getSize(self):
        return self.size
        
    def placeToInsert(elem, list):
        mid =  len(list)//2
         
        if list[mid] == elem :
             return mid
             
        if list[mid] < elem :
            return placeToInsert(elem, list[:mid])
            
        else:
            return placeToInsert(elem, list[mid:])
            
    def insert(self, elem):
        if elem == None:
            return 0
            
        else:
            
            if self.list[0] > elem:
                index = 0
            
            elif self.list[self.size-1] < elem:
                index = self.size - 1
            
            else:
                index = placeToInsert(elem, self.list)
            
            self.list.insert(index, elem)
            
    # def remove(self, elem):
    #     if elem in self.list:
    #         self.list.remove(elem)
    #         return 1
    #     
    #     return 0
    
    def pop(self):
        if self.size > 0:
            return self.list.pop(0)
            
        return 0
        
