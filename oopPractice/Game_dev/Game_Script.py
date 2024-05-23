import pygame
import random
from sys import exit

pygame.init()
pygame.mixer.init()
pygame.font.init()

killcount = 0
font = pygame.font.Font(None, 36)
title_text = font.render(f"Ninja Night", True, (200,255,200))
kill_count = font.render(f"Kills: {killcount}", True, (200,255,200))
screen = pygame.display.set_mode((900, 450))
pygame.display.set_caption('Ninja Night')
clock = pygame.time.Clock()

# Game music
# music = pygame.mixer.music.load()
# Game over screen
game_over = pygame.image.load('Game_over_screen.png')
game_over_scaled = pygame.transform.scale(game_over, (900,450))


# sky
sky_surf = pygame.image.load('Skyline.jpg')

# ground
ground_surf = pygame.image.load('Ground1.jpg').convert_alpha()
ground_rect = ground_surf.get_rect(midbottom = (450, 520))

# sun
sun_surf = pygame.Surface((100, 100), pygame.SRCALPHA)
sun_color = (255, 165, 0)
sun_center = (50, 50) 
sun_radius = 35
pygame.draw.circle(sun_surf, sun_color, sun_center, sun_radius)

# trees
tree_surf1 = pygame.image.load('Tree1.png').convert_alpha()
tree_surf2 = pygame.image.load('Tree2.png').convert_alpha()
tree_surf3 = pygame.image.load('Tree3.png').convert_alpha()

# enemies
enemy_hit_Counter = 0
enemy_surf1 = pygame.image.load('Zombie1.png').convert_alpha()
enemy_surf2 = pygame.image.load('Zombie2.png').convert_alpha()
enemy_surf3 = pygame.image.load('Zombie3.png').convert_alpha()
enemy_surf4 = pygame.image.load('Zombie4.png').convert_alpha()
enemy_surf1_flip = pygame.transform.flip(enemy_surf1, True, False)
enemy_surf2_flip = pygame.transform.flip(enemy_surf2, True, False)
enemy_surf3_flip = pygame.transform.flip(enemy_surf3, True, False)
enemy_surf4_flip = pygame.transform.flip(enemy_surf4, True, False)
enemy_rect1 = enemy_surf1.get_rect(midbottom = (400, ground_rect.top + 10))
current_enemy_surf = enemy_surf1

# player 1
playerHealth = 100
current_player_surf = pygame.image.load('NinjaStatic.png').convert_alpha()
attack_surf1 = pygame.image.load('NinjaAttack1.png').convert_alpha()
attack_surf2 = pygame.image.load('NinjaAttack2.png')
attack_surf1_left = pygame.transform.flip(attack_surf1, True, False)
attack_surf2_left = pygame.transform.flip(attack_surf2, True, False)
running_surf1 = pygame.image.load('NinjaRunning1.png').convert_alpha()
running_surf2 = pygame.image.load('NinjaRunning2.png').convert_alpha()
player_surf = pygame.image.load('NinjaStatic.png').convert_alpha()
player_surf1 = pygame.image.load('NinjaStatic.png').convert_alpha()
running_surf1_left = pygame.transform.flip(running_surf1, True, False)
running_surf2_left = pygame.transform.flip(running_surf2, True, False)
player_rect = player_surf.get_rect(midbottom = (80, ground_rect.top))
player_gravity = 0

player_animation_counter = 0
enemy_frame_rate = 20  # Number of frames per switch
enemy_animation_counter = 0
game_over = False


# Main Game Loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE and player_rect.colliderect(ground_rect):
        player_gravity = -15
  
  # enemy animation
  if player_rect.x <= enemy_rect1.x:
    enemy_rect1.x -= 1
    enemy_animation_counter += 1
    if enemy_animation_counter % enemy_frame_rate == 0:
      if current_enemy_surf == enemy_surf1_flip:
          current_enemy_surf = enemy_surf2_flip
      elif current_enemy_surf == enemy_surf2_flip:
          current_enemy_surf = enemy_surf3_flip
      elif current_enemy_surf == enemy_surf3_flip:
          current_enemy_surf = enemy_surf4_flip
      else:
          current_enemy_surf = enemy_surf1_flip
  else:
    enemy_rect1.x += 1
    enemy_animation_counter += 1
    if enemy_animation_counter % enemy_frame_rate == 0:
      if current_enemy_surf == enemy_surf1:
          current_enemy_surf = enemy_surf2
      elif current_enemy_surf == enemy_surf2:
          current_enemy_surf = enemy_surf3
      elif current_enemy_surf == enemy_surf3:
          current_enemy_surf = enemy_surf4
      else:
          current_enemy_surf = enemy_surf1
  
  # player animation
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_RIGHT and player_rect.colliderect(ground_rect):
      player_animation_counter += 1
      if player_animation_counter % 3 == 0:
        player_surf = running_surf1
      else:
        player_surf = running_surf2
      player_rect.x += 5
  else: player_surf = player_surf1
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_LEFT and player_rect.colliderect(ground_rect):
      player_animation_counter += 1
      if player_animation_counter % 3 == 0:
        player_surf = running_surf1_left
      else:
        player_surf = running_surf2_left
      player_rect.x -= 5
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_UP:
      player_animation_counter += 1
      if player_animation_counter % 3 == 0:
        player_surf = attack_surf1
      else: player_surf = attack_surf2
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_DOWN:
      player_animation_counter += 1
      if player_animation_counter % 3 == 0:
        player_surf = attack_surf1_left
      else: player_surf = attack_surf2_left
  
  # Attack event
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_UP and player_rect.colliderect(enemy_rect1):
       enemy_hit_Counter += 1
    else:
       print("miss")
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_DOWN and player_rect.colliderect(enemy_rect1):
       enemy_hit_Counter += 1
    else:
       print("miss")
  if enemy_hit_Counter == 5:
      print("hit")
      killcount += 1
      enemy_hit_Counter = 0
  if player_rect.colliderect(enemy_rect1) and event.type != pygame.KEYDOWN:
     print('-health')
     playerHealth -= .25
  if playerHealth <= 0:
     sky_surf = game_over_scaled
    
      
  kill_count = font.render(f"Kills: {killcount}", True, (200,255,200))
  player_health = font.render(f"Health: {playerHealth}", True, (200,255,200))
  screen.blit(sky_surf, (0,0))
  screen.blit(ground_surf, ground_rect)
  screen.blit(sun_surf, (100, 50)) 
  screen.blit(tree_surf1, (100, 250))
  screen.blit(tree_surf2, (300, 160))
  screen.blit(current_enemy_surf, enemy_rect1)
  screen.blit(title_text, (10, 10))
  screen.blit(kill_count, (450, 100))
  screen.blit(player_health, (450, 30))
  

  player_gravity += 1
  player_rect.y += player_gravity
  if player_rect.bottom >= 450:
      player_rect.bottom = 450
  screen.blit(player_surf, player_rect)
  screen.blit(tree_surf3, (550, 300))


        
  pygame.display.update() 
  clock.tick(60)
