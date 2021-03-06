from threading import Thread

import pygame

BACKGROUND = (20, 20, 20)
GRID = (70, 70, 70)
TOPPATH = (180, 20, 200)
BOTTOMGOAL = (80, 5, 90)
BOTTOMPATH = (60, 200, 60)
TOPGOAL = (20, 90, 20)


class Display:
    SIZE = 60
    LINE_WIDTH = 4
    FPS = 10
    bgSurface = None
    player = TOPPATH
    _quit = False

    def __init__(self, n, m, g):
        pygame.init()
        self.WIDTH = self.SIZE * n * 2
        self.HEIGHT = self.SIZE * (m * 2 + 2)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.loc = (self.WIDTH / 2, self.HEIGHT / 2)
        self.fgSurface = pygame.Surface((self.WIDTH, self.HEIGHT),pygame.SRCALPHA)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Paper Soccer')
        self.drawgrid(n, m, g)

    def drawgrid(self, n, m, g):
        self.bgSurface = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.bgSurface.fill((20, 20, 20))
        for x in range(n * 2):
            for y in range(m * 2 + 2):
                if y == 0:
                    color = TOPGOAL
                elif y == m * 2 + 1:
                    color = BOTTOMGOAL
                else:
                    color = GRID
                if 0 < y < m * 2 + 1 or n - g <= x < n + g:
                    rect = pygame.Rect(x * self.SIZE, y * self.SIZE, self.SIZE - 1, self.SIZE - 1)
                    pygame.draw.rect(self.bgSurface, color, rect)

    def addmove(self, direction):
        for ds in direction:
            d = int(ds)
            nloc = (self.loc[0] + ((0 < d < 4) - (4 < d < 8)) * self.SIZE, self.loc[1] + ((2 < d < 6) - (d < 2 or d > 6)) * self.SIZE)
            pygame.draw.line(self.fgSurface, self.player, self.loc, nloc, self.LINE_WIDTH)
            self.loc = nloc
        self.player = TOPPATH if self.player == BOTTOMPATH else BOTTOMPATH

    def startupdateloop(self):
        Thread(target=self._updateloop).start()

    def _updateloop(self):
        while not self._quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._quit = True
            self.screen.blit(self.bgSurface, (0, 0))
            self.screen.blit(self.fgSurface, (0, 0))
            pygame.display.update()
            self.clock.tick(self.FPS)
        pygame.display.quit()

    def close(self):
        self._quit = True
