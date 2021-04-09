import pygame
import time
from random import randint

pygame.init()

# Initialisation des variables.
# Taille de la fenêtre principale.
windowW = 650
windowH = 750
# Images utilisées.
fond = pygame.image.load("img/background.jpg")
imgPerso = pygame.image.load("img/fusee.png")
# Taille des images utilisées
persoW = 50
persoH = 66
# Sons utilisés.
son = pygame.mixer.Sound("sound/tir.wav")
tiren = pygame.mixer.Sound("sound/tirennemi.wav")
tirboss = pygame.mixer.Sound("sound/tirboss.wav")
boom = pygame.mixer.Sound("sound/explosion.wav")
boomboss = pygame.mixer.Sound("sound/boss.wav")
vieperso = pygame.mixer.Sound("sound/persovie.wav")
pygame.mixer.music.load("sound/musique.wav")
# Initialisation de variables d'options de jeu.
vitesseGlobale = 5
# Initialisation de l'horloge
horloge = pygame.time.Clock()
# Initialisation de la couleur
white = (255, 255, 255)


# Déclaration de la classe missile et de ses fonctions.
class Missile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.imgTir = pygame.image.load("img/tir.png")
        self.tailleMissileHauteur = 24
        self.tailleMissileLargeur = 14
        self.posXmissile = x + persoW / 2
        self.posYmissile = y - 25
        self.vitesseMissile = 2 * vitesseGlobale

    def updateY(self):
        self.posYmissile = self.posYmissile - self.vitesseMissile

    def draw(self, window):
        window.blit(self.imgTir, (self.posXmissile, self.posYmissile))

    def isAlive(self):
        if self.posYmissile < -10:
            return True

# Déclaration de la classe permettant aux ennemies de tirer de gauche à droite


class MissileEnnemiDiagInv():
    def __init__(self, x, y):

        self.imgTir = pygame.image.load("img/tirennemidiagg.png")
        self.tailleMissileHauteur = 24
        self.tailleMissileLargeur = 14
        self.posXmissile = x + persoW / 2
        self.posYmissile = y + 70
        self.vitesseMissile = 2 * vitesseGlobale

    def updateDiagInv(self):
        self.posXmissile = self.posXmissile - vitesseGlobale
        self.posYmissile = self.posYmissile + vitesseGlobale
        if (self.posXmissile < 0):
            self.posXmissile = windowW

    def draw(self, window):
        window.blit(self.imgTir, (self.posXmissile, self.posYmissile))

    def isAlive(self):
        if self.posYmissile > 960:
            return True

# Déclaration de la classe permettant aux ennemies de tirer de droite à gauche


class MissileEnnemiDiag():
    def __init__(self, x, y):

        self.imgTir = pygame.image.load("img/tirennemidiagd.png")
        self.tailleMissileHauteur = 24
        self.tailleMissileLargeur = 14
        self.posXmissile = x + persoW / 2
        self.posYmissile = y + 70
        self.vitesseMissile = 2 * vitesseGlobale

    def updateDiag(self):
        self.posXmissile = self.posXmissile + vitesseGlobale
        self.posYmissile = self.posYmissile + vitesseGlobale
        if (self.posXmissile > 650):
            self.posXmissile = 0

    def draw(self, window):
        window.blit(self.imgTir, (self.posXmissile, self.posYmissile))

    def isAlive(self):
        if self.posYmissile > 960:
            return True

# déclaration de la classe permettant aux ennemies de tirer tout droit


class MissileEnnemi():
    def __init__(self, x, y):
        self.imgTir = pygame.image.load("img/tirennemi.png")
        self.tailleMissileHauteur = 24
        self.tailleMissileLargeur = 14
        self.posXmissile = x + persoW / 2
        self.posYmissile = y + 70
        self.vitesseMissile = vitesseGlobale

    def updateY(self):
        self.posYmissile = self.posYmissile + self.vitesseMissile

    def draw(self, window):
        window.blit(self.imgTir, (self.posXmissile, self.posYmissile))

    def isAlive(self):
        if self.posYmissile > 960:
            return True

# Déclaration de la classe des énnemeis de base pour la gauche


class EnnemiBaseGauche(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imgEnemBase = pygame.image.load("img/ennemi.png")
        self.enembaseW = 50
        self.enembaseH = 66
        self.posXenembase = 0
        self.posYenembase = 0
        self.vitesseenembase = vitesseGlobale / 2
        self.apparitionX = 2.5
        self.apparitionY = 2.5
        self.touchable = False
        self.imgExplosion = pygame.image.load("img/boom.png")

    def draw(self, window):
        window.blit(self.imgEnemBase, (self.posXenembase, self.posYenembase))

    def touche(self, missile):
        if missile.posXmissile + missile.tailleMissileLargeur > self.posXenembase and (
                missile.posXmissile < self.posXenembase + self.enembaseW) and (
                missile.posYmissile + missile.tailleMissileHauteur > self.posYenembase) and (
                missile.posYmissile < self.posYenembase + self.enembaseH):
            return True

    def drawExplosion(self, window):
        window.blit(self.imgExplosion, (self.posXenembase, self.posYenembase))

# Déclaration de la classe des énnemeis de base pour la droite


class EnnemiBaseDroite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imgEnemBase = pygame.image.load("img/ennemi.png")  # Trouver un vrai image
        self.enembaseW = 50
        self.enembaseH = 66
        self.posXenembase = 650
        self.posYenembase = 0
        self.vitesseenembase = vitesseGlobale / 2
        self.apparitionX = 2.5
        self.apparitionY = 2.5
        self.touchable = False
        self.imgExplosion = pygame.image.load("img/boom.png")
        self.afficheEx = False

    def draw(self, window):
        window.blit(self.imgEnemBase, (self.posXenembase, self.posYenembase))

    def touche(self, missile):
        if missile.posXmissile + missile.tailleMissileLargeur > self.posXenembase and (
                missile.posXmissile < self.posXenembase + self.enembaseW) and (
                missile.posYmissile + missile.tailleMissileHauteur > self.posYenembase) and (
                missile.posYmissile < self.posYenembase + self.enembaseH):
            return True


class Boss(pygame.sprite.Sprite):
    def __init__(self):
        self.imgBoss = pygame.image.load("img/boss.png")
        self.bossW = 60
        self.bossH = 70
        self.posXboss = 295
        self.posYboss = -80
        self.vitesseBoss = vitesseGlobale
        self.apparitionY = 4
        self.touchable = False
        self.imgExplosion = pygame.image.load("img/boomboss.png")
        self.afficheEx = False

    def draw(self, window):
        window.blit(self.imgBoss, (self.posXboss, self.posYboss))

    def touche(self, missile):
        if missile.posXmissile + missile.tailleMissileLargeur > self.posXboss and (
                missile.posXmissile < self.posXboss + self.bossW) and (
                missile.posYmissile + missile.tailleMissileHauteur > self.posYboss) and (
                missile.posYmissile < self.posYboss + self.bossH):
            return True


class Personnage():
    def __init__(self, x, y):
        self.imgPerso = pygame.image.load("img/fusee.png")
        self.positionX = x
        self.positionY = y
        self.persoW = 50
        self.persoH = 72
        self.vie = 5
        self.touchable = True

    def updatePosPer(self, a, b):
        self.positionX = self.positionX + a
        self.positionY = self.positionY + b

    def draw(self, window):
        window.blit(self.imgPerso, (self.positionX, self.positionY))

    def isOver(self):
        if self.positionY < 0 or self.positionY + self.persoH > windowH - 10 or self.positionX < -10 or self.positionX + self.persoW > windowW + 25:
            return True

    def getPx(self):
        return self.positionX

    def getPy(self):
        return self.positionY

    def getVie(self):
        return self.vie

    def touche3(self, boss):
        if boss.posXboss + boss.bossW > self.positionX and (boss.posXboss < self.positionX + self.persoW) and (
                boss.posYboss + boss.bossW > self.positionY) and (boss.posYboss < self.positionY + self.persoH):
            return True

    def touche2(self, ennemi):
        if ennemi.posXenembase + ennemi.enembaseW > self.positionX and (
                ennemi.posXenembase < self.positionX + self.persoW) and (
                ennemi.posYenembase + ennemi.enembaseW > self.positionY) and (
                ennemi.posYenembase < self.positionY + self.persoH):
            return True

    def touche(self, missile):
        if missile.posXmissile + missile.tailleMissileLargeur > self.positionX and (
                missile.posXmissile < self.positionX + self.persoW) and (
                missile.posYmissile + missile.tailleMissileHauteur > self.positionY) and (
                missile.posYmissile < self.positionY + self.persoH):
            return True

    """"		
class Explosion:
	def __init__(self, win, pos):
		self.pos = pos
		self.frames = 100
		self.current_frame = 0
		self.image = pygame.image.load("img/boom.png")
		self.win = win
	
	def is_finish(self):
		if self.current_frame > self.frames:
			return True
	
	def draw(self):
		self.win.blit(self.image,self.pos)
		self.current_frame += 1
"""


# Ouverture de la fenêtre principale.
fenetre = pygame.display.set_mode((windowW, windowH))
pygame.display.set_caption("Rocket Shooter")
pygame.mixer.music.play(loops=-1)


# Fonction de jeu principale.
def gameLoop():
    # Coordonnées des éléments du jeu.
    persoX = 325
    persoY = 630
    # Coordonnées pour le déplacement du joueur.
    deplacementY = 0
    deplacementX = 0

    game_over = False
    missile = []
    ennemibased = []
    ennemibaseg = []
    boss = []
    missilea = []
    missileb = []
    missilec = []
    joueur = Personnage(persoX, persoY)
    vie = joueur.getVie()
    score = 20
    esquiveD = 5
    esquiveG = -5
    esquiveB = 5
    tir = 0
    boomXD = 0
    boomYD = 0
    tourBoomD = 0
    afficheBoomdroite = False
    liste_explosions = []
    liste_explosionsG = []
    liste_explosionsB = []
    imagedroite = 0
    boomXG = 0
    boomYG = 0
    tourBoomG = 0
    afficheBoomgauche = False
    imagegauche = 0
    boomXB = 0
    boomYB = 0
    tourBoomB = 0
    afficheBoomboss = False
    imageboss = 0
    tirboss = 0
    joueurtouche = 0
    couldownTir = 0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    deplacementX = 6
                if event.key == pygame.K_LEFT:
                    deplacementX = -6
                if event.key == pygame.K_UP:
                    deplacementY = -6
                if event.key == pygame.K_DOWN:
                    deplacementY = 6
                if event.key == pygame.K_SPACE and couldownTir > 10:
                    missile1 = Missile(joueur.getPx(), joueur.getPy())
                    missile.append(missile1)
                    son.play()
                    couldownTir = 0
                    tir = 0
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    deplacementX = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    deplacementY = 0

        joueur.updatePosPer(deplacementX, deplacementY)
        couldownTir = couldownTir + 1
        joueurtouche = joueurtouche + 1
        vie = joueur.getVie()
        imagedroite = imagedroite + 1
        imagegauche = imagegauche + 1
        imageboss = imageboss + 1
        tirboss = tirboss + 1
        fenetre.blit(fond, (0, 0))
        # Affichage du perso.
        joueur.draw(fenetre)

        if (joueurtouche > 200):
            joueur.touchable = True
        # On gère si nos missiles sortent de la carte + leur affichage
        for m in missile:
            m.updateY()
            m.draw(fenetre)
            if (m.isAlive() == True):
                del missile[0]

        # Pour les missiles ennemies droit: affichage + sortie de map  + touche joueur
        for m in missilea:
            m.updateY()
            m.draw(fenetre)
            if (joueur.touche(m) == True and joueur.touchable == True):
                vieperso.play()
                joueur.vie = joueur.vie - 1
                joueur.positionX = 325
                joueur.positionY = 630
                joueur.touchable = False
            if (m.isAlive() == True):
                del missilea[0]

        # Pour les missiles ennemies diag droite: affichage + sortie de map  + touche joueur
        for m in missileb:
            m.updateDiag()
            m.draw(fenetre)
            if (joueur.touche(m) == True and joueur.touchable == True):
                vieperso.play()
                joueur.vie = joueur.vie - 1
                joueur.positionX = 325
                joueur.positionY = 630
                joueur.touchable = False
            if (m.isAlive() == True):
                del missileb[0]

        # Pour les missiles ennemies diag gauche: affichage + sortie de map  + touche joueur
        for m in missilec:
            m.updateDiagInv()
            m.draw(fenetre)
            if (joueur.touche(m) == True and joueur.touchable == True):
                vieperso.play()
                joueur.vie = joueur.vie - 1
                joueur.positionX = 325
                joueur.positionY = 630
                joueur.touchable = False
            if (m.isAlive() == True):
                del missilec[0]

        # Si aucun ennemie à droite n'est présent alors on en ajoute un
        if not ennemibased:
            ennemi1 = EnnemiBaseDroite()
            ennemibased.append(ennemi1)

        # Pour chaque ennemie de droite: affichage + position + touche + tir
        for e in ennemibased:
            e.draw(fenetre)
            e.posXenembase = e.posXenembase - e.apparitionX
            if (joueur.touche2(e) and e.touchable == True):
                score = score + 1
                del ennemibased[0]
                vieperso.play()
                joueur.vie = joueur.vie - 1
                joueur.positionX = 325
                joueur.positionY = 630
                joueur.touchable = False
            if (e.posXenembase < 400):
                e.apparitionX = 0
            e.posYenembase = e.posYenembase + e.apparitionY
            if (e.posYenembase > 50):
                e.apparitionY = 0
            if (e.apparitionX == 0 and e.apparitionY == 0):
                e.touchable = True
            for m in missile:
                if (
                        e.posXenembase - 30 < m.posXmissile and m.posXmissile < e.posXenembase + 80 and e.touchable == True):
                    if (e.posXenembase + 80 > 650):
                        esquiveD = -esquiveD
                    if (e.posXenembase < 360):
                        esquiveD = -esquiveD
                    e.posXenembase = e.posXenembase + esquiveD
                if e.touche(m) and e.touchable:
                    imagedroite = 0
                    del ennemibased[0]
                    boom.play()
                    score = score + 1
                    afficheBoomdroite = True
                    boomXD = e.posXenembase
                    boomYD = e.posYenembase

            if imagedroite > 10:
                afficheBoomdroite = False
            if (e.posXenembase - 80 < joueur.getPx() + joueur.persoW and joueur.getPx() < e.posXenembase + 130):
                test = randint(0, 29)
                if (test == 1):
                    missile1 = MissileEnnemi(e.posXenembase, e.posYenembase)
                    missilea.append(missile1)
                    tiren.play()

        # apparition du boss
        if (score % 20 == 0 and len(boss) == 0 and score != 0):
            boss1 = Boss()
            boss.append(boss1)

        # On gère les événements du boss
        for b in boss:
            b.draw(fenetre)
            b.posYboss = b.posYboss + b.apparitionY
            if (joueur.touche3(b) and b.touchable == True):
                vieperso.play()
                joueur.vie = joueur.vie - 1
                joueur.positionX = 325
                joueur.positionY = 630
                joueur.touchable = False
            if (b.posYboss > 0):
                b.apparitionY = 0
            if (b.apparitionY == 0):
                b.touchable = True
            for m in missile:
                if (b.posXboss - 30 < m.posXmissile and m.posXmissile < b.posXboss + 90 and b.touchable == True):
                    if (b.posXboss + 70 > 630):
                        esquiveB = -esquiveB
                    if (b.posXboss < 10):
                        esquiveB = -esquiveB
                    b.posXboss = b.posXboss + esquiveB

                if b.touche(m) and b.touchable:
                    imageboss = 0
                    del boss[0]
                    score = score + 5
                    boomboss.play()
                    afficheBoomboss = True
                    boomXB = b.posXboss
                    boomYB = b.posYboss

            if tirboss > 50:
                missile1 = MissileEnnemi(b.posXboss, b.posYboss)
                missilea.append(missile1)
                missile2 = MissileEnnemiDiag(b.posXboss, b.posYboss)
                missileb.append(missile2)
                missile3 = MissileEnnemiDiagInv(b.posXboss, b.posYboss)
                missilec.append(missile3)
                tirboss = 0

        # Si aucun ennemie à gauche n'est présent alors on en ajoute un
        if not ennemibaseg:
            ennemi2 = EnnemiBaseGauche()
            ennemibaseg.append(ennemi2)

        # Pour chaque ennemie de gauche: affichage + position + touche + tir
        for e in ennemibaseg:
            e.draw(fenetre)
            e.posXenembase = e.posXenembase + e.apparitionX
            if (joueur.touche2(e) and e.touchable == True):
                score = score + 1
                del ennemibaseg[0]
                vieperso.play()
                joueur.vie = joueur.vie - 1
                joueur.positionX = 325
                joueur.positionY = 630
                joueur.touchable = False
            if (e.posXenembase > 200):
                e.apparitionX = 0
            e.posYenembase = e.posYenembase + e.apparitionY
            if (e.posYenembase > 50):
                e.apparitionY = 0
            if (e.apparitionX == 0 and e.apparitionY == 0):
                e.touchable = True
            for m in missile:
                if (
                        e.posXenembase - 30 < m.posXmissile and m.posXmissile < e.posXenembase + 80 and e.touchable == True):
                    if (e.posXenembase + 60 > 300):
                        esquiveG = -esquiveG
                    if (e.posXenembase < 10):
                        esquiveG = -esquiveG
                    e.posXenembase = e.posXenembase + esquiveG
                if e.touche(m) and e.touchable:
                    imagegauche = 0
                    del ennemibaseg[0]
                    score = score + 1
                    afficheBoomgauche = True
                    boomXG = e.posXenembase
                    boomYG = e.posYenembase

            if (e.posXenembase - 80 < joueur.getPx() + joueur.persoW and joueur.getPx() < e.posXenembase + 130):
                test = randint(0, 29)
                if (test == 1):
                    missile1 = MissileEnnemi(e.posXenembase, e.posYenembase)
                    missilea.append(missile1)
                    tiren.play()

        # Si le joueur sort de la map alors il perd une vie
        if (joueur.isOver() == True):
            joueur.vie = joueur.vie - 1
            joueur.positionX = 325
            joueur.positionY = 630

        # Si le joueur n'a plus de vie alors le jeu est finis
        if (joueur.vie == 0):
            displayMessage("You lose ! Try again.", 60, windowW / 2, windowH / 2 - 50)
            displayMessage("Appuyer sur une touche pour continuer.", 20, windowW / 2, windowH / 2 + 50)
            game_over = True

        displayMessage("SCORE : " + str(score), 15, 40, 20)
        strVie = ""
        for i in range(0, vie):
            strVie += "█"
        displayMessage("VIES : " + strVie, 15, windowW - 60, 20)

        pygame.display.update()
        horloge.tick(100)

    if playAgain() == True:
        gameLoop()


# Fonction qui affiche du texte.
def displayMessage(text, fontSize, x, y):
    font = pygame.font.Font('font/homespun.ttf', fontSize)
    img = font.render(text, True, white)
    displayRect = img.get_rect()
    displayRect.center = (x, y)
    fenetre.blit(img, displayRect)


# méthode pour jouer de nouveau, si on appuie sur une touche, on rejoue
def playAgain():
    time.sleep(1)
    while True:
        for event in pygame.event.get([pygame.KEYDOWN, pygame.QUIT]):
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key != pygame.K_ESCAPE:
                    return True
                else:
                    pygame.quit()
        horloge.tick()


"""
Ce qui nous reste à faire:
-Faire esquiver l'ennemi dans certaines conditions
-Plus d'ennemis

"""

gameLoop()
pygame.quit()
quit()
