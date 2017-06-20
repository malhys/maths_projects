class cesar(object):
    '''Classe pour chifrer / déchiffrer un texte avec le code de ceésar
    (chiffrement par décalage, défini à la construction)
    '''
    
    def __init__(self, decalage):
        '''Constructeur, fournir le décalage souhaité'''
        self.decalage = decalage % 26
        
        
    def chiffrerLettre(self, lettre):
        
        if 'A' < lettre < 'Z':
            
            ecart = ord('Z') - ord(lettre)
            if ecart > self.decalge:
                
                return chr(ord(letrre) + self.decalage
                
            else :
                return chr(ord('A' + (self.decalge - ecart)))
                
        elif 'a' < lettre < 'z':
            
            ecart = ord('z') - ord(lettre)
            if ecart > self.decalge:
                
                return chr(ord(letrre) + self.decalage
                
            else:
                return chr(ord('a' + (self.decalge - ecart)))