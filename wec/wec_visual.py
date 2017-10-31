import pygame
import pymunk.pygame_util


class wec_visual():

    def __init__(self):
        # initialize screen for displaying WEC design
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 800))
        self.screen.fill((255, 255, 255))
        pygame.display.update()

    def display(self, device):

        options = pymunk.pygame_util.DrawOptions(self.screen)
        device.world.step(1)
        device.world.step(2)
        device.world.debug_draw(options)
        pygame.display.update()
