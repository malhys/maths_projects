class set(object):
    """Implantation d'un ensemble à partir d'une liste"""
    
    def __init__(self):
        self.list=[]
        self.size=0
        
    def getSize(self):
        return self.size
        
    def add(self, elem):
        """Ajouter un élément à l'ensemble"""
        if elem != None:
            #L'utilisateur a bien fourni un élément à ajouter
            
            if not (elem in self.list):
                #L'élément n'est pas déjà présent dans l'ensemble
                self.list.append(elem)
                self.size += 1
                return 1
            
            return -1
        return 0

    def contains(self, elem):
        """Savoir si un élément est présent dans l'ensemble"""
        return elem in self.size

    def remove(self, elem):
        if elem != None:
            #L'élément fourni est valide
            if elem in self.list:
                #L'élément fourni est présent dasn l'ensemble
                self.list.remove(elem)
                self.size -= 1
                return 1
            
            return -1
        
        return 0