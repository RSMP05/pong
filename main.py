import pygame as pg
import settings
import striker
import game
import screen
pg.init()
clock = pg.time.Clock()

def main():
    pg.display.set_caption("Pong")
    
    game.main()

if __name__ == "__main__":
    main()
