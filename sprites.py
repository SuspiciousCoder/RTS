import pygame as pg
from settings import *


#Player
class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.image = pg.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.image.set_colorkey(WHITE)
        self.health = 3
        self.range = 3
        self.movement = 5
        self.x = x
        self.y = y
        #Unit HUD
        self.info()

    def info(self):
        self.font = pg.font.SysFont("Comic San MS", 25)
        self.image.blit(self.image, (0, 0))
        self.display_health = str(self.health)
        self.rendered = self.font.render(self.display_health, True, GREEN)
        self.image.blit(self.rendered, (TILESIZE / 4, 11))

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy
            self.health -= 1
            self.info()

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

#Still buggy stuff --- --- --- --- --- --- --- --- --- --- ---

    #fill new cells with objs and later on refer to there x 'n y's
    def get_neighbours(self):
        self.new_cells = [(Cell(self.x, self.y))]
        #ARRAY MANIPULTAION !!
        new_cell.append([Cell(self.x - 1, self.y)])
        new_cell.append([Cell(self.x + 1, self.y)])
        new_cell.append([Cell(self.x, self.y + 1)])
        new_cell.append([Cell(self.x, self.y - 1)])

        for Cell in new_cells:
            show_neighbours()

        self.old_cells = new_cells

    def fight(self, dx=0, dy=0):
        for sprite in self.game.all_sprites:
            if sprite.x == self.x +    dx and sprite.y == self.y + dy:
                self.health -= 1
                self.info()
                return True
        return False

#Not neded yet stuff

#    def move_per_turn(self, dx=0, dy=0):
#        if not self.collide_with_everything(dx, dy) and self.movement > 0:
#            self.x += dx
#            self.y += dy
#            self.movement -= 1
#            if enemy is neaR:
#               choose_target()


#walls
class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y, png):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = png
        self.image = pg.transform.scale(self.image, (TILESIZE,TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


#mob
class Mob(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y


    def move(self, dx=0, dy=0):
        if not self.collide_with_player(dx, dy):
            self.x += dx
            self.y += dy

    def collide_with_player(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                self.game.spawn_mob((wall.x + 1),(wall.y))
                self.game.spawn_mob((wall.x - 1),(wall.y))
                self.game.spawn_mob((wall.x),(wall.y + 1))
                self.game.spawn_mob((wall.x),(wall.y - 1))
                return True
        return False


    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE


#cell
class Cell(pg.sprite.Sprite):
    def __init__(self, game, x, y, png):
        self.groups = game.all_sprites, game.cells
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = png
        self.image = pg.transform.scale(self.image , (TILESIZE,TILESIZE) )
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
