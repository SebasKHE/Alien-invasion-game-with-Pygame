import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import os
def run_game():

    #inicializamos el juego y creamos un objeto pantalla

    pygame.init()
    
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_heigth))
    pygame.display.set_caption("Alien Invasion")
    

    #cREATE AN INSTANCE TO STOER GAME STATISICS
    stats = GameStats(ai_settings)


    #Make a ship

    ship = Ship(ai_settings, screen)
    #Make a group to store bullets in
    bullets = Group()
    bullets_aliens = Group()
    aliens = Group()

    #Make the play button.
    play_button = Button (ai_settings, screen, "Play")

    sb = Scoreboard(ai_settings, screen, stats)

    #Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens, bullets)

    if os.path.exists("stats.txt"):
        if os.path.getsize("stats.txt") > 0:
            with open("stats.txt", "r") as save_stats:
                recuperar = save_stats.read().strip()
                stats.high_score = int(recuperar)

    # comenzamos el bucle principal para el juego   
    while True:

        
        #Make a ship
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, bullets_aliens)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
                
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, bullets_aliens)
        
        
       

run_game()