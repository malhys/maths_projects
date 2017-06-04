class stack(object):
    """Implantation d'une pile d'éléments à partir d'une liste"""
    
    def __init__(self):
        self.list=[]
        self.size=0
        
    def getSize(self):
        """Retourne le nombre d'éléments de la pile"""
        return self.size
    
    def push(self, elem):
        """Ajouter un élément non nul à la pile. (O(1)).
        Retourne 1 si l'ajout s'est bien déroulé. 0 sinon"""
        
        if elem != None:
            self.list.append(elem)
            self.size+=1
            return 1
        
        return 0
        
    def pop(self, elem):
        """Retire et renvoie le dernier élément ajouté"""
        
        if self.size > 0:
            self.size -= 1
            return self.list.pop()
            
        return None
            
