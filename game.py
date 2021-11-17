
import pygame
from models import Rock, Spaceship
from utils import load_sprite

bullets = []
rocks = []

class SpaceRocks:
    def __init__(self):
        # Initialize pygame and set the title
        pygame.init()
        pygame.display.set_caption("Space Rocks")
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("space", False)

        self.ship = Spaceship((400, 300))

        global rocks
        rocks = [
            Rock.create_random(self.screen, self.ship.position)
            for _ in range(6)
        ]

    def main_loop(self):
        while True:
            self._handle_input()
            self._game_logic()
            self._draw()


    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.ship.shoot()




        is_key_pressed = pygame.key.get_pressed()
        if is_key_pressed[pygame.K_ESCAPE] or is_key_pressed[pygame.K_q]:
            quit()

        if self.ship is None:
            quit()

        elif is_key_pressed[pygame.K_RIGHT]:
            self.ship.rotate(clockwise=True)
        elif is_key_pressed[pygame.K_LEFT]:
            self.ship.rotate(clockwise=False)
        elif is_key_pressed[pygame.K_UP]:
            self.ship.acceleration()

    @property
    def game_object(self):
        global bullets, rocks
        stuff = [*bullets, *rocks]

        if self.ship:
            stuff.append(self.ship)

        return stuff

    def _game_logic(self):
        global bullets, rocks

        for obj in self.game_object:
            obj.move(self.screen)

        rect = self.screen.get_rect()
        for bullet in bullets[:]:
            if not rect.collidepoint(bullet.position):
                bullets.remove(bullet)

        for bullet in bullets[:]:
            for rock in rocks[:]:
                if rock.collides_with(bullet):
                    #for some reason the .split function is not appending the new split rocks into game.py
                    rocks.remove(rock)
                    rock.split()
                    bullets.remove(bullet)
                    break

        if self.ship:
            for rock in rocks[:]:
                if rock.collides_with(self.ship):
                    quit()
                    break

    def _draw(self):
        self.screen.blit(self.background, (0, 0))

        for obj in self.game_object:
            obj.draw(self.screen)

        pygame.display.flip()
        self.clock.tick(60)

if __name__ == "__main__":
    asteroids = SpaceRocks()
    asteroids.main_loop()
