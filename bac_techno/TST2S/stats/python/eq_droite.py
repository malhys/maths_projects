import equation

my_A = [0, 0]
my_B = [4, 4]



def get_equation_points(A, B):
    """
        Détermination de l'équation de la droite passant par les points 
        A (xA ; yA) et B (xB ; yB) à partir de leurs coordinnées
    """
    
    # Calcul de la "pente" de la droite
    # coefficient directeur  = (xB - xA) / (yB - yA)
    coeff = (B[0]-A[0])/(B[1]-A[1])
    
    # Calcul de l'ordonnée à l'origine à partir du coefficient directeur
    # et des coordonnées du premier point
    ord_origine = A[1] - coeff * A[0]
    
    return equation.equation(coeff, ord_origine)


def get_equation_coef_point(coeff, A):
    """
        Détermination de l'équation de la droite de coefficient directeur coeff
        et qui passe par le point A (xA ; yA)
    """
    
    ord_origine = A[1] - coeff * A[0]
    
    return equation.equation(coeff, ord_origine)
    
    
    
#Exécution
eq = get_equation_points(my_A, my_B)
print(eq)