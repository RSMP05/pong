import pygame as pg
import striker
import ballpy
import settings
import screen
import main as mainpy
pg.init()

def main():
    running = True

    player1 = striker.Striker(20, 0, 10, 100, 10, settings.GREEN)
    player2 = striker.Striker(settings.WIDTH-30, 0, 10, 100, 10, settings.GREEN)
    ball = ballpy.Ball(settings.WIDTH//2, settings.HEIGHT//2, 7, 7, settings.WHITE)

    playerList = [player1, player2]

    player1score, player2score = 0, 0
    player1YFac, player2YFac = 0, 0

    while running:
        screen.screen.fill(settings.BLACK)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    player2YFac = -1
                if event.key == pg.K_DOWN:
                    player2YFac = 1
                if event.key == pg.K_w:
                    player1YFac = -1
                if event.key == pg.K_s:
                    player1YFac = 1
            if event.type == pg.KEYUP:
                if event.key == pg.K_UP or event.key == pg.K_DOWN:
                    player2YFac = 0
                if event.key == pg.K_w or event.key == pg.K_s:
                    player1YFac = 0

        for player in playerList:
            if pg.Rect.colliderect(ball.getRect(), player.getRect()):
                ball.hit()

        player1.update(player1YFac)
        player2.update(player2YFac)
        point = ball.update()

        if point == -1:
            player1score += 1
        elif point == 1:
            player2score += 1

        if point:
            ball.reset()

        player1.display()
        player2.display()
        ball.display()

        player1.displayScore("Player 1", player1score, 100, 20, settings.WHITE)
        player2.displayScore("Player 2", player2score, settings.WIDTH - 100, 20, settings.WHITE)

        pg.display.update()

        mainpy.clock.tick(settings.FPS)
