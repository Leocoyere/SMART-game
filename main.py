# IMPORTS
import pygame
from game import Game
from player import *
from data import *
from word import *

pygame.init()

# FENÊTRE DU JEU
pygame.display.set_caption( "SMART" )
screen = pygame.display.set_mode(( WIDTH,HEIGTH ))

# VARIABLES
game = Game(screen)
frame_per_second = pygame.time.Clock()
running = True

# Lancer la musique du jeu
game.main_theme.play(-1, 0)


while running:

    # mettre à jour le jeu
    game.update(screen)

    # rafraîchir le l'image du jeu
    pygame.display.flip()

    # évènements qui surviennent au cours du jeu
    for event in pygame.event.get():

        # si l'évènement est fermeture de la fenêtre
        if event.type == pygame.QUIT:
            # fermeture du jeu
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        
        # si l'évènement est un clic de la souris
        if event.type == pygame.MOUSEBUTTONDOWN:

            # si le match est en cours
            if game.match:
                # et que c'est le tour du joueur 1
                if game.turn % 2 == 0:
                    for button in game.database.all_buttons:
                        # si le joueur clique sur un des boutons de la database
                        if button.rect.collidepoint(event.pos):
                            game.add_word(button, game.player_1)

                    # si le bouton du final est cliqué
                    if game.player_1.finalbutton.rect.collidepoint(event.pos):
                        game.player_1.final = True
                    
                    # si le joueur clique sur son personnage
                    if game.player_1.rect.collidepoint(event.pos):
                        game.player_1.special = True

                # si ce n'est pas le tour du joueur 1, c'est celui du joueur 2        
                else:
                    for button in game.database.all_buttons:
                        # si le joueur clique sur un des boutons de la database
                        if button.rect.collidepoint(event.pos):
                            game.add_word(button, game.player_2)

                    # si le bouton du final est cliqué
                    if game.player_2.finalbutton.rect.collidepoint(event.pos):
                        game.player_2.final = True
                    
                    # si le joueur clique sur son personnage
                    if game.player_2.rect.collidepoint(event.pos):
                        game.player_2.special = True

            # si un le bouton du menu est cliqué
            if game.menu.button.rect.collidepoint(event.pos):
                game.play_sound(game.open)
                game.paused = True

            # si le jeu est sur pause
            if game.paused:
                # si le bouton du son est cliqué
                if game.menu.sound.rect.collidepoint(event.pos):
                    game.menu.sound_change()

                # si le bouton home est cliqué    
                if game.menu.home.rect.collidepoint(event.pos):
                    game.reset_all()
                    game.main_theme.stop()
                    game.fight_theme.stop()
                    game.main_theme.play(-1)
                    game.main = True

                # si le bouton resume est cliqué
                if game.menu.resume.rect.collidepoint(event.pos):
                    game.play_sound(game.close)
                    game.paused = False
            
            # si l'écran titre est en cours
            if game.main:
                # si le bouton start est cliqué
                if game.start.rect.collidepoint(event.pos):
                    game.play_sound(game.play)
                    game.reset_all()
                    game.choose_1 = True
                # si le bouton contact est cliqué
                if game.contact.rect.collidepoint(event.pos):
                    if game.contact_menu:
                        game.play_sound(game.close)
                        game.contact_menu = False
                    else:
                        game.play_sound(game.open)
                        game.contact_menu = True
                # si le bouton options est cliqué
                if game.settings.rect.collidepoint(event.pos):
                    game.play_sound(game.open)
                    game.paused = True

            # si l'écran de choix du joueur 1 est en cours
            elif game.choose_1:
                # si le joueur clique sur les infos du 1er personnage
                if game.character1.info.rect.collidepoint(event.pos):
                    game.play_sound(game.open)
                    game.character_number = 1
                    game.reset_all()
                    game.description_1 = True
                # si le joueur clique sur les infos du 2ème personnage
                if game.character2.info.rect.collidepoint(event.pos):
                    game.play_sound(game.open)
                    game.character_number = 2
                    game.reset_all()
                    game.description_1 = True
                # si le joueur clique sur les infos du 3ème personnage
                if game.character3.info.rect.collidepoint(event.pos):
                    game.play_sound(game.open)
                    game.character_number = 3
                    game.reset_all()
                    game.description_1 = True
                # si le joueur choisis sur le 1er personnage
                if game.character1.choose.rect.collidepoint(event.pos):
                    game.play_sound(game.select)
                    game.player_1 = Player("conny", 1, game, [ Word("subject", "a bunny", 4, "animals"), Word("verb", "studied", 4, "verb"), Word("link", "and", 4, "link") ], "animals", screen)
                    game.reset_all()
                    game.choose_2 = True
                # si le joueur choisis sur le 2ème personnage
                if game.character2.choose.rect.collidepoint(event.pos):
                    game.play_sound(game.select)
                    game.player_1 = Player("leroy", 1, game, [ Word("subject", "a turtle", 4, "animals"), Word("verb", "learned", 4, "verb"), Word("link", "and", 4, "link") ], "space", screen)
                    game.reset_all()
                    game.choose_2 = True
                # si le joueur choisis sur le 3ème personnage
                if game.character3.choose.rect.collidepoint(event.pos):
                    game.play_sound(game.select)
                    game.player_1 = Player("max", 1, game, [ Word("subject", "a dog", 4, "animals"), Word("verb", "taught", 4, "verb"), Word("link", "and", 4, "link") ], "pollution", screen)
                    game.reset_all()
                    game.choose_2 = True

            # si l'écran de choix du joueur 2 est en cours
            elif game.choose_2:
                # si le joueur clique sur les infos du 1er personnage
                if game.character1.info.rect.collidepoint(event.pos):
                    game.play_sound(game.open)
                    game.character_number = 1
                    game.choose_2 = False
                    game.description_2 = True
                # si le joueur clique sur les infos du 2ème personnage
                if game.character2.info.rect.collidepoint(event.pos):
                    game.play_sound(game.open)
                    game.character_number = 2
                    game.choose_2 = False
                    game.description_2 = True
                # si le joueur clique sur les infos du 3ème personnage
                if game.character3.info.rect.collidepoint(event.pos):
                    game.play_sound(game.open)
                    game.character_number = 3
                    game.choose_2 = False
                    game.description_2 = True
                # si le joueur choisis sur le 1er personnage
                if game.character1.choose.rect.collidepoint(event.pos):
                    game.play_sound(game.select)
                    game.player_2 = Player("conny", 2, game, [ Word("subject", "a bunny", 4, "animals"), Word("verb", "studied", 4, "verb"), Word("link", "and", 4, "link") ], "animals", screen)
                    game.new_match(screen)
                # si le joueur choisis sur le 2ème personnage
                if game.character2.choose.rect.collidepoint(event.pos):
                    game.play_sound(game.select)
                    game.player_2 = Player("leroy", 2, game, [ Word("subject", "a turtle", 4, "animals"), Word("verb", "learned", 4, "verb"), Word("link", "and", 4, "link") ], "space", screen)
                    game.new_match(screen)
                # si le joueur choisis sur le 3ème personnage
                if game.character3.choose.rect.collidepoint(event.pos):
                    game.play_sound(game.select) 
                    game.player_2 = Player("max", 2, game, [ Word("subject", "a dog", 4, "animals"), Word("verb", "taught", 4, "verb"), Word("link", "and", 4, "link") ], "pollution", screen)
                    game.new_match(screen)

            # si l'écran de description du joueur 1 est en cours
            elif game.description_1:
                # si le bouton de retour du personnage 1 est cliqué
                if game.character1_cv.back.rect.collidepoint(event.pos):
                    game.play_sound(game.close)
                    game.reset_all()
                    game.choose_1 = True
                # si le bouton de retour du personnage 2 est cliqué
                if game.character2_cv.back.rect.collidepoint(event.pos):
                    game.play_sound(game.close)
                    game.reset_all()
                    game.choose_1 = True
                # si le bouton de retour du personnage 3 est cliqué
                if game.character3_cv.back.rect.collidepoint(event.pos):
                    game.play_sound(game.close)
                    game.reset_all()
                    game.choose_1 = True
            
            # si l'écran de description du joueur 2 est en cours
            elif game.description_2:
                # si le bouton de retour du personnage 1 est cliqué
                if game.character1_cv.back.rect.collidepoint(event.pos):
                    game.play_sound(game.close)
                    game.reset_all()
                    game.choose_2 = True
                # si le bouton de retour du personnage 2 est cliqué
                if game.character2_cv.back.rect.collidepoint(event.pos):
                    game.play_sound(game.close)
                    game.reset_all()
                    game.choose_2 = True
                # si le bouton de retour du personnage 3 est cliqué
                if game.character3_cv.back.rect.collidepoint(event.pos):
                    game.play_sound(game.close)
                    game.reset_all()
                    game.choose_2 = True

    # FRAMES PER SECOND
    frame_per_second.tick(FPS)