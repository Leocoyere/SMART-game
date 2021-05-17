# IMPORTS
import pygame
from player import *
from word import *
import random

# classe qui contient le jeu
class Game:

    def __init__(self, screen):
        # ÉCRAN TITRE
        self.logo = pygame.image.load( "assets/elements/logo.png" )
        self.start = Button((WIDTH/2 - 41 -100), (HEIGTH/2 + 62.5 + 43), "assets/elements/play.png")
        self.contact = Button((WIDTH/2 - 41 +100), (HEIGTH/2 + 62.5 + 43), "assets/elements/contact.png")
        self.settings = Button((WIDTH/2 - 41), (HEIGTH/2 + 62.5 + 43), "assets/elements/settings.png")
            # MENU CONTACT
        self.contact_menu = False
        
        # ÉCRAN CHOIX DU PERSONNAGE
        self.character1 = Characterblock(screen, "conny", (200), (HEIGTH/2 - 100))
        self.character2 = Characterblock(screen, "leroy", (400 + 183), (HEIGTH/2 - 100))
        self.character3 = Characterblock(screen, "max", (WIDTH - 400), (HEIGTH/2 - 100))
        self.character_number = 1
        self.choose_1 = False
        self.choose_2 = False
            # ÉCRAN DESCRIPTION DU PERSONNAGE
        self.character1_cv = CharacterCV(screen, "conny", "This cute bunny left his burrow at the age of 16 to go to college.He is the smartest in his class and never stops learning.He dreams of becoming a great physician to   launch rockets into space, but before that he will have to fill his gaps on animals.")
        self.character2_cv = CharacterCV(screen, "leroy", "Son of two famous matematicians, his path was traced even before his birth.After    long studies in mathematics,he decided to take an interest in quantum physics. He   loves to discover the new secrets of his  world and his brain thirsts for knowledge. Used to living in his shell, he has a    phobia of the great outdoors, don't talk  to him about space, he might not recover..")
        self.character3_cv = CharacterCV(screen, "max", "Geographer for 5 years, he decided to     leave everything to leran ecology. He is  now an activist and fights for the        protection of the planet. You better      respect the blue planet or he will come   for you and trust me, you don't want that.If there is one thing he hates, it's of   course pollution.")
        self.description_1 = False
        self.description_2 = False
        # JOUEURS
        self.player_1 = None
        self.player_2 = None
        # WORDS
            # FINALS
        self.thats = Word("final",", that's logic !",0, "final")
        self.sure = Word("final","i'm sure of it !",0, "final")
        self.about = Word("final",", what about this ?",0, "final")
        self.einstein = Word("final",", ask Einstein !",0, "final")
        self.machine = Word("final",", i am a machine !",0, "final")
            # SUBJECTS
        self.mammal = Word("subject","the mammals", 4, "animals")
        self.north = Word("subject","the north pole", 4, "geography")
        self.factory = Word("subject","a gas factory", 4, "pollution")
        self.dinosaur = Word("subject","the dinosaurs", 4, "animals")
        self.curie = Word("subject","Marie Curie", 4, "celebrity")
        self.system = Word("subject","a system", 4, "statitics")
        self.volcano = Word("subject","a volcano", 4, "geography")
        self.velocity = Word("subject","the velocity", 4, "science")
        self.planet = Word("subject","the planet", 4, "space")
        self.nuclear = Word("subject","a central", 4, "pollution")
        self.newton = Word("subject","Isaac Newton", 4, "celebrity")
        self.stratosphere = Word("subject","the stratosphere",4, "space")
        self.moon = Word("subject","the moon",4, "space")
        self.hole = Word("subject","a black hole",4, "space")
        self.peninsula = Word("subject","the peninsula",4, "geography")
        self.ozone = Word("subject","the ozone",4, "space")
            # VERBS
        self.increase = Word("verb","increase", 2, "verb")
        self.reverse = Word("verb","reverse", 2, "verb")
        self.split = Word("verb","split", 2, "verb")
        self.decrease = Word("verb","decrease", 2, "verb")
        self.combust = Word("verb","combust", 2, "verb")
        self.merge = Word("verb","merge", 2, "verb")
        self.vanish = Word("verb","vanished", 2, "verb")
        self.created = Word("verb","created", 2, "verb")
        self.discover = Word("verb","discover", 2, "verb")
        self.froze = Word("verb","froze", 2, "verb")
        self.radiate = Word("verb","radiate", 2, "verb")
        self.spreads = Word("verb","spreads", 2, "verb")
        self.destroys = Word("verb","destroys", 2, "verb")
        self.grow = Word("verb","grow", 2, "verb")
        self.boil = Word("verb","boil", 2, "verb")
            # OBJECTS
        self.phreatic = Word("object","phreatic zone", 3, "geography")
        self.atoms = Word("object","atoms", 3, "science")
        self.life = Word("object","life expectancy", 3, "statitics")
        self.gravity = Word("object","gravity",3, "space")
        self.mucous = Word("object","mucous membrane", 3, "science")
        self.contagious = Word("object","contagious germs", 3, "science")
        self.mortality = Word("object","mortality rate", 3, "statitics")
        self.plastic = Word("object","plastic production", 3, "pollution")
        self.dna = Word("object","DNA", 3, "science")
        self.warming = Word("object","global warming",3, "pollution")
        self.diseases = Word("object","diseases",3, "science")
        self.neurons = Word("object","neurons",3, "science")
        self.poverty = Word("object","poverty",3, "statitics")
        self.statistics = Word("object","statistics",3, "statitics")
        self.energy = Word("object","energy",3, "science")
            # LINKS
        self.et = Word("link","and",1, "links")
        # ALL WORDS
        self.verbs = [self.increase, self.decrease, self.radiate, self.spreads, self.destroys,self.grow, self.boil, self.vanish, self.created, self.froze, self.reverse, self.split, self.combust, self.merge]
        self.subjects = [self.mammal,self.planet,self.nuclear,self.newton,self.stratosphere,self.peninsula,self.ozone, self.factory, self.dinosaur, self.curie, self.system, self.velocity, self.volcano, self.north, self.moon, self.hole]
        self.objects = [self.warming, self.phreatic,self.dna,self.diseases,self.neurons,self.poverty,self.statistics,self.energy, self.life, self.mucous, self.contagious, self.mortality, self.plastic, self.atoms, self.gravity]
        self.links = [ self.et ]
        self.final = [self.thats, self.sure, self.about, self.einstein, self.machine]
        # DATABASE
        self.database = Database(screen)
        self.turn = 2
        # WARNING BLOCK
        self.warningblock = Warningblock(screen)
        self.error = False
        # PAUSE BLOCK
        self.menu = Pauseblock(screen, self)
        self.paused = False
        # SCREENS
        self.main = True
        self.match = False
        # END OF GAME
        self.end = False
        # SOUNDS
        self.sound = True
        self.fight_theme = pygame.mixer.Sound("assets/sounds/theme.ogg")
        self.main_theme = pygame.mixer.Sound("assets/sounds/main_theme.ogg")
        self.open = pygame.mixer.Sound("assets/sounds/open.ogg")
        self.close = pygame.mixer.Sound("assets/sounds/close.ogg")
        self.select = pygame.mixer.Sound("assets/sounds/select.ogg")
        self.play = pygame.mixer.Sound("assets/sounds/start.ogg")

    # FUNCTIONS #
    
    def character(self, screen, number):
        """ Cette fonction affiche les informations sur un des personnages jouables """
        if number == 1:
            if self.sound:
                pygame.mixer.Sound("assets/sounds/boing.ogg").play()
            self.character1_cv.display()
        elif number == 2:
            if self.sound:
                pygame.mixer.Sound("assets/sounds/boing.ogg").play()
            self.character2_cv.display()
        elif number == 3:
            if self.sound:
                pygame.mixer.Sound("assets/sounds/boing.ogg").play()
            self.character3_cv.display()
            
    def characters_list(self, screen):
        """ Cette fonction affiche la liste des personnages jouables """
        screen.fill((0,150,200))
        if self.choose_1:
            screen.blit( pygame.image.load( "assets/elements/choose_1.png" ), (WIDTH/2 - 281, 50) )
        elif self.choose_2:
            screen.blit( pygame.image.load( "assets/elements/choose_2.png" ), (WIDTH/2 - 281, 50) )
        screen.blit( self.character1.image, self.character1.rect )
        screen.blit( self.character2.image, self.character2.rect )
        screen.blit( self.character3.image, self.character3.rect )
        self.character1.display()
        self.character2.display()
        self.character3.display()
        screen.blit( self.settings.image, (self.settings.rect.x, HEIGTH - 50 - 43 ))
        self.menu.display()

    def add_word(self, button, player):
        """ Cette fonction ajoute un mot à la phrase d'un joueur et le retire de la database """
        # on appelle la fonction de vérification du joueur
        verification = player.add_word(button.number)
        if verification:
            # si la vérification est bonne, on ajoute le mot à la phrase du joueur
            player.add_word(button.number)
            # et enlever le mot de la database
            self.database.words.remove(button.number)
            # le joueur a joué donc on incrémente le tour
            self.turn += 1
        else:
            # si la vérification n'est pas bonne, on appelle la fonction d'erreur
            player.error_message("Grammatical error ! (-5 IQ)")
            # le joueur a joué donc on incrémente le tour
            self.turn += 1

    def play_sound(self, sound):
        """ Cette fonction joue le son qu'on lui donne à condition que le son du jeu sois activé """
        if self.sound:
            sound.play()
    
    def title(self, screen):
        """ Cette fonction affiche l'écran titre """
        screen.fill((0,150,200)) # couleur de fond
        screen.blit( self.logo, ( WIDTH/2 - 167, HEIGTH/2 - 62.5) ) # logo
        screen.blit( self.start.image, self.start.rect ) # bouton start
        screen.blit( self.contact.image, self.contact.rect ) # bouton contact
        screen.blit( self.settings.image, self.settings.rect ) # bouton options

    def word_generator(self):
        """" Cette fonction choisis des mots au hasard parmis les catégories qu'on lui donne """
        tab = [self.subjects, self.subjects, self.objects, self.subjects, self.links, self.verbs] # toutes les catégories
        random.shuffle(tab) # on mélange la liste
        # si la database n'est pas vide
        if len(self.database.words) > 0:
            for j in self.database.words:
                for i in tab:
                    v = random.randint(0,(len(i)-1)) # numéro choisi au hasard dans la catégorie donnée
                    # si le mot choisi au hasard est différent des mots présents dans la database
                    if i[v] != j:
                        # et que la longueur de la database est de 6 ou moins
                        if len(self.database.words) <= 5:
                            # on ajoute le mot à la database
                            self.database.words.append(i[v])
        # si la database est vide
        else:
            # pas besoin de vérifier les mots à l'intérieur
            for i in tab:
                v = random.randint(0,(len(i)-1)) # numéro choisi au hasard dans la catégorie donnée
                # on ajoute le mot à la database
                self.database.words.append(i[v])

    def contacts(self, screen):
        """ Cette fonction affiche le menu contact """
        screen.blit( pygame.image.load("assets/elements/contact_menu.png"), (WIDTH/2 - 223,HEIGTH/2 - 220) ) # bloc de fond
        screen.blit( pygame.image.load("assets/elements/linkedin.png"), (WIDTH/2 - 223 + 100 - 35,HEIGTH/2 - 220 + 100 - 35) ) # logo linkedin
        screen.blit( pygame.image.load("assets/elements/linkedin_name.png"), (WIDTH/2 - 223 + 70 + 108 + 20 - 35,HEIGTH/2 - 220 + 100 - 35 + 16) ) # nom linkedin
        screen.blit( pygame.image.load("assets/elements/github.png"), (WIDTH/2 - 223 + 100 - 35,HEIGTH/2 + 90 - 100 - 34) ) # logo github
        screen.blit( pygame.image.load("assets/elements/github_name.png"), (WIDTH/2 - 223 + 71 + 108 + 20 - 35,HEIGTH/2 + 90 - 100 - 34 + 17) ) # nom github

    def end_game(self, screen, dead, notdead):
        """ Cette fonction affiche la fin du jeu, elle prend en paramètres le joueur mort, et le joueur encore en vie """
        for i in dead.dead: # on affiche les images du personnage mort dans une boucle
            screen.fill((0,150,200)) # couleur de fond
            # si le joueur 1 est mort
            if dead.number == 1:
                # on affiche son image
                screen.blit( pygame.transform.scale(pygame.image.load(i), (200,200)), dead.rect )
            # si le joueur 2 est mort
            elif dead.number == 2:
                # on affiche son image retournée
                screen.blit( pygame.transform.flip(pygame.transform.scale(pygame.image.load(i), (200,200)), 180, 0), dead.rect )
            # on affiche l'image du joueur encore en vie
            screen.blit( notdead.image, notdead.rect )
            # on affiche le bouton du menu pause
            screen.blit( self.menu.button.image, self.menu.button.rect )
            # on affiche les conteneurs des barres de QI des deux personnages
            screen.blit( pygame.image.load( "assets/elements/IQ_bar.png" ), (200, HEIGTH - 100) )
            screen.blit( pygame.image.load( "assets/elements/IQ_bar.png" ), ( 830, HEIGTH - 100 ) )
            dead.QIbar(screen) # et on
            notdead.QIbar(screen) # les remplit
            # on change le message du warningblock avec le nom du joueur gagnant
            self.warningblock.message = "Player " + str(notdead.number) + " won the game!"
            # on affiche le warningblock
            screen.blit( self.warningblock.image, self.warningblock.rect )
            self.menu.display()
            self.warningblock.display()
            # on rafraîchit l'écran
            pygame.display.flip()
            # pause de 150ms
            pygame.time.wait(150)
        # pause de 1s
        pygame.time.wait(1000)
        self.reset_all()
        self.main = True
        self.fight_theme.stop()
        self.main_theme.play()
        
    def update(self, screen):
        """ Cette fonction met l'écran du jeu à jour """
        # si le son est désactivé, on stop les musiques
        if self.sound == False:
            self.main_theme.stop()
            self.fight_theme.stop()
        # si l'écran titre est en cours
        if self.main:
            # on appelle la fonction qui affiche l'écran titre
            self.title(screen)
            # si le menu contact est activé
            if self.contact_menu:
                # on appelle la fonction qui l'affiche
                self.contacts(screen)
        # si un des menus de choix est activé
        elif self.choose_1 or self.choose_2:
            # on appelle la fonction de la liste des personnages
            self.characters_list(screen)
        # si un des menus de description est activé
        elif self.description_1 or self.description_2:
            # on appelle la fonction qui l'affiche
            self.character(screen, self.character_number)
        # si le match est en cours
        elif self.match:
            # si la database est vide
            if len(self.database.words) == 0:
                # on appelle la fonctions qui génère de nouveaux mots
                self.word_generator()
            # si le tour est pair
            if self.turn % 2 == 0:
                # c'est le tour du joueur 1
                self.player_turn(screen, self.player_1, self.player_2)
            # si le tour est impair
            else:
                # c'est le tour du joueur 2
                self.player_turn(screen, self.player_2, self.player_1)
        # si le jeu est sur pause
        if self.paused:
            # on appelle la fonction pause
            self.is_paused(screen)
    
    def message(self, screen):
        """" Cette fonction affiche un message bloc quand un joueur fait une erreur """
        # si il y a une erreur
        if self.error:
            # on affiche le bloc d'erreur
            screen.blit( self.warningblock.image, self.warningblock.rect )
            # et on appelle la fonction qui met le bloc à jour
            self.warningblock.display()
            # on rafraichît l'écran
            pygame.display.flip()
            # pause de 1.5s
            pygame.time.wait(1500)
            # l'erreur à été affichée, on peut l'enlever
            self.error = False

    def reset_all(self):
        """ Cette fonction annule tout les menus en cours """
        self.choose_1 = False
        self.choose_2 = False
        self.description_1 = False
        self.description_2 = False
        self.main = False
        self.match = False
        self.paused = False
        self.contact_menu = False
        self.error = False
        self.end = False

    def new_match(self, screen):
        """ Cette fonction crée un nouveau match """
        # on reset tout les menus
        self.reset_all()
        # le match est en cours
        self.match = True
        # on coupe la music de l'écran titre
        self.main_theme.stop()
        # et on lance celle du match
        self.fight_theme.play(-1)
        # nouvelle database
        self.database = Database(screen)
        # réinitialisation du tour
        self.turn = 2
        # nouveau warningblock
        self.warningblock = Warningblock(screen)

    def player_turn(self, screen, isplaying, isnotplaying):
        """ Cette fonction prend deux joueurs en paramètres, elle affiche le tour du joueur en train de jouer """
        # si un des joueurs est à 0
        if isplaying.IQ == 0:
            # on appelle la fonction qui affiche la fin du jeu avec en paramètre le joueur mort et le joueur vivant
            self.end_game(screen, isplaying, isnotplaying)         
        elif isnotplaying.IQ == 0:
            # on appelle la fonction qui affiche la fin du jeu avec en paramètre le joueur mort et le joueur vivant
            self.end_game(screen, isnotplaying, isplaying)
        # si les deux joueurs sont en vie 
        else:
            # on appelle la fonction qui met les joueurs à jour
            isplaying.display(isnotplaying)
            isnotplaying.display(isplaying)
            screen.fill((0,150,200)) # couleur de fond
            # on affiche les images des deux joueurs
            screen.blit( isplaying.image, isplaying.rect )
            screen.blit( isnotplaying.image, isnotplaying.rect )
            # on affiche les blocs de texte des joueurs
            screen.blit( isplaying.textblock[0], (isplaying.textblock[1], isplaying.textblock[2] ))
            screen.blit( isnotplaying.textblock[0], (isnotplaying.textblock[1], isnotplaying.textblock[2] ))
            # on affiche le bouton pause
            screen.blit( self.menu.button.image, self.menu.button.rect )
            # on appelle les fonctions qui mettent les joueurs à jour
            isplaying.sentence_update(0)
            isnotplaying.sentence_update(0)
            # on affiche tout les mots de la database
            self.database.all_buttons.draw(screen)
            # on appelle la fonction qui met la database à jour
            self.database.display(0)
            # on affiche le bouton de validation du joueur en train de jouer
            screen.blit(isplaying.finalbutton.image, isplaying.finalbutton.rect)

            # on affiche les conteneurs des barres de QI des deux personnages
            screen.blit( pygame.image.load( "assets/elements/IQ_bar.png" ), (200, HEIGTH - 100) )
            screen.blit( pygame.image.load( "assets/elements/IQ_bar.png" ), ( 830, HEIGTH - 100 ) )
            isplaying.QIbar(screen) # et on
            isnotplaying.QIbar(screen) # les remplit
            # on appelle la fonction qui met à jour le message d'erreur
            self.message(screen)
        
    """ Les trois fonctions suivantes affichent les images d'un joueur quand il est blessé,
        qu'il utilise son spécial, ou qu'il valide sa phrase. Pour ça j'utilise un for qui 
        affiche une liste d'image en même temps que les éléments du jeu """

    def hurt_player(self, screen, player_hurted):
        """ Cette fonction s'occupe d'animer un joueur quand il est blessé """
        for i in range(1,5):
            screen.fill((0,150,200)) # couleur de fond
            # si c'est le joueur 1
            if player_hurted.number == 1:
                # on affiche normalement son image
                screen.blit( pygame.transform.scale(pygame.image.load("assets/" + player_hurted.name + "/hurt/hurt_" + str(i) + ".png"), (200, 200)), player_hurted.rect )
                # et on affiche l'image du joueur 2
                screen.blit( self.player_2.image, self.player_2.rect )
            # si c'est le joueur 2
            elif player_hurted.number == 2:
                # on affiche son image retournée
                screen.blit( pygame.transform.flip( pygame.transform.scale(pygame.image.load("assets/" + player_hurted.name + "/hurt/hurt_" + str(i) + ".png"), (200, 200)), 180, 0), player_hurted.rect )
                # et on affiche l'image du joueur 1
                screen.blit( self.player_1.image, self.player_1.rect )
            # on affiche les blocs de texte des deux joueurs
            screen.blit( self.player_1.textblock[0], (self.player_1.textblock[1], self.player_1.textblock[2] ))
            screen.blit( self.player_2.textblock[0], (self.player_2.textblock[1], self.player_2.textblock[2] ))
            # on affiche le bouton pause
            screen.blit( self.menu.button.image, self.menu.button.rect )
            # on appelle les fonctions qui mettent les phrases des joueurs à jour
            self.player_1.sentence_update(0)
            self.player_2.sentence_update(0)
            # on affiche tout les mots de la database
            self.database.all_buttons.draw(screen)
            # on appelle la fonction qui met la database à jour
            self.database.display(0)

            # on affiche les conteneurs des barres de QI des deux personnages
            screen.blit( pygame.image.load( "assets/elements/IQ_bar.png" ), (200, HEIGTH - 100) )
            screen.blit( pygame.image.load( "assets/elements/IQ_bar.png" ), ( 830, HEIGTH - 100 ) )
            self.player_1.QIbar(screen) # et on
            self.player_2.QIbar(screen) # les remplit
            # on rafraichît l'écran
            pygame.display.flip()
            # pause de 100ms
            pygame.time.wait(100)

    def idea_player(self, screen, player_idea):
        """ Cette fonction s'occupe d'animer un joueur quand il utilise son spécial """
        # À peu près la même chose que la fonction hurt_player ci-dessus
        for i in range(1,4):
            screen.fill((0,150,200))
            if player_idea.number == 1:
                screen.blit( pygame.transform.scale(pygame.image.load("assets/" + player_idea.name + "/idea/idea_" + str(i) + ".png"), (200, 200)), player_idea.rect )
                screen.blit( self.player_2.image, self.player_2.rect )
            elif player_idea.number == 2:
                screen.blit( pygame.transform.flip( pygame.transform.scale(pygame.image.load("assets/" + player_idea.name + "/idea/idea_" + str(i) + ".png"), (200, 200)), 180, 0), player_idea.rect )
                screen.blit( self.player_1.image, self.player_1.rect )
            screen.blit( self.player_1.textblock[0], (self.player_1.textblock[1], self.player_1.textblock[2] ))
            screen.blit( self.player_2.textblock[0], (self.player_2.textblock[1], self.player_2.textblock[2] ))
            screen.blit( self.menu.button.image, self.menu.button.rect )
            self.player_1.sentence_update(0)
            self.player_2.sentence_update(0)
            self.database.all_buttons.draw(screen)
            self.database.display(0)

            screen.blit( pygame.image.load( "assets/elements/IQ_bar.png" ), (200, HEIGTH - 100) )
            self.player_1.QIbar(screen)
            screen.blit( pygame.image.load( "assets/elements/IQ_bar.png" ), ( 830, HEIGTH - 100 ) )
            self.player_2.QIbar(screen)
            pygame.display.flip()
            pygame.time.wait(200)
        
        
    def final_player(self, screen, player_final):
        """ Cette fonction s'occupe d'animer un joueur quand il valide sa phrase """
        # À peu près la même chose que la fonction hurt_player ci-dessus
        word = self.final[random.randint(0,(len(self.final)-1))]
        screen.fill((0,150,200))
        screen.blit( self.player_1.image, self.player_1.rect )
        screen.blit( self.player_2.image, self.player_2.rect )
        screen.blit( self.player_1.textblock[0], (self.player_1.textblock[1], self.player_1.textblock[2] ))
        screen.blit( self.player_2.textblock[0], (self.player_2.textblock[1], self.player_2.textblock[2] ))
        screen.blit( word.text_name[0], ((player_final.textblock[1] + 120 - len(word.name) * 4),(475)) )
        screen.blit( self.menu.button.image, self.menu.button.rect )
        self.player_1.sentence_update(0)
        self.player_2.sentence_update(0)
        self.database.all_buttons.draw(screen)
        self.database.display(0)

        screen.blit( pygame.image.load( "assets/elements/IQ_bar.png" ), (200, HEIGTH - 100) )
        self.player_1.QIbar(screen)
        screen.blit( pygame.image.load( "assets/elements/IQ_bar.png" ), ( 830, HEIGTH - 100 ) )
        self.player_2.QIbar(screen)
        pygame.display.flip()

    def is_paused(self, screen):
        """ Cette fonction affiche le menu pause quand le jeu est sur pause """
        screen.blit(self.menu.image, self.menu.rect) # bloc de fond
        screen.blit(self.menu.home.image, self.menu.home.rect) # bouton home
        screen.blit(self.menu.sound.image, self.menu.sound.rect) # bouton son
        screen.blit(self.menu.resume.image, self.menu.resume.rect) # bouton resume