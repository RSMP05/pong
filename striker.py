import settings
import pygame as pg
import screen
pg.init()

class Striker:
    def __init__(self, posx, posy, width, height, speed, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.playerRect = pg.Rect(posx, posy, width, height)
        self.payerDraw = pg.draw.rect(screen.screen, self.color, self.playerRect)

    def display(self):
        self.playerDraw = pg.draw.rect(screen.screen, self.color, self.playerRect)

    def update(self, yFac):
        #yFac == -1 -> moving upwards
        #yFac == 1 -> moving downwards
        #yFac == 0 -> not moving
        self.posy = self.posy + (self.speed * yFac)

        if self.posy <= 0:
            self.posy = 0
        elif self.posy + self.height >= settings.HEIGHT:
            self.posy = settings.HEIGHT - self.height

        self.playerRect = pg.Rect(self.posx, self.posy, self.width, self.height)

    def displayScore(self, text, score, x, y, color):
        text = settings.font20.render(text + str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)

        screen.screen.blit(text, textRect)

    def getRect(self):
        return self.playerRect
