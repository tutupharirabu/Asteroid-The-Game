import os
import sys
import getpass
import pygame

from constants import *

from assets.player import Player
from assets.asteroid import Asteroid
from assets.asteroidfield import AsteroidField
from assets.shot import Shot

def game_over_screen(screen, score, whoami):
  font_large = pygame.font.Font(None, 72)
  font_medium = pygame.font.Font(None, 48)
  font_small = pygame.font.Font(None, 36)
  
  # Game over message
  game_over_text = font_large.render("GAME OVER", True, (255, 0, 0))
  final_score_text = font_medium.render(f"{whoami}'s Final Score: {score}", True, (255, 255, 255))
  
  # Options
  retry_text = font_small.render("Press R to Retry", True, (255, 255, 255))
  exit_text = font_small.render("Press ESC to Exit", True, (255, 255, 255))
  
  # Position the text
  screen_center_x = SCREEN_WIDTH // 2
  screen_center_y = SCREEN_HEIGHT // 2
  
  game_over_rect = game_over_text.get_rect(center=(screen_center_x, screen_center_y - 80))
  final_score_rect = final_score_text.get_rect(center=(screen_center_x, screen_center_y))
  retry_rect = retry_text.get_rect(center=(screen_center_x, screen_center_y + 80))
  exit_rect = exit_text.get_rect(center=(screen_center_x, screen_center_y + 120))
  
  # Draw everything
  screen.fill("black")
  screen.blit(game_over_text, game_over_rect)
  screen.blit(final_score_text, final_score_rect)
  screen.blit(retry_text, retry_rect)
  screen.blit(exit_text, exit_rect)
  pygame.display.flip()
  
  # Wait for player decision
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_r:
          return True  # Retry
        elif event.key == pygame.K_ESCAPE:
          return False  # Exit

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  
  try:
    whoami = getpass.getuser()
  except:
    whoami = os.environ.get('USER') or os.environ.get('USERNAME') or "Player One"
  
  while True:
    # Initialize score
    score = 0
    font = pygame.font.Font(None, 36)

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
    game_running = True

    while game_running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          return
      
      updatable.update(dt)

      for asteroid in asteroids:
        if asteroid.collides_with(player):
          game_running = False
          break

        for shot in shots:
          if asteroid.collides_with(shot):
            shot.kill()
            asteroid.split()
            # Increase score when asteroid is hit
            score += 100

      screen.fill("black")

      for obj in drawable:
        obj.draw(screen)
      
      # Display score
      score_text = font.render(f"Score: {score}", True, (255, 255, 255))
      screen.blit(score_text, (20, 20))
      
      pygame.display.flip()
      dt = clock.tick(60) / 1000
    
    # After game ends, show game over screen
    if not game_over_screen(screen, score, whoami):
      break  # Exit the game if player chose to exit

if __name__ == "__main__":
  main()