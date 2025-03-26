import os
import sys
import getpass
import pygame

from constants import *

from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = updatable
  asteroid_field = AsteroidField()

  shots = pygame.sprite.Group()

  Shot.containers = (shots, updatable, drawable)
  
  Player.containers = (updatable, drawable)
  
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  dt = 0

  try:
    whoami = getpass.getuser()
  except:
    whoami = os.environ.get('USER') or os.environ.get('USERNAME') or "Player One"

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    updatable.update(dt)

    for asteroid in asteroids:
      if asteroid.collides_with(player):
        print(f'Game Over, {whoami}!')
        sys.exit()

      for shot in shots:
        if asteroid.collides_with(shot):
          shot.kill()
          asteroid.split()

    screen.fill("black")

    for obj in drawable:
      obj.draw(screen)
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()