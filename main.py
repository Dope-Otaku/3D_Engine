import pygame as pop

'''
in this we will create a class which will open a gui interface into which our 3d object will be rendered and
displayed | since we are not using c++ we need to use an external lib
'''
class ObjectRenderer:
    def __init__(self):
        pop.init() #called pygame for accessing the modules
