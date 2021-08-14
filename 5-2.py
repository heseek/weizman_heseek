import pygame
import random

Screen_x = 550 * 2
Screen_y = 350 * 2


class Cloud:
    def __init__(self, x, root):
        self.x = x
        self.y = random.randint(0, 25)
        self.image = root.image_cloud
        self.game = root
        self.speed = random.randint(5, 15)

    def move(self):
        self.x += self.speed
        if self.x > Screen_x:
            self.x = 0

    def draw(self):
        self.game.screen.blit(self.image, (self.x, self.y))

    def rain(self):
        for _ in range(1):
            self.game.rains.append(Rain(self.x + random.randint(0, 130), self.y + 60, self.game))

    # def click(self, event):


class Rain:
    def __init__(self, x, y, game):
        self.x = x
        self.y = y
        self.speed = random.randint(5, 18)
        self.bold = random.randint(1, 4)
        self.game = game
        self.len = random.randint(5, 15)
        # self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.color = (153, 204, 255)

    def move(self):
        self.y += self.speed
        self.x -= 3

    def off_screen(self):
        return self.y > Screen_y + 20

    def draw(self):
        pygame.draw.line(self.game.screen, self.color, (self.x, self.y), (self.x, self.y + self.len), self.bold)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('게임 제목')
        self.screen = pygame.display.set_mode((Screen_x, Screen_y))
        self.clock = pygame.time.Clock()
        self.playing = True
        self.rains = []
        self.clouds = []
        self.load_date()

    def load_date(self):
        self.image = pygame.image.load('bg1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (Screen_x, Screen_y))
        self.image_cloud = pygame.image.load('cloud-b.svg').convert_alpha()

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                for cloud in self.clouds:
                    cloud.click(event)

    def update(self):
        # 구름 생성
        while len(self.clouds) < 17:
            self.clouds.append(Cloud(random.randint(0, Screen_x), self))
        # 구름에서 비 내리기
        for cloud in self.clouds:
            cloud.rain()
        # 비 움직이게 하고 벗어나면 삭제
        for rain in self.rains:
            rain.move()
            if rain.off_screen():
                self.rains.remove(rain)
                del rain
        # 구름 움직이기
        for cloud in self.clouds:
            cloud.move()

    def draw(self):
        self.screen.fill((102, 102, 102))
        self.screen.blit(self.image, (0, 0))
        for rain in self.rains:
            rain.draw()
        for cloud in self.clouds:
            cloud.draw()


game = Game()
game.run()
pygame.quit()
