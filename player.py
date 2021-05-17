# IMPORTS
import pygame
import random
from data import *
from word import *

""" Ce fichier contient la classe Player """

# class qui contient le joueur
class Player(pygame.sprite.Sprite):
    """ Cette classe crée un joueur """

    def __init__(self, name, number, game, specials_words, weakness, screen):
        super().__init__()
        self.weakness = weakness
        self.name = name
        self.portrait = pygame.transform.scale( pygame.image.load("characters/" + self.name + "/portrait/portrait.png"), (200,200))
        self.IQ = 100
        self.IQ_verif = 100
        self.number = number
        self.voice = [ pygame.mixer.Sound("characters/" + self.name + "/voice/voice_1.ogg"), pygame.mixer.Sound("characters/" + self.name + "/voice/voice_2.ogg")]
        self.special = False
        self.game = game
        self.final = False
        self.words = []
        self.screen = screen
        self.words_special = specials_words
        self.dead = [ "characters/" + self.name + "/dead/dead_1.png", "characters/" + self.name + "/dead/dead_2.png", "characters/" + self.name + "/dead/dead_3.png", "characters/" + self.name + "/dead/dead_4.png", "characters/" + self.name + "/dead/dead_5.png", "characters/" + self.name + "/dead/dead_6.png", "characters/" + self.name + "/dead/dead_7.png", "characters/" + self.name + "/dead/dead_8.png"]
        if number == 1:
            self.static = pygame.transform.scale( pygame.image.load("characters/" + self.name + "/static.png"), (200,200) )
            self.image = pygame.transform.scale( pygame.image.load("characters/" + self.name + "/static.png"), (200,200) )
            self.rect = self.image.get_rect()
            self.rect.x = 300
            self.rect.y = HEIGTH - 350
            self.finalbutton = Button(50, HEIGTH-130, 'elements/button.png')
            self.textblock = [ pygame.image.load('elements/player_block.png') , 50, 150 ]
        if number == 2:
            self.static = pygame.transform.flip(pygame.transform.scale( pygame.image.load("characters/" + self.name + "/static.png"), (200,200) ), 180, 0)
            self.image = pygame.transform.flip(pygame.transform.scale( pygame.image.load("characters/" + self.name + "/static.png"), (200,200) ), 180, 0)
            self.rect = self.image.get_rect()
            self.rect.x = 850
            self.rect.y = HEIGTH - 350
            self.finalbutton = Button(1200 , HEIGTH-130, 'elements/button.png')
            self.textblock = [ pygame.image.load('elements/player_block.png') , 1050, 150 ]

    def display(self, enemy):
        """ Cette fonction met à jour les états du joueur """
        # si le QI du joueur  est différent du QI qu'il avait avant, c'est qu'il à été blessé
        if self.IQ != self.IQ_verif:
            # on joue le son de blessure
            pygame.mixer.Sound("sounds/hurted.ogg").play()
            # on appelle la fonction du jeu qui affiche les images du joueur blessé
            self.game.hurt_player(self.screen, self)
            # on remet le QI de vérification égal au QI   
            self.IQ_verif = self.IQ 
        # si le joueur utilise son spécial
        if self.special:
            # on appelle la fonction du jeu qui affiche les images du joueur quand il utilise son spécial
            self.game.idea_player(self.screen, self)
            # on appelle la fonction du spécial
            self.idea()
            # le spécial n'est plus utilisé
            self.special = False
            # on perd du QI
            self.IQ -= 5
        # si le joueur valide sa phrase
        if self.final:
            # on appelle la fonction du jeu qui affiche les images du joueur quand il valide sa phrase
            self.final_word(enemy)
            # le final n'est plus utilisé
            self.final = False
        # si la longueur de la phrase est de plus de 10 mots
        if len(self.words) > 10:
            # on appelle la fonction de phrase trop longues
            self.error_message("Too long sentence ! (-5 IQ)")
            # on supprime le mot qui vient d'être ajouté
            self.words.pop(len(self.words)-1)
            
    def final_word(self, enemy):
        """ Cette fonction est appellée quand le joueur valide sa phrase. Elle vérifie si la phrase est correcte """
        # si la phrase est vide ( qu'il n'y a pas de phrase donc )
        if len(self.words) == 0:
            # on appelle la fonction d'erreur
            self.error_message("No sentence ! (IQ - 5)")
        # si la phrase n'est pas vide
        else:
            # mais que la phrase finit par un mot de liaison
            if self.words[len(self.words) - 1].element == "link":
                # on appelle la fonction d'erreur
                self.error_message("You can't finish like that! (IQ - 5)")
            # on appelle la fonction du jeu qui joue les sons avec un random des voix du personnage
            self.game.play_sound(self.voice[random.randint(0,1)])
            # on appelle la fonction du jeu qui anime le final d'un joueur
            self.game.final_player(self.screen, self)
            # on appelle la fonction qui attaque l'ennemi
            self.attack(enemy)
            # pause de 1s
            pygame.time.wait(1000)
            # on appelle la fonctions qui vide la phrase du joueur
            self.reset()
        # le joueur a joué donc on incrémente le tour du jeu
        self.game.turn += 1

    def QIbar(self, surface):
        """ Cette fonction affiche et met à jour la barre de QI du joueur """
        # le QI du joueur ne peut pas être inférieur à zéro
        if self.IQ < 0:
            self.IQ = 0
        # si c'est le joueur 1
        if self.number == 1:
            # on affiche sa barre de QI à l'emplacement du conteneur 1
            surface.blit(pygame.transform.scale( pygame.image.load('elements/IQ.png'), (int(self.IQ * 2.45), 34) ), (253, HEIGTH - 87))
        # si c'est le joueur 2
        if self.number == 2:
            # on affiche sa barre de QI à l'emplacement du conteneur 2
            surface.blit(pygame.transform.scale( pygame.image.load('elements/IQ.png'), (int(self.IQ * 2.45), 34) ), (883, HEIGTH - 87))

    def add_word(self, word):
        """ Cette fonction ajoute le mot qu'on lui donne à la phrase du joueur après 
        avoir vérifié qu'il correspond à la phrase """
        # si la fonction de vérification renvoie True, c'est que le mot correspond à la phrase
        if self.check_word(word):
            # on l'ajoute à la phrase
            self.words.append(word)
            # on return True pour dire qu'il n'y a pas d'erreur grammaticale
            return True
    
    def check_word(self, word):
        """ Cette fonction vérifie si le mot qu'on lui donne correspond à au modèle d'une phrase
        en fonction de la phrase du joueur. Elle vérifie beaucoup de conditions mais au moins la
        phrase sera correcte dans tout les cas """
        # si la phrase n'est pas vide
        if len(self.words) != 0:
            # si l'avant dernier mot est un sujet
            if self.words[len(self.words) - 2].element == "subject":
                # si le dernier mot est un objet
                if self.words[len(self.words) - 1].element == "object":
                    # si le mot est un verbe ou un mot de liaison
                    if word.element == "verb" or word.element == "link":
                        # on peut l'ajouter à la phrase
                        return True
                    # sinon
                    else:
                        # on return False qui provoquera une erreur grammaticale
                        return False
                # sinon si le dernier mot est un verbe
                elif self.words[len(self.words) - 1].element == "verb":
                    # si le mot est un objet, un mot de liaison ou un sujet
                    if word.element == "object" or word.name == "link" or word.element == "subject":
                        # on peut l'ajouter à la phrase
                        return True
                    # sinon
                    else:
                        # on return False
                        return False
                # sinon si le dernier mot est un mot de liaison
                elif self.words[len(self.words) - 1].element == "link":
                    # si le mot est un sujet ou un verbe
                    if word.element == "subject" or word.element == "verb":
                        # on peut l'ajouter à la phrase
                        return True
                    # sinon
                    else:
                        # on return False
                        return False
            # sinon si l'avant dernier mot est un objet
            if self.words[len(self.words) - 2].element == "object":
                # si le dernier mot est un mot de liaison
                if self.words[len(self.words) - 1].element == "link":
                    # si le mot est un sujet
                    if word.element == "subject":
                        # on peut l'ajouter à la phrase
                        return True
                    # sinon
                    else:
                        # on return False
                        return False
                # si le dernier mot est un verbe
                if self.words[len(self.words) - 1].element == "verb":
                    # si le mot est un sujet
                    if word.element == "subject":
                        # on peut l'ajouter à la phrase
                        return True
                    # sinon
                    else:
                        # on return False
                        return False
            # sinon si l'avant dernier mot est un verbe
            if self.words[len(self.words) - 2].element == "verb":
                # si le dernier mot est un sujet
                if self.words[len(self.words) - 1].element == "subject":
                    # si le mot est un objet ou un mot de liaison
                    if word.element == "object" or word.element == "link":
                        # on peut l'ajouter à la phrase
                        return True
                    # sinon
                    else:
                        # on return False
                        return False
                # sinon si le dernier mot est un mot de liaison
                if self.words[len(self.words) - 1].element == "link":
                    # si le mot est un verbe ou un sujet
                    if word.element == "verb" or word.element == "subject":
                        # on peut l'ajouter à la phrase
                        return True
                    # sinon
                    else:
                        # on return False
                        return False
                # sinon si le dernier mot est un objet
                if self.words[len(self.words) - 1].element == "object":
                    # si le mot est un mot de liaison
                    if word.element == "link":
                        # on peut l'ajouter à la phrase
                        return True
                    # sinon
                    else:
                        # on return False
                        return False
            # sinon si l'avant dernier mot est un mot de liaison
            if self.words[len(self.words) - 2].element == "link":
                # et que le dernier mot est un verbe
                if self.words[len(self.words) - 1].element == "verb":
                    # si le mot est un sujet ou un objet
                    if word.element == "subject" or word.element == "object":
                        # on peut l'ajouter à la phrase
                        return True
                    # sinon
                    else:
                        # on return False
                        return False
            # si le dernier mot est un lien
            if self.words[len(self.words) - 1].element == "link":
                # si le mot est un sujet ou un verbe
                if word.element == "subject" or word.element == "verb":
                    # on peut l'ajouter à la phrase
                    return True
                # sinon
                else:
                    # on return False
                    return False
            # si le dernier mot est un objet
            if self.words[len(self.words) - 1].element == "object":
                # si le mot est un mot de liaison ou un verbe
                if word.element == "link" or word.element == "verb":
                    # on peut l'ajouter à la phrase
                    return True
                # sinon
                else:
                    # on return False
                    return False
            # si le dernier mot est un sujet
            if self.words[len(self.words) - 1].element == "subject":
                # si le mot est un mot de liaison, un verbe ou un objet
                if word.element == "link" or word.element == "verb" or word.element == "object":
                    # on peut l'ajouter à la phrase
                    return True
                # sinon
                else:
                    # on return False
                    return False
        # sinon si la phrase est vide
        else:
            # le seul mot accepté est le sujet
            if word.element == "subject":
                # on peut l'ajouter à la phrase
                return True
            # sinon
            else:
                # on return False
                return False

    def reset(self):
        """ Cette fonction parcours la liste de mot du joueur et les supprime """
        for i in range(0, len(self.words)):
            self.words.pop(0)

    def idea(self):
        """ Cette fonction s'occupe du spécial du joueur """
        # on parcours la liste de mots spéciaux du joueur
        for i in self.words_special:
            # si le mot est compatible avec la phrase
            if self.check_word(i):
                # on l'ajoute à la phrase
                self.words.append(i)
                # on arrête la boucle car on ne veut ajouter qu'un seul mot à la phrase
                break
    
    def attack(self, enemy):
        """ Cette fonction s'occupe de l'attaque du joueur, elle prend en paramètre le joueur ennemi """
        # on met la variable de dégâts à zéro
        damage = 0
        # on parcours la phrase du joueur
        for i in self.words:
            # si le type du mot est la faiblesse de l'ennemi
            if enemy.weakness == i.type:
                # on ajoute à la variable de dégâts les dégâts du mot multipliés par deux
                damage += i.damage * 2
                # on change l'erreur du warningblock
                self.game.warningblock.message = "Weakness ( damage x2 )"
                # on affiche l'erreur
                self.game.error = True
            # sinon
            else:
                # on ajoute à la variable de dégâts les dégâts du mot
                damage += i.damage
        # on soustrait au QI de l'ennemi le nombre de dégâts
        enemy.IQ -= damage
    
    def error_message(self, message):
        """ Cette fonction est appelée en cas d'erreur commise, elle change le message 
        du warningblock avec celui qu'elle prend en paramètre et retire du QI au joueur """
        # le joueur perd du QI
        self.IQ -= 5
        # on change le message du warningblock
        self.game.warningblock.message = message
        # on affiche l'erreur
        self.game.error = True

    def sentence_update(self, number):
        """ Cette fonction met à jour la phrase du joueur """
        # si la phrase n'est pas vide et que sa longueur est inférieure ou égale à 10
        if len(self.words) > 0 and len(self.words) <= 10:
            # on affiche le mot à la position donnée
            # la position est calculée de façon à ce que le mot soit centré
            self.screen.blit(self.words[number].text_name[0], (self.textblock[1] + 120 - len(self.words[number].name) * 4,180 + (number * 25)))
            # si la phrase est plus longue que le chiffre en paramètre +1
            if len(self.words) > (number+1):
                # on l'a rappelle en incrémentant le nombre
                self.sentence_update((number+1))
