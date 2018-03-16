


#############################################################################
#-----------------------------------DOCS------------------------------------#
#############################################################################
#                                                                           #
# Last changes:                                                             #
# show_neighbours in events and player.py                                   #
# add sprites                                                               #
# randomize wall images on spawn                                            #
#                                                                           #
# pR0blems:                                                                 #
# when player hits wall                                                     #
# mob visibility                                                            #
# spawn_mob() ggf neu refenzieren                                           #
#                                                                           #
# To do:                                                                    #
# hardcode range                                                            #
#                                                                           #
#############################################################################



import os
from os import path
import pygame as pg
import sys
from settings import *
from sprites import *
#from player import *
#from mob import *
#from wall import *
#from cell import *
import random

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Rts")
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, 'img')
        # outsourcen
        self.player_img = pg.image.load(os.path.join(img_folder, 'tank.png'))#.convert()
        self.ground_img1 = pg.image.load(os.path.join(img_folder, 'ground1.png')).convert()
        self.ground_img2 = pg.image.load(os.path.join(img_folder, 'ground2.png')).convert()
        self.tree_img1 = pg.image.load(os.path.join(img_folder, 'tree1.png')).convert()
        self.tree_img2 = pg.image.load(os.path.join(img_folder, 'tree2.png')).convert()
        self.tree_img3 = pg.image.load(os.path.join(img_folder, 'tree3.png')).convert()
        self.map_data = []
        with open(path.join(game_folder, "mapfile.txt"), "rt") as f:
            for line in f:
                self.map_data.append(line)


    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.wall_list = [self.tree_img1, self.tree_img2, self.tree_img3]
        self.mobs = pg.sprite.Group()
        self.cells = pg.sprite.Group()
        self.cell_list = [self.ground_img1, self.ground_img2]
        #load map
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == "1":
                    Wall(self, col, row, (random.choice(self.wall_list)))
                if tile == ".":
                    Cell(self, col, row, (random.choice(self.cell_list)))

        self.player  = Player(self, 15, 18)
        self.mob = Mob(self, 15,15)

    def spawn_cell(self, pos):
        e = Cell(self, pos[0], pos[1])

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                #Player
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy=1)
                if event.key == pg.K_SPACE:
                    self.player.show_neighbours()
                if event.key == pg.K_b:
                    self.player.hide_range()
                #Mob
                if event.key == pg.K_a:
                    self.mob.move(dx=-1)
                if event.key == pg.K_d:
                    self.mob.move(dx=1)
                if event.key == pg.K_w:
                    self.mob.move(dy=-1)
                if event.key == pg.K_s:
                    self.mob.move(dy=1)

            #if event.type == pg.KEYUP:
            #    if event.key == pg.K_SPACE:
            #787        self.player.hide_neighbours()


    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
