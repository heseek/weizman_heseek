import pygame
import random

Screen_x = 550 * 2
Screen_y = 350 * 2



class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('게임 제목')
        self.screen = pygame.display.set_mode((Screen_x, Screen_y))
        self.clock = pygame.time.Clock()
        self.playing = True

    def run(self):
        while self.playing:
            self.clock.tick(60)
            self.event()
            self.update()
            self.draw()
            pygame.display.update()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        pass

    def draw(self):
        self.screen.fill((204, 204, 204))


game = Game()
game.run()
pygame.quit()
