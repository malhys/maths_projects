class queue(object):
    """Imlantation d'une file (FIFO) sur la base d'une liste"""
    def __init__(self):
        self.list = []
        self.size = 0
        
    def get_size(self):
        """Retourne le nombre d'éléments dans la file (O(1))"""
        return self.size
        
    
    def push(self, elem):
        """Ajouter un élément à la fin de la file (O(1))
        
            Retourne 1 si l'ajout s'est bien déroulé, 0 sinon"""
        if elem != None:
            self.list.append(elem)
            self.size += 1
            return 1
            
        return 0
     
     
    def pop(self):
        """Retirer le premier élément de la file si elle n'est pas vide. (O(1))
            Retourne l'élément retiré, None si la file est vide"""
            
        if self.size > 0:
            self.size -= 1
            return self.list.pop(0)
            
        return None
           
    