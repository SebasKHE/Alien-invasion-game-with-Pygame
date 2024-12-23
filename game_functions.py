import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien
from random import randint



def check_keydown_events (event, ai_settings, screen, ship, bullets, stats, play_button, aliens):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    if event.key == pygame.K_p:
        check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, None, None)    
            
def fire_bullet(ai_settings, screen, ship, bullets):
    #cREATE A NEW BULLET AND ADD IT TO THE BULLETS GRUOP
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

    
def check_events (ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, ):
    """Respon to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open ("stats.txt", "w") as save_stats:
                save_stats.write(str(stats.high_score))
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets, stats, play_button, aliens)
            
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)
        
def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Start a anew game when the player clicks Play."""
    
    button_clicked = mouse_x is not None and play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked or mouse_x is None and not stats.game_active:
        #reset the gamae settings
        ai_settings.initialize_dynamic_settings()
        

        #hide the mouse cursor.
        pygame.mouse.set_visible(False)

        #Reset game statistics
        stats.reset_stats()    
        stats.game_active = True

        #Reset the scoreboardimages
        sb.prep_images()

    
        #Empty the list of alines and bullets.
        aliens.empty()
        bullets.empty()

        #Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens, bullets)
        ship.center_ship()
    
    

def update_screen (ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, alien_bullets):

    screen.fill (ai_settings.bg_color)  #redibujar la pantalla durante cada bucle con el color dado
    #Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    for bullet in alien_bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    
    #draw the score information
    sb.show_score()

    #Draw the play button if the game is inactigve
    if not stats.game_active:
        play_button.draw_button()

    #hacer que se vea la el dibujo de pantalla mas reciente    
    pygame.display.flip()



def check_keyup_events (event, ship):
    """Respond to RELEASES"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets):
    """Updating position of bullets and get rid of old bullets"""
    
    # Update player's bullets
    bullets.update()

    # Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

    # Update alien bullets
    alien_bullets.update()

    # Get rid of alien bullets that have disappeared
    for bullet in alien_bullets.copy():
        if bullet.rect.top > ai_settings.screen_height:
            alien_bullets.remove(bullet)

    # Check for any collisions (bullets hitting aliens, etc.)
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)
    check_alies_bullet_collision_ship(ai_settings, stats, sb, screen, ship, aliens, alien_bullets)
    

def check_bullet_alien_collisions (ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Respond to bullet alien collisions"""
    #Remove any bullets and aliens that have collided
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
        sb.prep_score()
        check_high_scores(stats, sb)
        
    if len(aliens) == 0:
        #If the entire fleet is destroyed, start a new level
        bullets.empty()
        ai_settings.increase_speed()

        #Increase level
        stats.level += 1
        sb.prep_level()
        
        create_fleet(ai_settings, screen, ship, aliens, bullets)

def check_alies_bullet_collision_ship(ai_settings, stats, sb, screen, ship, aliens, alien_bullets):
    collisions = pygame.sprite.spritecollide(ship, alien_bullets, True)  # True to remove bullet on collision
    if collisions:
        ship_hit(ai_settings, stats, sb, screen, ship, aliens, alien_bullets)
        
def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    
    #create an alien and place it in the row
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet (ai_settings, screen, ship, aliens, bullets):
    """Create a full fleet of aliens"""
    #Create an alien and find the number of aliens in a row
    #Spacing between eac alien is equal to one alien width
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

    aliens_shoot(aliens, bullets)

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen"""
    available_space_y = (ai_settings.screen_heigth - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

 
def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction (ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Respond to ship being hit by alien"""
    if stats.ships_left > 0:
        stats.ships_left -= 1

        #update scoreboard
        sb.prep_ships()

        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens, bullets)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """
    Check if the fleet is at an edge
    """
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

    #Look for alien_ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)

    #Look for aliens hitting the bottom of the screen
    check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)
    
def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Check if any aliens have reached the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #Treat this the same as if the ship got hit
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
            break

def check_high_scores(stats, sb):
    """Check to see if there's a new high score"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def aliens_shoot(aliens, bullets_aliens):
    """Allow aliens to shoot bullets randomly"""
    for alien in aliens:
        # Random chance to shoot
        if randint(1, 100) <= 50:  # 5% chance to shoot
            bullet = Bullet(aliens.sprites()[0].ai_settings, aliens.sprites()[0].screen, alien=alien)
            bullets_aliens.add(bullet)


