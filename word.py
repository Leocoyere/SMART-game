# IMPORTS
import pygame
from data import *

# class des mots
class Word(pygame.sprite.Sprite):
    """ Cette classe crée un mot, le mot a un element, un type, un nom, et des dégâts propres à lui-même """
    
    def __init__(self, element, name, damage, type_word):
        super().__init__()
        self.name = name
        self.font_text = pygame.font.Font('assets/font/Passion_One/PassionOne-Regular.ttf', 25)
        self.text_name = [self.font_text.render(self.name, True, (255,255,255)), (369, 200)]
        self.element = element
        self.damage = damage
        self.type = type_word

# class du bloc d'erreur     
class Warningblock(pygame.sprite.Sprite):
    """ Cette classe crée un bloc qui affiche les différentes erreurs commises dans le jeu """

    def __init__(self, screen):
        super().__init__()
        self.message = ""
        self.image = pygame.image.load("assets/elements/warning.png")
        self.font_text = pygame.font.Font('assets/font/Passion_One/PassionOne-Regular.ttf', 25)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2 - 185 
        self.rect.y = HEIGTH / 2 - 149
        self.text = [self.font_text.render(self.message, True, (255,255,255)), ((self.rect.x + 182 - (len(self.message) * 5)), (self.rect.y + 100))]
        self.screen = screen
    
    def display(self):
        """ Cette fonction met à jour le message du bloc """
        self.text = [self.font_text.render(self.message, True, (255,255,255)), ((self.rect.x + 187 - (len(self.message) * 4.5)), (self.rect.y + 100))]
        self.screen.blit(self.text[0], self.text[1])

# class bouton
class Button(pygame.sprite.Sprite):
    """ Cette classe crée un bouton qui sera cliquable par la suite """
    
    def __init__(self, x, y, img):
        super().__init__()
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# class menu pause
class Pauseblock(pygame.sprite.Sprite):
    """ Cette classe crée le menu pause """
    
    def __init__(self, screen, game):
        super().__init__()
        self.image = pygame.image.load("assets/elements/pause_menu.png")
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2 - 162
        self.rect.y = HEIGTH / 2 - 156
        self.screen = screen
        self.game = game
        # boutons présents dans le menu
        self.button = Button((WIDTH/2 + -54), (HEIGTH - 130), "assets/elements/pause.png")
        self.home = Button((WIDTH/2 - 162 + 70), (HEIGTH/2 - 156 + 100), "assets/elements/home.png")
        self.sound = Button((WIDTH/2 + 162 - 70 - 82), (HEIGTH/2 - 156 + 100), "assets/elements/sound_on.png")
        self.resume = Button((WIDTH/2 + 75 - 153), (HEIGTH/2 - 156 + 100 + 30 + 68), "assets/elements/resume.png")

    def display(self):
        """ Cette fonction vérifie si le jeu est en pause, quand c'est le cas, elle affiche le menu pause """
        if self.game.paused:
            self.screen.blit(self.image, self.rect)
            self.screen.blit(self.home.image, self.home.rect)
            self.screen.blit(self.sound.image, self.sound.rect)
            self.screen.blit(self.resume.image, self.resume.rect)
    
    def sound_change(self):
        """ Cette fonction est destinée au bouton du son, elle est appellée quand le bouton est cliqué
        elle change l'image du bouton et met à jour le son du jeu """
        # si le son du jeu est activé
        if self.game.sound:
            # on change l'image du son
            self.sound.image = pygame.image.load("assets/elements/sound_off.png")
            # et on coupe le son du jeu
            self.game.sound = False
        # si le son est désactivé
        elif self.game.sound == False:
            # on change l'image du son
            self.sound.image = pygame.image.load("assets/elements/sound_on.png")
            # et on allume le son du jeu
            self.game.sound = True
            # si le match est en cours
            if self.game.match:
                # on joue la musique du match
                self.game.fight_theme.play(-1)
            # sinon
            else:
                # on joue la musique du thème principal
                self.game.main_theme.play(-1)

# class bouton conteneur de mot
class Wordbutton(pygame.sprite.Sprite):
    """ Cette classe crée un bouton destiné à contenir un mot """

    def __init__(self, number, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/elements/wordbutton.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.number = number

# class database
class Database(pygame.sprite.Sprite):
    """ Cette classe crée la database qui va contenir tout les mots à afficher """

    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load("assets/elements/wordbutton.png")
        self.base = ""
        self.words = []
        self.font = pygame.font.Font('assets/font/Passion_One/PassionOne-Regular.ttf', 20)
        self.text_pos = [ [self.font.render("", True, (33,33,33)), (150, 150)], [self.font.render("", True, (33,33,33)), (150, 150)], [self.font.render("", True, (33,33,33)), (150, 150)], [self.font.render("", True, (33,33,33)), (150, 150)], [self.font.render("", True, (33,33,33)), (150, 150)], [self.font.render("", True, (33,33,33)), (150, 150)], [self.font.render("", True, (33,33,33)), (150, 150)], [self.font.render("", True, (33,33,33)), (150, 150)] ]
        self.screen = screen
        self.rect = self.image.get_rect( center = ( 90,30 ) )
        self.rect.x = 90
        self.rect.y = 30
        self.all_buttons = pygame.sprite.Group()

    """        if len(self.words) > 0 and len(self.words) <= 10:
            # on affiche le mot à la position donnée
            # la position est calculée de façon à ce que le mot soit centré
            self.screen.blit(self.words[number].text_name[0], (self.textblock[1] + 120 - len(self.words[number].name) * 4,180 + (number * 25)))
            # si la phrase est plus longue que le chiffre en paramètre +1
            if len(self.words) > (number+1):
                # on l'a rappelle en incrémentant le nombre
                self.sentence_update((number+1)) """

    def display(self, number):
        """ Cette fonction affiche les mots de la database en les ajoutant dans des boutons """
        self.all_buttons = pygame.sprite.Group()
        for i in range(len(self.words)):
            if i == 0:
                self.screen.blit(self.words[0].text_name[0], (self.rect.x + 85 - len(self.words[0].name) * 4.6, self.rect.y + 20))
                self.all_buttons.add(Wordbutton( self.words[0], 90, 30 ))
            if i == 1:
                self.screen.blit(self.words[1].text_name[0], (self.rect.x + 200 + 85 - len(self.words[1].name) * 4.6, self.rect.y + 20))
                self.all_buttons.add(Wordbutton( self.words[1], 290, 30 ))
            if i == 2:
                self.screen.blit(self.words[2].text_name[0], (self.rect.x + 400 + 85 - len(self.words[2].name) * 4.6, self.rect.y + 20))
                self.all_buttons.add(Wordbutton( self.words[2], 490, 30 ))
            if i == 3:
                self.screen.blit(self.words[3].text_name[0], (self.rect.x + 600 + 85 - len(self.words[3].name) * 4.6, self.rect.y + 20))
                self.all_buttons.add(Wordbutton( self.words[3], 690, 30 ))
            if i == 4:
                self.screen.blit(self.words[4].text_name[0], (self.rect.x + 800 + 85 - len(self.words[4].name) * 4.6, self.rect.y + 20))
                self.all_buttons.add(Wordbutton( self.words[4], 890, 30 ))
            if i == 5:
                self.screen.blit(self.words[5].text_name[0], (self.rect.x + 1000 + 85 - len(self.words[5].name) * 4.6, self.rect.y + 20))
                self.all_buttons.add(Wordbutton( self.words[5], 1090, 30 ))

# class bloc de présentation du personnage
class Characterblock(pygame.sprite.Sprite):
    """ Cette classe crée le profil d'un personnage avec les boutons qui vont avec """

    def __init__(self, screen, name, x, y):
        super().__init__()
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load("assets/" + name + "/portrait/portrait.png"), (200,200))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.info = Button((self.rect.x + 50 - 41), (self.rect.y + 200 + 50 - 43), "assets/elements/info.png")
        self.choose = Button((self.rect.x + 200 - 50 - 41), (self.rect.y + 200 + 50 - 43), "assets/elements/valid.png")
    
    def display(self):
        self.screen.blit( self.info.image, self.info.rect)
        self.screen.blit( self.choose.image, self.choose.rect)

# class détails du personnage
class CharacterCV(pygame.sprite.Sprite):
    """ Cette classe crée l'écran de présentation du personnage """

    def __init__(self, screen, name, text):
        super().__init__()
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load( "assets/" + name + "/static.png" ), (200,200))
        self.jump = [ "assets/" + name + "/jump/jump_1.png", "assets/" + name + "/jump/jump_2.png", "assets/" + name + "/jump/jump_3.png", "assets/" + name + "/jump/jump_4.png", "assets/" + name + "/jump/jump_5.png", "assets/" + name + "/jump/jump_6.png", "assets/" + name + "/jump/jump_7.png", "assets/" + name + "/jump/jump_8.png" ]
        self.font = pygame.font.Font('assets/font/Passion_One/PassionOne-Regular.ttf', 25)
        self.weakness = pygame.image.load( "assets/" + name + "/weaknesses/weakness.png" )
        self.text = text
        self.name = pygame.image.load( "assets/" + name + "/name/" + name + ".png" )
        self.back = Button( (80 - 41), (80 - 42), "assets/elements/group.png")

    def display(self):
        """ Cette fonction affiche l'écran de présentation du personnage"""
        # on parcours les images du personnage
        for i in self.jump:
            number = 42 # le nombre de caractères affichés par ligne
            y = 125 # la position en y de la ligne
            self.screen.fill((0,150,200)) # couleur de fond
            # nom du personnage
            self.screen.blit( self.name, (WIDTH - 500 - 115, 100) )
            # l'image du personnage
            self.screen.blit( pygame.transform.scale(pygame.image.load( i ), (200,200)), ((400 - 100), (HEIGTH - 200 - 100)) )
            # on affiche le texte de présentation
            for j in range(int(len(self.text) / number)):
                self.screen.blit( self.font.render( self.text[number-42:number], True, (255,255,255) ), (WIDTH - 500 - 115, y + 68 ) )
                number += 42 # on incrémente le nombre
                y += 20 # on incrémente la position en y
            # on affiche l'image du bouton retour
            self.screen.blit( self.back.image, self.back.rect )
            # on affiche le tableau de faiblesse du personnage
            self.screen.blit( self.weakness, (WIDTH - 500 - 115, HEIGTH - 100 - 135) )
            # on rafraichît l'écran
            pygame.display.flip()
            # pause de 100ms pour l'animation de saut
            pygame.time.wait(100)
    