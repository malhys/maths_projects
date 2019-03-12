from turtle import *

rainbow=["red", "orange", "yellow", "green", "cyan", "blue", "violet", "indigo", "green", "yellow", "orange"]

nb = 0

def getNewColor(nb):
    
    nb = nb % len(rainbow)
    pencolor(rainbow[nb])
    nb += 1
    return nb

def carre(length):
    for i in range(4):
        forward(length)
        left(90)
        
def polygon(length, nb_sides):
    for i in range(nb_sides):
        forward(length)
        left(360/nb_sides)
    
    
    
def figure(length, nb_sides, nb_polygons):
    nb=0
    for i in range(nb_polygons):
        polygon(length, nb_sides)
        left(360/nb_polygons)
        #nb=getNewColor(nb)

clearscreen()
figure(150, 4, 50)
