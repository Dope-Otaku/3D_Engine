import pygame as pop

'''
in this we will create a class which will open a gui interface into which our 3d object will be rendered and
displayed | since we are not using c++ we need to use an external lib
'''
class ObjectRenderer:
    def __init__(self):
        pop.init() #called pygame for accessing the modules
        self.RES = self.WIDTH, self.HEIGHT = 1600, 900
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.fps = 60 #adjusting the fps 
        self.screen = pop.display.set_mode(self.RES)
        self.clock = pop.time.clock()

    def draw(self):
        self.screen.fill(pop.Color('darkslategray'))