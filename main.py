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
        self.FPS = 60 #adjusting the max fps 
        self.screen = pop.display.set_mode(self.RES)
        self.clock = pop.time.Clock()

    def draw(self):
        self.screen.fill(pop.Color('darkslategray'))

    def run(self):
        while True:
            self.draw()
            [exit() for i in pop.event.get() if i.type == pop.QUIT]
            pop.display.set_caption(str(self.clock.get_fps()))
            pop.display.flip()
            self.clock.tick(self.FPS)


if __name__ == "__main__":
    app = ObjectRenderer()
    app.run()