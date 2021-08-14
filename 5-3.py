import pygame
import random
from pygame.locals import *

SCREEN_X = 550 * 2
SCREEN_Y = 350 * 2
CHARACTER_SPEED = 5


class Player:
    def __init__(self, root):
        self.x = 100
        self.y = SCREEN_Y - 200
        self.dx = 0
        self.dy = 0
        self.game = root
        self.image = self.game.player_image
        self.hit = 0

    def move(self, key):
        if key == pygame.K_UP:
            self.dy = -CHARACTER_SPEED
            self.dx = 0
        if key == pygame.K_DOWN:
            self.dy = CHARACTER_SPEED
            self.dx = 0
        if key == pygame.K_LEFT:
            self.dx = -CHARACTER_SPEED
            self.dy = 0
        if key == pygame.K_RIGHT:
            self.dx = CHARACTER_SPEED
            self.dy = 0

        if 0 < self.x < SCREEN_X:
            self.x += self.dx
        else:
            self.dx *= -1
            self.x += self.dx

        if 0 < self.y < SCREEN_Y:
            self.y += self.dy
        else:
            self.dy *= -1
            self.y += self.dy

    def draw(self):
        game.screen.blit(self.image, (self.x, self.y))


class Cloud:
    def __init__(self, x, root):
        self.x = x
        self.y = random.randint(0, 25)
        self.image = root.image_cloud
        self.game = root
        self.speed = random.randint(5, 15)

    def move(self):
        self.x += self.speed
        if self.x > SCREEN_X:
            self.x = 0

    def draw(self):
        self.game.screen.blit(self.image, (self.x, self.y))

    def rain(self):
        for _ in range(1):
            self.game.rains.append(Rain(self.x + random.randint(0, 130), self.y + 60, self.game))

    def click(self):
        pos = pygame.mouse.get_pos()
        rect = self.image.get_rect()
        rect.x = self.x
        rect.y = self.y
        return rect.collidepoint(pos)


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
        return self.y > SCREEN_Y + 20

    def draw(self):
        pygame.draw.line(self.game.screen, self.color, (self.x, self.y), (self.x, self.y + self.len), self.bold)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('게임 제목')
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
        self.clock = pygame.time.Clock()
        self.playing = True
        self.rains = []
        self.clouds = []
        self.load_date()
        self.player = Player(self)

    def load_date(self):
        self.image = pygame.image.load('bg1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (SCREEN_X, SCREEN_Y))
        self.image_cloud = pygame.image.load('cloud-b.svg').convert_alpha()
        self.player_image = pygame.image.load('beetle (1).svg').convert_alpha()
        self.player_image = pygame.transform.scale(self.player_image, (260, 200))

    def run(self):
        self.opening()
        while self.playing:
            self.clock.tick(60)
            self.event()
            self.update()
            self.draw()
            pygame.display.update()
        self.ending()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for cloud in self.clouds:
                    if cloud.click():
                        self.clouds.remove(cloud)
                        del cloud
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.playing = False
                self.player.move(event.key)

    def update(self):
        # 구름 생성
        while len(self.clouds) < 17:
            self.clouds.append(Cloud(random.randint(0, SCREEN_X), self))
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
        # 플레이어 움직이기
        self.player.move(None)

    def draw(self):
        self.screen.fill((102, 102, 102))
        self.screen.blit(self.image, (0, 0))
        for rain in self.rains:
            rain.draw()
        for cloud in self.clouds:
            cloud.draw()
        self.player.draw()

    def opening(self):
        self.screen.fill(pygame.Color('black'))
        stop = True
        self.draw_text(f'스페이스 바 = 시작.', 30, pygame.Color('hotpink'), 100, SCREEN_Y * 1 / 20)
        self.draw_text(f'화살표 키 = 움직임.', 30, pygame.Color('hotpink'), 100, SCREEN_Y * 2 / 20)
        self.draw_text(f'q 버튼  = 종료.', 30, pygame.Color('hotpink'), 100, SCREEN_Y * 3 / 20)
        self.draw_text(f'구름 클릭 = 없어짐(구름이).', 30, pygame.Color('hotpink'), 100, SCREEN_Y * 4 / 20)
        pygame.display.flip()
        while stop:
            self.clock.tick(60)
            pygame.event.get()
            self.pressed_key = pygame.key.get_pressed()
            if self.pressed_key[K_SPACE]:
                stop = False

    def ending(self):
        self.screen.fill(pygame.Color('black'))
        stop = True
        self.draw_text(f':)', 30, pygame.Color('hotpink'), 100, SCREEN_Y * 1 / 30)

        pygame.display.flip()
        while stop:
            self.clock.tick(60)
            pygame.event.get()
            self.pressed_key = pygame.key.get_pressed()
            if self.pressed_key[K_SPACE]:
                stop = False

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.SysFont('malgungothic', size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.x = x
        text_rect.y = y
        self.screen.blit(text_surface, text_rect)


game = Game()
game.run()
pygame.quit()
