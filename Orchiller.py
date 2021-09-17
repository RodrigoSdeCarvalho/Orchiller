import os, sys
dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)
# -- Pra fazer o executável --

import math
import pygame
import random
pygame.init()

displayW = 800
displayH = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
orange = (255, 200, 0)

gameDisplay = pygame.display.set_mode((displayW, displayH))
pygame.display.set_caption('Killer Orchid!')
clock = pygame.time.Clock()

fundo = pygame.image.load('Imagens/Garden.png')

escudoImg = pygame.image.load('Imagens/Escudo.png')
escudoFogoImg = pygame.image.load('Imagens/EscudoFogo.png')
Luz = pygame.image.load('Imagens/iluminacao.png')
Escuridao = pygame.image.load('Imagens/escuridao.png')
auraCura = pygame.image.load('Imagens/auraCura.png')
auraCura2 = pygame.image.load('Imagens/auraCura2.png')
auraCura3 = pygame.image.load('Imagens/auraCura3.png')
danoImg = pygame.image.load('Imagens/dano.png')
coerulea1Img = pygame.image.load('Imagens/coerulea_1.png')
coerulea2Img = pygame.image.load('Imagens/coerulea_2.png')
cycnoches1Img = pygame.image.load('Imagens/cycnoches_1.png')
cycnoches2Img = pygame.image.load('Imagens/cycnoches_2.png')
cymbidium1Img = pygame.image.load('Imagens/cymbidium_1.png')
cymbidium2Img = pygame.image.load('Imagens/cymbidium_2.png')
caladenia1Img = pygame.image.load('Imagens/caladenia_1.png')
caladenia2Img = pygame.image.load('Imagens/caladenia_2.png')
waterDropImg = pygame.image.load('Imagens/waterDrop.png')
sporeImg = pygame.image.load('Imagens/spore.png')
thornImg = pygame.image.load('Imagens/thorn.png')
semente1Img = pygame.image.load('Imagens/semente1.png')
semente2Img = pygame.image.load('Imagens/semente2.png')
semente3Img = pygame.image.load('Imagens/semente3.png')
vine1Img = pygame.image.load('Imagens/vine1.png')
vine2Img = pygame.image.load('Imagens/vine2.png')
vine3Img = pygame.image.load('Imagens/vine3.png')
plantinha1Img = pygame.image.load('Imagens/plantinha1.png')
plantinha2Img = pygame.image.load('Imagens/plantinha2.png')
plantinha3Img = pygame.image.load('Imagens/plantinha3.png')
plantinha4Img = pygame.image.load('Imagens/plantinha4.png')
planta1Img = pygame.image.load('Imagens/planta.png')
planta2Img = pygame.image.load('Imagens/planta2.png')
planta3Img = pygame.image.load('Imagens/planta3.png')
montanhaImg = pygame.image.load('Imagens/montanha.png')

pimentaImg = pygame.image.load('Imagens/pimenta.png')
pimentaAzulImg = pygame.image.load('Imagens/pimenta_azul.png')
cerejaImg = pygame.image.load('Imagens/cereja.png')
cerejaAzulImg = pygame.image.load('Imagens/cereja_azul.png')
melancia1Img = pygame.image.load('Imagens/melancia-1.png')
melancia2Img = pygame.image.load('Imagens/melancia-2.png')
melancia3Img = pygame.image.load('Imagens/melancia-3.png')
tomateImg = pygame.image.load('Imagens/tomate.png')
pimentao1Img = pygame.image.load('Imagens/pimentao_1.png')
pimentao2Img = pygame.image.load('Imagens/pimentao_2.png')
maca1Img = pygame.image.load('Imagens/maca_1.png')
maca2Img = pygame.image.load('Imagens/maca_2.png')
MorangoImg = pygame.image.load('Imagens/Morango.png')

alface1Img = pygame.image.load('Imagens/alface.png')
alface2Img = pygame.image.load('Imagens/alface_2.png')
alface3Img = pygame.image.load('Imagens/alface_3.png')
alface4Img = pygame.image.load('Imagens/alface_4.png')
brocolisImg = pygame.image.load('Imagens/brocolis.png')
abacateImg = pygame.image.load('Imagens/abacate.png')
carocoImg = pygame.image.load('Imagens/caroco.png')
caroco2Img = pygame.image.load('Imagens/caroco2.png')
caroco3Img = pygame.image.load('Imagens/caroco3.png')
caroco4Img = pygame.image.load('Imagens/caroco4.png')
limaoImg = pygame.image.load('Imagens/limao.png')
acido1Img = pygame.image.load('Imagens/acido1.png')
acido2Img = pygame.image.load('Imagens/acido2.png')
vagem1Img = pygame.image.load('Imagens/vagem_1.png')
vagem2Img = pygame.image.load('Imagens/vagem_2.png')
vagem3Img = pygame.image.load('Imagens/vagem_3.png')
vagem4Img = pygame.image.load('Imagens/vagem_4.png')
ervilha1Img = pygame.image.load('Imagens/ervilha_1.png')
ervilha2Img = pygame.image.load('Imagens/ervilha_2.png')
pimentaoVerdeImg = pygame.image.load('Imagens/pimentaoVerde.png')
pimentaVerdeImg = pygame.image.load('Imagens/pimentaVerde.png')

blueBerryImg = pygame.image.load('Imagens/blueBerry.png')
pimentaPretaImg = pygame.image.load('Imagens/pimentaPreta.png')
pimentaoPretoImg = pygame.image.load('Imagens/pimentaoPreto.png')
beterrabaImg = pygame.image.load('Imagens/beterraba.png')
berinjelaImg = pygame.image.load('Imagens/berinjela.png')
grapesImg = pygame.image.load('Imagens/grapes.png')
psychicImg = pygame.image.load('Imagens/psychic.png')
psychicWImg = pygame.image.load('Imagens/psychicWither.png')

slotImg = pygame.image.load('Imagens/slot.png')
passivo1itemImg = pygame.image.load('Imagens/passivo1_item.png')
passivo2itemImg = pygame.image.load('Imagens/passivo2_item.png')
passivo3itemImg = pygame.image.load('Imagens/passivo3_item.png')
passivo4itemImg = pygame.image.load('Imagens/passivo4_item.png')
passivo5itemImg = pygame.image.load('Imagens/passivo5_item.png')
passivo6itemImg = pygame.image.load('Imagens/passivo6_item.png')
cerejaBombaImg = pygame.image.load('Imagens/cerejaBomba.png')
passivo11Img = pygame.image.load('Imagens/passivo1_1.png')
passivo12Img = pygame.image.load('Imagens/passivo1_2.png')
passivo13Img = pygame.image.load('Imagens/passivo1_3.png')
passivo21Img = pygame.image.load('Imagens/passivo2_1.png')
passivo22Img = pygame.image.load('Imagens/passivo2_2.png')
passivo23Img = pygame.image.load('Imagens/passivo2_3.png')
passivo31Img = pygame.image.load('Imagens/passivo3_1.png')
passivo32Img = pygame.image.load('Imagens/passivo3_2.png')
passivo33Img = pygame.image.load('Imagens/passivo3_3.png')
passivo41Img = pygame.image.load('Imagens/passivo4_1.png')
passivo42Img = pygame.image.load('Imagens/passivo4_2.png')
passivo43Img = pygame.image.load('Imagens/passivo4_3.png')
passivo51Img = pygame.image.load('Imagens/passivo5_1.png')
passivo52Img = pygame.image.load('Imagens/passivo5_2.png')
passivo53Img = pygame.image.load('Imagens/passivo5_3.png')
passivo61Img = pygame.image.load('Imagens/passivo6_1.png')
passivo62Img = pygame.image.load('Imagens/passivo6_2.png')
passivo63Img = pygame.image.load('Imagens/passivo6_3.png')

poderBloqueadoImg = pygame.image.load('Imagens/PoderBloqueado.png') # Poder que ainda não tem level pra usar
poder11Img = pygame.image.load('Imagens/poder1_1.png') # spores
poder21Img = pygame.image.load('Imagens/poder2_1.png') # blast
poder31Img = pygame.image.load('Imagens/poder3_1.png') # thorns
poder41Img = pygame.image.load('Imagens/poder4_1.png') # defense
poder51Img = pygame.image.load('Imagens/poder5_1.png') # minions
poder61Img = pygame.image.load('Imagens/poder6_1.png') # healing salve
poder71Img = pygame.image.load('Imagens/poder7_1.png') # bomb
poder81Img = pygame.image.load('Imagens/poder8_1.png') # vampire vines
poder91Img = pygame.image.load('Imagens/poder9_1.png') # Imolate

poder12Img = pygame.image.load('Imagens/poder1_2.png') # spores
poder22Img = pygame.image.load('Imagens/poder2_2.png') # blast
poder32Img = pygame.image.load('Imagens/poder3_2.png') # thorns
poder42Img = pygame.image.load('Imagens/poder4_2.png') # defense
poder52Img = pygame.image.load('Imagens/poder5_2.png') # minions
poder62Img = pygame.image.load('Imagens/poder6_2.png') # healing salve
poder72Img = pygame.image.load('Imagens/poder7_2.png') # bomb
poder82Img = pygame.image.load('Imagens/poder8_2.png') # vampire vines
poder92Img = pygame.image.load('Imagens/poder9_2.png') # Imolate

poder13Img = pygame.image.load('Imagens/poder1_3.png') # spores
poder23Img = pygame.image.load('Imagens/poder2_3.png') # blast
poder33Img = pygame.image.load('Imagens/poder3_3.png') # thorns
poder43Img = pygame.image.load('Imagens/poder4_3.png') # defense
poder53Img = pygame.image.load('Imagens/poder5_3.png') # minions
poder63Img = pygame.image.load('Imagens/poder6_3.png') # healing salve
poder73Img = pygame.image.load('Imagens/poder7_3.png') # bomb
poder83Img = pygame.image.load('Imagens/poder8_3.png') # vampire vines
poder93Img = pygame.image.load('Imagens/poder9_3.png') # Imolate
poder0Img = pygame.image.load('Imagens/poder0.png') # Deathly death spell

blocoTopoImg = pygame.image.load('Imagens/blocoTopo.png')
blocoLadoImg = pygame.image.load('Imagens/blocoLado.png')

emerson1Img = pygame.image.load('Imagens/sombra_1.png')
emerson2Img = pygame.image.load('Imagens/sombra_2.png')
emerson3Img = pygame.image.load('Imagens/sombra_3.png')
emerson4Img = pygame.image.load('Imagens/sombra_4.png')
emerson5Img = pygame.image.load('Imagens/sombra_5.png')
emerson6Img = pygame.image.load('Imagens/sombra_6.png')
emerson7Img = pygame.image.load('Imagens/sombra_7.png')
emerson8Img = pygame.image.load('Imagens/sombra_8.png')
emerson9Img = pygame.image.load('Imagens/sombra_9.png')

magia1Img = pygame.image.load('Imagens/bolaMagia.png')
magia2Img = pygame.image.load('Imagens/bolaMagia2.png')
magia3Img = pygame.image.load('Imagens/bolaMagia3.png')


acidoSOM = pygame.mixer.Sound('Sons/acido.wav')
acido2SOM = pygame.mixer.Sound('Sons/acido2.wav')
aguaSOM = pygame.mixer.Sound('Sons/agua.wav')
danoSOM = pygame.mixer.Sound('Sons/dano.wav')
explosaoSOM = pygame.mixer.Sound('Sons/explosao.wav')
morteInimigoSOM = pygame.mixer.Sound('Sons/morteInimigo.wav')
morteInimigo2SOM = pygame.mixer.Sound('Sons/morteInimigo2.wav')
morteInimigo3SOM = pygame.mixer.Sound('Sons/morteInimigo3.wav')
passivoSOM = pygame.mixer.Sound('Sons/passivo.wav')
bossDefeatSOM = pygame.mixer.Sound('Sons/bossdefeat.wav')
deathSOM = pygame.mixer.Sound('Sons/death.wav')

espinhosSOM = pygame.mixer.Sound('Sons/espinhos.wav')
vinesSOM = pygame.mixer.Sound('Sons/vines.wav')

hard = pygame.mixer.Sound('Sons/hard.wav')
extrahard = pygame.mixer.Sound('Sons/extrahard.ogg')
Nightmare = pygame.mixer.Sound('Sons/Nightmare.wav')
SALADAMUSICA = pygame.mixer.Sound('Sons/SALADA.wav')

def escrever(texto, tam, pos):
    largeText = pygame.font.Font('freesansbold.ttf', tam)
    TextSurf = largeText.render(texto, True, black)
    TextRect = TextSurf.get_rect()
    TextRect.center = ((pos[0], pos[1]))
    gameDisplay.blit(TextSurf, TextRect)
def escreverCanto(texto, tam, pos):
    largeText = pygame.font.Font('freesansbold.ttf', tam)
    TextSurf = largeText.render(texto, True, black)
    gameDisplay.blit(TextSurf, pos)

def dislaySel():
    if sel == 1:
        RectStart1 = pygame.image.load('imagens\PLAYsqr.png')
        RectStart2 = pygame.image.load('imagens\grayHELPsqr.png')
        RectStart3 = pygame.image.load('imagens\grayCharactersqr.png')
        RectStart4 = pygame.image.load('imagens\grayLEADERBOARDsqr.png')
        RectStart5 = pygame.image.load('imagens\grayDifficultysqr.png')
        RectStart6 = pygame.image.load('imagens\grayQUITsqr.png')
        gameDisplay.blit(RectStart1, (25, 50))
        gameDisplay.blit(RectStart2, (25, 125))
        gameDisplay.blit(RectStart3, (25, 200))
        gameDisplay.blit(RectStart4, (25, 275))
        gameDisplay.blit(RectStart5, (25, 350))
        gameDisplay.blit(RectStart6, (25, 425))
    if sel == 2:
        RectStart1 = pygame.image.load('imagens\grayPLAYsqr.png')
        RectStart2 = pygame.image.load('imagens\HELPsqr.png')
        RectStart3 = pygame.image.load('imagens\grayCharactersqr.png')
        RectStart4 = pygame.image.load('imagens\grayLEADERBOARDsqr.png')
        RectStart5 = pygame.image.load('imagens\grayDifficultysqr.png')
        RectStart6 = pygame.image.load('imagens\grayQUITsqr.png')
        gameDisplay.blit(RectStart1, (25, 50))
        gameDisplay.blit(RectStart2, (25, 125))
        gameDisplay.blit(RectStart3, (25, 200))
        gameDisplay.blit(RectStart4, (25, 275))
        gameDisplay.blit(RectStart5, (25, 350))
        gameDisplay.blit(RectStart6, (25, 425))
    if sel == 3:
        RectStart1 = pygame.image.load('imagens\grayPLAYsqr.png')
        RectStart2 = pygame.image.load('imagens\grayHELPsqr.png')
        RectStart3 = pygame.image.load('imagens\Charactersqr.png')
        RectStart4 = pygame.image.load('imagens\grayLEADERBOARDsqr.png')
        RectStart5 = pygame.image.load('imagens\grayDifficultysqr.png')
        RectStart6 = pygame.image.load('imagens\grayQUITsqr.png')
        gameDisplay.blit(RectStart1, (25, 50))
        gameDisplay.blit(RectStart2, (25, 125))
        gameDisplay.blit(RectStart3, (25, 200))
        gameDisplay.blit(RectStart4, (25, 275))
        gameDisplay.blit(RectStart5, (25, 350))
        gameDisplay.blit(RectStart6, (25, 425))
    if sel == 4:
        RectStart1 = pygame.image.load('imagens\grayPLAYsqr.png')
        RectStart2 = pygame.image.load('imagens\grayHELPsqr.png')
        RectStart3 = pygame.image.load('imagens\grayCharactersqr.png')
        RectStart4 = pygame.image.load('imagens\LEADERBOARDsqr.png')
        RectStart5 = pygame.image.load('imagens\grayDifficultysqr.png')
        RectStart6 = pygame.image.load('imagens\grayQUITsqr.png')
        gameDisplay.blit(RectStart1, (25, 50))
        gameDisplay.blit(RectStart2, (25, 125))
        gameDisplay.blit(RectStart3, (25, 200))
        gameDisplay.blit(RectStart4, (25, 275))
        gameDisplay.blit(RectStart5, (25, 350))
        gameDisplay.blit(RectStart6, (25, 425))
    if sel == 5:
        RectStart1 = pygame.image.load('imagens\grayPLAYsqr.png')
        RectStart2 = pygame.image.load('imagens\grayHELPsqr.png')
        RectStart3 = pygame.image.load('imagens\grayCharactersqr.png')
        RectStart4 = pygame.image.load('imagens\grayLEADERBOARDsqr.png')
        RectStart5 = pygame.image.load('imagens\Difficultysqr.png')
        RectStart6 = pygame.image.load('imagens\grayQUITsqr.png')
        gameDisplay.blit(RectStart1, (25, 50))
        gameDisplay.blit(RectStart2, (25, 125))
        gameDisplay.blit(RectStart3, (25, 200))
        gameDisplay.blit(RectStart4, (25, 275))
        gameDisplay.blit(RectStart5, (25, 350))
        gameDisplay.blit(RectStart6, (25, 425))
    if sel == 6:
        RectStart1 = pygame.image.load('imagens\grayPLAYsqr.png')
        RectStart2 = pygame.image.load('imagens\grayHELPsqr.png')
        RectStart3 = pygame.image.load('imagens\grayCharactersqr.png')
        RectStart4 = pygame.image.load('imagens\grayLEADERBOARDsqr.png')
        RectStart5 = pygame.image.load('imagens\grayDifficultysqr.png')
        RectStart6 = pygame.image.load('imagens\QUITsqr.png')
        gameDisplay.blit(RectStart1, (25, 50))
        gameDisplay.blit(RectStart2, (25, 125))
        gameDisplay.blit(RectStart3, (25, 200))
        gameDisplay.blit(RectStart4, (25, 275))
        gameDisplay.blit(RectStart5, (25, 350))
        gameDisplay.blit(RectStart6, (25, 425))

def difficulty(dificuldade):
    diff = True
    with open('Imagens/Statos.txt', 'r') as file:
        info = file.read()
        info = info.split('\n')
        Mlevel = 0
        for orq in info:
            orqs = [float(temp) for temp in orq.split('|')]
            level = orqs[5]
            if level > Mlevel:
                Mlevel = level
    Maxdificuldade = 1
    if Mlevel > 5:
        Maxdificuldade = 2
    if Mlevel > 8:
        Maxdificuldade = 3
    if Mlevel > 12:
        Maxdificuldade = 4
    if Mlevel > 15:
        Maxdificuldade = 5
    if Mlevel > 18:
        Maxdificuldade = 6
    if Mlevel > 21:
        Maxdificuldade = 7
    if Mlevel > 24:
        Maxdificuldade = 8
    if Mlevel > 27:
        Maxdificuldade = 9
    while diff:
        gameDisplay.fill((221, 155, 11))
        gameMenu = pygame.image.load('imagens\Garden.png')
        gameDisplay.blit(gameMenu, (0, 0))
        if dificuldade == 1:
            escrever("Difficulty: Hard", 50, [400, 300])
        elif dificuldade == 2:
            escrever("Difficulty: Extra Hard", 50, [400, 300])
        elif dificuldade == 3:
            escrever("Difficulty: Nightmare", 50, [400, 300])
        elif dificuldade == 4:
            escrever("Difficulty: SALAD", 50, [400, 300]) 
        elif dificuldade == 5:
            escrever("Game Mode: Beat Beet Beats", 50, [400, 300]) 
            escrever("Different gamemodes do not give xp", 15, [400, 450]) 
        elif dificuldade == 6:
            escrever("Game Mode: Boss Bass", 50, [400, 300]) 
            escrever("Different gamemodes do not give xp", 15, [400, 450]) 
        elif dificuldade == 7:
            escrever("Game Mode: Diet Salad", 50, [400, 300]) 
            escrever("Different gamemodes do not give xp", 15, [400, 450]) 
        elif dificuldade == 8:
            escrever("Game Mode: Tank Time", 50, [400, 300]) 
            escrever("Different gamemodes do not give xp", 15, [400, 450]) 
        elif dificuldade == 9:
            escrever("Game Mode: Water World", 50, [400, 300]) 
            escrever("Different gamemodes do not give xp", 15, [400, 450]) 
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()       
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if dificuldade == 1:
                        dificuldade = Maxdificuldade
                    else:
                        dificuldade -= 1
                if event.key == pygame.K_RIGHT:
                    if dificuldade == Maxdificuldade:
                        dificuldade = 1
                    else:    
                        dificuldade += 1
                if event.key == pygame.K_SPACE:
                    return dificuldade

def character(chacList, orquidea):
    chac = True
    with open('Imagens/Statos.txt', 'r') as file:
        info = file.read()
        info = info.split('\n')
        leveis = []
        for orq in info:
            orqs = [float(temp) for temp in orq.split('|')]
            leveis.append(orqs[5])
    while chac:
        gameDisplay.fill((221, 155, 11))
        gameMenu = pygame.image.load('imagens\Garden.png')
        gameDisplay.blit(gameMenu, (0, 0))
        if orquidea == 1:
            escrever(chacList[1], 50, [400, 200])
            chacImage = pygame.image.load('Imagens/cycnoches_1.png')
            gameDisplay.blit(chacImage, (400, 350))
            escrever('Level: %d' % int(leveis[0]), 15, (410, 400))
        elif orquidea == 2:
            escrever(chacList[1], 50, [400, 200])
            chacImage = pygame.image.load('Imagens/cymbidium_1.png')
            gameDisplay.blit(chacImage, (400, 350))
            escrever('Level: %d' % int(leveis[1]), 15, (410, 400))
        elif orquidea == 3:
            escrever(chacList[1], 50, [400, 200])
            chacImage = pygame.image.load('Imagens/coerulea_1.png')
            gameDisplay.blit(chacImage, (400, 350))            
            escrever('Level: %d' % int(leveis[2]), 15, (410, 400))
        elif orquidea == 4:
            escrever(chacList[1], 50, [400, 200]) 
            chacImage = pygame.image.load('Imagens/caladenia_1.png')
            gameDisplay.blit(chacImage, (400, 350))            
            escrever('Level: %d' % int(leveis[3]), 15, (410, 400))
        pygame.display.update()
        if orquidea == 1:
            chacList[1] = 'Cycnoches'
            chacList[2] = cycnoches1Img
            chacList[3] = cycnoches2Img
        elif orquidea == 2:
            chacList[1] = 'Cymbidium'
            chacList[2] = cymbidium1Img
            chacList[3] = cymbidium2Img
        elif orquidea == 3:
            chacList[1] = 'Coerulea'
            chacList[2] = coerulea1Img
            chacList[3] = coerulea2Img
        elif orquidea == 4:
            chacList[1] = 'Caladenia'
            chacList[2] = caladenia1Img
            chacList[3] = caladenia2Img
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()       
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if orquidea == 1:
                        orquidea = 4
                        chacList[0] = orquidea
                    else:
                        orquidea -= 1
                        chacList[0] = orquidea
                if event.key == pygame.K_RIGHT:
                    if orquidea == 4:
                        orquidea = 1
                        chacList[0] = orquidea
                    else:    
                        orquidea += 1
                        chacList[0] = orquidea 
                if event.key == pygame.K_SPACE:
                    return chacList, orquidea

def spore(s):
    gameDisplay.blit(sporeImg, (s[0], s[1]))
def thorn(sd):
    Ti = pygame.transform.rotate(thornImg, sd[1])
    gameDisplay.blit(Ti, (sd[0][0], sd[0][1]))
def semente(sd, f):
    if f >= 0 and f < 10:
        ti = semente1Img
    if f >= 10 and f < 20:
        ti = semente2Img
    if f >= 20 and f < 30:
        ti = semente3Img
    if f >= 30 and f < 40:
        ti = semente2Img
    Ti = pygame.transform.rotate(ti, math.degrees(sd[2]))
    gameDisplay.blit(Ti, (sd[0], sd[1]))
def magia(sd, f):
    if f >= 0 and f < 10:
        ti = magia1Img
    if f >= 10 and f < 20:
        ti = magia2Img
    if f >= 20 and f < 30:
        ti = magia3Img
    Ti = pygame.transform.rotate(ti, math.degrees(sd[2]))
    gameDisplay.blit(Ti, (sd[0], sd[1]))
def ervilha(s, f):
    if f >= 0 and f < 5:
        ti = ervilha1Img
    if f >= 5 and f < 10:
        ti = ervilha2Img
    gameDisplay.blit(ti, (s[0], s[1]))
def acido(sd, f):
    if f >= 0 and f < 5:
        ti = acido1Img
    if f >= 5 and f < 10:
        ti = acido2Img
    Ti = pygame.transform.rotate(ti, math.degrees(sd[2]))
    gameDisplay.blit(Ti, (sd[0], sd[1]))
def psychic(sd, t):
    if t == 0:
        ti = psychicImg
    elif t == 1:
        ti = psychicWImg
    Ti = pygame.transform.rotate(ti, math.degrees(sd[2]))
    gameDisplay.blit(Ti, (sd[0], sd[1]))
def bombaDisplay(sd, f):
    rot = f*8
    rot += sd[2]
    Ti = pygame.transform.rotate(cerejaBombaImg, rot)
    gameDisplay.blit(Ti, (sd[0], sd[1]))
def plantinha(s, t):
    if t == 1:
        gameDisplay.blit(plantinha1Img, (s[0], s[1]))
    elif t == 2:
        gameDisplay.blit(plantinha2Img, (s[0], s[1]))
    elif t == 3:
        gameDisplay.blit(plantinha3Img, (s[0], s[1]))
    elif t == 4:
        gameDisplay.blit(plantinha4Img, (s[0], s[1]))
def water(s):
    gameDisplay.blit(waterDropImg, (s[0], s[1]))
def montanha(s):
    gameDisplay.blit(montanhaImg, (s[0], s[1]))

def pimenta(s):
    gameDisplay.blit(pimentaImg, (s[0], s[1]))
def cereja(s):
    gameDisplay.blit(cerejaImg, (s[0], s[1]))
def melancia(s, e):
    if e == 1:
        gameDisplay.blit(melancia1Img, (s[0], s[1]))
    elif e == 2:
        gameDisplay.blit(melancia2Img, (s[0], s[1]))
    elif e == 3:
        gameDisplay.blit(melancia3Img, (s[0], s[1]))
def pimentaAzul(s):
    gameDisplay.blit(pimentaAzulImg, (s[0], s[1]))
def cerejaAzul(s):
    gameDisplay.blit(cerejaAzulImg, (s[0], s[1]))
def tomate(s):
    gameDisplay.blit(tomateImg, (s[0], s[1]))
def pimentao(s, e):
    if e == 1:
        gameDisplay.blit(pimentao1Img, (s[0], s[1]))
    elif e == 2:
        gameDisplay.blit(pimentao2Img, (s[0], s[1]))
def maca(s, e):
    if e == 1:
        gameDisplay.blit(maca1Img, (s[0], s[1]))
    elif e == 2:
        gameDisplay.blit(maca2Img, (s[0], s[1]))
def Morango(s):
    gameDisplay.blit(MorangoImg, (s[0], s[1]))

def alface(s, f):
    if f >= 0 and f < 5:
        ti = alface1Img
    if f >= 5 and f < 10:
        ti = alface2Img
    if f >= 10 and f < 15:
        ti = alface3Img
    if f >= 15 and f < 20:
        ti = alface4Img
    gameDisplay.blit(ti, (s[0], s[1]))

def vagem(sd, f):
    if f >= 0 and f < 10:
        ti = vagem1Img
    if f >= 10 and f < 20:
        ti = vagem2Img
    if f >= 20 and f < 30:
        ti = vagem3Img
    if f >= 30 and f < 40:
        ti = vagem4Img
    Ti = pygame.transform.rotate(ti, sd[2])
    gameDisplay.blit(Ti, (sd[0], sd[1]))

def Emerson(sd, f):
    f = f//2
    if f == 0:
        ti = emerson1Img
    elif f == 1:
        ti = emerson2Img
    elif f == 2:
        ti = emerson3Img
    elif f == 3:
        ti = emerson4Img
    elif f == 4:
        ti = emerson5Img
    elif f == 5:
        ti = emerson6Img
    elif f == 6:
        ti = emerson7Img
    elif f == 7:
        ti = emerson8Img
    elif f == 8:
        ti = emerson9Img
    if sd[3] > 75:
        Ti = pygame.transform.rotate(ti, sd[2]+180)
    else:
        Ti = pygame.transform.rotate(ti, sd[2])
    gameDisplay.blit(Ti, (sd[0], sd[1]))

def pimentaoVerde(s):
    gameDisplay.blit(pimentaoVerdeImg, (s[0], s[1]))
def pimentaVerde(s):
    gameDisplay.blit(pimentaVerdeImg, (s[0], s[1]))

def brocolis(s):
    gameDisplay.blit(brocolisImg, (s[0], s[1]))

def abacate(s):
    gameDisplay.blit(abacateImg, (s[0], s[1]))
def caroco(s, e):
    if e == 0:
        gameDisplay.blit(carocoImg, (s[0], s[1]))
    if e >= 750:
        gameDisplay.blit(caroco2Img, (s[0], s[1]))
    if e >= 754:
        gameDisplay.blit(caroco3Img, (s[0], s[1]))
    if e >= 758:
        gameDisplay.blit(caroco4Img, (s[0], s[1]))
def limao(s):
    gameDisplay.blit(limaoImg, (s[0], s[1]))


def blueBerry(s):
    gameDisplay.blit(blueBerryImg, (s[0], s[1]))
def pimentaPreta(s):
    gameDisplay.blit(pimentaPretaImg, (s[0], s[1]))
def pimentaoPreto(s):
    gameDisplay.blit(pimentaoPretoImg, (s[0], s[1]))
def beterraba(s):
    gameDisplay.blit(beterrabaImg, (s[0], s[1]))
def berinjela(s):
    gameDisplay.blit(berinjelaImg, (s[0], s[1]))
def grapes(s):
    gameDisplay.blit(grapesImg, (s[0], s[1]))


def danoInimigo(i, ini, dano):
    global inimigos
    global boss
    global o
    inimigos[i][4] -= dano
    o.rage += dano
    if boss > 0 and inimigos[i][0] in [500, 600, 700, 1000]:
        boss -= dano
    if inimigos[i][4] <= 0:
        mata(ini)

def aleatorio(t, s):
    d = [6, 8]
    if t == 0:
        C = random.randrange(0, 100)
        if C == 0:
            itens.append([0, s, d])
    if t == 8:
        C = random.randrange(0, 5)
        if C == 0:
            itens.append([0, s, d])
    if t == 13:
        C = random.randrange(0, 2)
        if C == 0:
            itens.append([0, s, d])
    if t == 15:
        C = random.randrange(0, 20)
        if C == 0:
            itens.append([0, s, d])
    if t == 25:
        itens.append([0, s, d])
    if t == 2.5:
        C = random.randrange(0, 40)
        if C == 0:
            itens.append([0, s, d])
    
    d = [14, 14]
    if t == 1:
        C = random.randrange(0, 10)
        if C == 0:
            itens.append([2, s, d])
    if t == 5:
        itens.append([2, s, d])
    
    d = [12, 12]
    if t == 2:
        C = random.randrange(0, 50)
        if C == 0:
            itens.append([1, s, d])
    
    d = [15, 10]
    if t == 2:
        C = random.randrange(0, 50)
        if C == 0:
            itens.append([3, s, d])

    d = [16, 16]
    if t == 4:
        C = random.randrange(0, 10)
        if C == 0:
            itens.append([4, s, d])
    
    if t in [500, 600, 700, 1000]:
        C = random.randrange(0, 2)
        if C == 0:
            itens.append([5, s, d])

    if t == 9:
        C = random.randrange(0, 4)
        if C == 0:
            itens.append([6, s, d])
    if t == 20:
        C = random.randrange(0, 12)
        if C == 0:
            itens.append([6, s, d])
    if t == 700 or t == 1000:
        C = random.randrange(0, 3)
        if C == 0:
            itens.append([6, s, d])

def mata(ini):
    global o
    global score
    global escudo
    global escudoFogo
    inimigos.remove(ini)
    if poderPassivo >=4 and poderPassivo <= 6:
        o.agua += (poderPassivo-3)*ini[0] +1
    if poderPassivo >= 13 and poderPassivo <= 15:
        escudo += 3*(poderPassivo - 12)
    if poderPassivo == 15:
        escudoFogo += 1.5
    score += ini[0]*2+1
    if ini[0] == 7:
        inimigos.append([11, [ini[1][0], ini[1][1]], [15, 15], 0, 15])

    Sm = random.randrange(0, 3)
    if ini[0] > 400:
        bossDefeatSOM.play()
    elif Sm == 0:
        morteInimigoSOM.play()
    elif Sm == 1:
        morteInimigo2SOM.play()
    elif Sm == 2:
        morteInimigo3SOM.play()
    aleatorio(ini[0], ini[1])

def planta(p):
    if p[2] == 1:
        gameDisplay.blit(auraCura, (p[0]-14, p[1]-14))
        gameDisplay.blit(planta1Img, (p[0], p[1]))
    elif p[2] == 2:
        gameDisplay.blit(auraCura2, (p[0]-18, p[1]-18))
        gameDisplay.blit(planta2Img, (p[0], p[1]))
    elif p[2] == 3:
        gameDisplay.blit(auraCura3, (p[0]-35, p[1]-35))
        gameDisplay.blit(planta3Img, (p[0], p[1]))
def vine(sd, f):
    if f >= 0 and f < 5:
        ti = vine1Img
    if f >= 5 and f < 10:
        ti = vine2Img
    if f >= 10 and f < 15:
        ti = vine3Img
    Ti = pygame.transform.rotate(ti, 90+math.degrees(sd[2]))
    gameDisplay.blit(Ti, (sd[0], sd[1]))

def colisaoBorda(Rect):
    if (Rect[0] > displayW-Rect[2]-12 or Rect[0] < 16 or Rect[1] > displayH-Rect[3]-12 or Rect[1] < 16) or (pygame.Rect(Rect[0], Rect[1], Rect[2], Rect[3]).colliderect(pygame.Rect(xmont+1, ymont+40, 96, 40))):
        return True
    else:
        return False

class Orquidea():
    def __init__(self, life, Mlife, stamina, Mstamina, agua, Magua, level, xp, correr):
        self.x = displayW*0.5
        self.y = displayH*0.9
        self.w = 25
        self.h = 20
        self.vx = 0
        self.vy = 0
        self.v = correr
        self.R = 0
        self.life = life + level/2
        self.Mlife = Mlife + level/2
        self.stamina = stamina + level
        self.Mstamina = Mstamina + level
        self.agua = agua + level*5
        self.Magua = Magua + level*5
        self.level = level
        self.xp = xp
        self.Vlife = 0
        self.Wlife = 0
        self.rage = 0
        self.Mrage = 300 + self.Mstamina*5
        self.danoTomado = 0
        self.direction = 0
    def Rotina(self, counter, cicloDia, xmont, ymont):
        if not colisaoBorda([self.x+self.vx*self.v, self.y, self.w, self.h]):
            self.x += self.vx*self.v
        if not colisaoBorda([self.x, self.y+self.vy*self.v, self.w, self.h]):
            self.y += self.vy*self.v
        if pygame.Rect(self.x, self.y, self.w, self.h).colliderect(pygame.Rect(xmont+1, ymont+40, 96, 40)):
            self.x -= self.vx*self.v
            self.y -= self.vy*self.v

        if self.life < self.Mlife:
            self.life += 0.0000015*cicloDia*self.Mlife*self.agua
        if self.stamina < self.Mstamina:
            self.stamina += 0.0002*cicloDia*self.agua

        if self.danoTomado == 1:
            self.danoTomado = 0
            gameDisplay.blit(pygame.transform.rotate(danoImg, self.R), (self.x, self.y))
        elif counter % 30 < 15:
            gameDisplay.blit(pygame.transform.rotate(orc1Img, self.R), (self.x, self.y))
        else:
            gameDisplay.blit(pygame.transform.rotate(orc2Img, self.R), (self.x, self.y))
    def dano(self, l):
        global escudo
        f = 1
        self.rage += l
        if poder4ativ == 1:
            f /= 0.6**poder4lvl
        if orquidea == 2:
            f /= 0.7
        if orquidea == 3:
            f *= 0.9
        if poderPassivo >= 7 and poderPassivo <= 9:
            f /= 1 - (poderPassivo-6)*0.2
        self.danoTomado = 1
        if escudo > 0:
            escudo -= l/f
            f /= 0.1
        if self.life < l/f:
            self.Vlife -= l/f
        else:
            self.life -= l/f
        danoSOM.play()


def gameLoop(dificuldade):
    global xmont
    global ymont
    xmont = random.randrange(100, 450)
    ymont = random.randrange(100, 450)
    global o
    orqs = []
    with open('Imagens/Statos.txt', 'r') as file:
        info = file.read()
        info = info.split('\n')
        global orquideas
        orquideas = []
        for orq in info:
            orqs = [float(temp) for temp in orq.split('|')]
            orquideas.append(orqs)
            if orqs[0] == orquidea:
                global iorq
                global level
                global xp
                iorq = orquideas.index(orqs)
                level = orqs[5]
                o = Orquidea(orqs[1], orqs[1], orqs[2], orqs[2], orqs[3], orqs[3], level, orqs[6], orqs[4])
    r_change = 0
    l_change = 0
    u_change = 0
    d_change = 0
    if dificuldade == 8:
        o.Mlife = 200
        o.life = 200
        o.Magua = 75
        o.agua = 75
        o.Mstamina = 0
    elif dificuldade == 9:
        o.Mlife = 5
        o.Mstamina = 5
        o.Magua = 1000
        o.agua = 1000
    TamanhoBarra = 1
    global escudo
    global escudoFogo
    escudo = 0
    escudoFogo = 0
    global orc1Img
    global orc2Img
    poder = 1
    poder1lvl = 1
    poder2lvl = 1
    poder3lvl = 1
    global poder4lvl
    poder4lvl = 1
    poder5lvl = 1
    poder6lvl = 1
    poder7lvl = 1
    poder8lvl = 1
    poder9lvl = 1
    if level >= 12:
        poder1lvl = 3
    elif level >= 7:
        poder1lvl = 2
    if level >= 13:
        poder2lvl = 3
    elif level >= 8:
        poder2lvl = 2
    dia = 0
    cicloDia = 1.00000
    global poder4ativ
    poder4ativ = 0
    poder9ativ = 0
    diaNoite = -1
    counter = 1
    global inimigos
    inimigos = []
    minions = []
    plantas = []
    spores = []
    thorns = []
    sementes = []
    thornsIni = []
    waterDrops = []
    global score
    score = 0
    global boss
    boss = 0
    Mboss = 0
    global poderPassivo
    poderPassivo = 0
    global itens
    itens = []
    bombas = 0
    bomba = []
    vines = []
    acidos = []
    ervilhas = []
    psychics = []
    magias = []

    if dificuldade == 1:
        hard.play(-1)
    elif dificuldade == 3:
        Nightmare.play(-1)
    elif dificuldade == 4:
        SALADAMUSICA.play(-1)
    else:
        extrahard.play(-1)

    while (o.life + o.Vlife) > 0:
        gameDisplay.blit(fundo, (0, 0))
        blast = 75
        for pos in range(displayW//16):
            gameDisplay.blit(blocoTopoImg, (pos*16, 0))
            gameDisplay.blit(blocoLadoImg, (16*pos, 584))
        for pos in range(displayH//16):
            gameDisplay.blit(blocoLadoImg, (0, 16*pos))
            gameDisplay.blit(blocoLadoImg, (784, 16*pos))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                SALADAMUSICA.stop()
                extrahard.stop()
                hard.stop()
                Nightmare.stop()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    l_change = 5
                    o.direction = 270
                elif event.key == pygame.K_RIGHT:
                    r_change = 5
                    o.direction = 90
                if event.key == pygame.K_UP:
                    u_change = 5
                    o.direction = 180
                elif event.key == pygame.K_DOWN:
                    d_change = 5
                    o.direction = 270

                if d_change > 0 and r_change > 0:
                    d_change = 12.5**(1/2)
                    r_change = 12.5**(1/2)
                    o.direction = 45
                if d_change > 0 and l_change > 0:
                    d_change = 12.5**(1/2)
                    l_change = 12.5**(1/2)
                    o.direction = 315
                if u_change > 0 and r_change > 0:
                    u_change = 12.5**(1/2)
                    r_change = 12.5**(1/2)
                    o.direction = 135
                if u_change > 0 and l_change > 0:
                    u_change = 12.5**(1/2)
                    l_change = 12.5**(1/2)
                    o.direction = 225
                if event.key == pygame.K_z:
                    o.v = 2
                if event.key == pygame.K_1:
                    poder = 1
                    if level >= 16:
                        poder1lvl = 3
                    elif level >= 7:
                        poder1lvl = 2
                    else:
                        poder1lvl = 1
                if event.key == pygame.K_2:
                    poder = 2
                    if level >= 17:
                        poder2lvl = 3
                    elif level >= 8:
                        poder2lvl = 2
                    else:
                        poder2lvl = 1
                if event.key == pygame.K_3:
                    poder = 3
                    if level >= 18:
                        poder3lvl = 3
                    elif level >= 9:
                        poder3lvl = 2
                    else:
                        poder3lvl = 1
                if event.key == pygame.K_4:
                    poder = 4
                    if level >= 19:
                        poder4lvl = 3
                    elif level >= 10:
                        poder4lvl = 2
                    else:
                        poder4lvl = 1
                if event.key == pygame.K_5:
                    poder = 5
                    if level >= 20:
                        poder5lvl = 3
                    elif level >= 11:
                        poder5lvl = 2
                    else:
                        poder5lvl = 1
                if event.key == pygame.K_6:
                    poder = 6
                    if level >= 21:
                        poder6lvl = 3
                    elif level >= 12:
                        poder6lvl = 2
                    else:
                        poder6lvl = 1
                if event.key == pygame.K_7:
                    poder = 7
                    if level >= 22:
                        poder7lvl = 3
                    elif level >= 13:
                        poder7lvl = 2
                    else:
                        poder7lvl = 1
                if event.key == pygame.K_8:
                    poder = 8
                    if level >= 23:
                        poder8lvl = 3
                    elif level >= 14:
                        poder8lvl = 2
                    else:
                        poder8lvl = 1
                if event.key == pygame.K_9:
                    poder = 9
                    if level >= 24:
                        poder9lvl = 3
                    elif level >= 15:
                        poder9lvl = 2
                    else:
                        poder9lvl = 1
                if event.key == pygame.K_0:
                    poder = 0
                if event.key == pygame.K_SPACE:
                    if poder == 1:
                        if poder1lvl == 1:
                            if [o.x+o.w/2, o.y+o.h/2] not in spores and o.stamina >= 1:
                                spores.append([o.x+o.w/2, o.y+o.h/2])
                                o.stamina -= 1
                        elif poder1lvl == 2:
                            if [(o.x+o.w/2)+3, (o.y+o.h/2)] not in spores and o.stamina >= 0.75:
                                spores.append([(o.x+o.w/2)+3, (o.y+o.h/2)])
                                o.stamina -= 0.75
                            if [(o.x+o.w/2)-3, (o.y+o.h/2)] not in spores and o.stamina >= 0.75:
                                spores.append([(o.x+o.w/2)-3, (o.y+o.h/2)])
                                o.stamina -= 0.75
                        elif poder1lvl == 3:
                            if [(o.x+o.w/2)+5, (o.y+o.h/2)+5] not in spores and o.stamina >= 0.5:
                                spores.append([(o.x+o.w/2)+5, (o.y+o.h/2)+5])
                                o.stamina -= 0.5
                            if [(o.x+o.w/2)+5, (o.y+o.h/2)-5] not in spores and o.stamina >= 0.5:
                                spores.append([(o.x+o.w/2)+5, (o.y+o.h/2)-5])
                                o.stamina -= 0.5
                            if [(o.x+o.w/2)-5, (o.y+o.h/2)+5] not in spores and o.stamina >= 0.5:
                                spores.append([(o.x+o.w/2)-5, (o.y+o.h/2)+5])
                                o.stamina -= 0.5
                            if [(o.x+o.w/2)-5, (o.y+o.h/2)-5] not in spores and o.stamina >= 0.5:
                                spores.append([(o.x+o.w/2)-5, (o.y+o.h/2)-5])
                                o.stamina -= 0.5
                    elif poder == 2:
                        if (o.stamina >= 5*poder2lvl):
                            blast = 255
                            for ini in inimigos.copy():
                                i = inimigos.index(ini)
                                if ((o.x+o.w/2 - inimigos[i][1][0])**2 + (o.y+o.h/2 - inimigos[i][1][1])**2)**(1/2) < (35 + (25*poder2lvl)) or ((o.x+o.w/2 - (inimigos[i][1][0] + inimigos[i][2][0]))**2 + (o.y+o.h/2 - (inimigos[i][1][1] + inimigos[i][2][1]))**2)**(1/2) < (35 + (25*poder2lvl)):
                                    danoInimigo(i, ini, 4*poder2lvl)
                            explosaoSOM.play()
                            o.stamina -= 6*poder2lvl
                    elif poder == 3:
                        if o.stamina >= 2 and poder3lvl == 1:
                            thorns.append([[o.x+o.w/2, o.y+o.h/2], o.direction, 0])
                            thorns.append([[o.x+o.w/2, o.y+o.h/2], o.direction+45, 0])
                            thorns.append([[o.x+o.w/2, o.y+o.h/2], o.direction-45, 0])
                            thorns.append([[o.x+o.w/2, o.y+o.h/2], o.direction+90, 0])
                            thorns.append([[o.x+o.w/2, o.y+o.h/2], o.direction-90, 0])
                            o.stamina -= 2
                            espinhosSOM.play()
                        elif o.stamina >= 3 and poder3lvl == 2:
                            o.stamina -= 3
                            for numero in range(8):
                                thorns.append([[o.x+o.w/2, o.y+o.h/2], 45*numero, -10])
                            espinhosSOM.play()
                        elif o.stamina >= 6 and poder3lvl == 3:
                            o.stamina -= 6
                            for numero in range(24):
                                thorns.append([[o.x+o.w/2, o.y+o.h/2], 15*numero, -15])
                            espinhosSOM.play()
                    elif poder == 4 and o.level >= 2:
                        poder4ativ = 1
                    elif poder == 5 and o.level >= 3:
                        if poder5lvl == 1 and o.stamina >= 10 and o.life > 3 and o.agua >= 25:
                            o.stamina -= 10
                            o.life -= 3
                            o.agua -= 25
                            minions.append([[o.x, o.y], 5, 0, 1])
                        elif poder5lvl == 2 and o.stamina >= 15 and o.life > 6 and o.agua >= 50:
                            o.stamina -= 15
                            o.life -= 6
                            o.agua -= 50
                            minions.append([[o.x, o.y], 10, 0, 2])
                        elif poder5lvl == 3 and o.stamina >= 20 and o.life > 9 and o.agua >= 100:
                            o.stamina -= 20
                            o.life -= 9
                            o.agua -= 100
                            minions.append([[o.x, o.y], 20, 0, 3])
                    elif poder == 6 and o.level >= 4:
                        if o.stamina >= 10 and o.agua >= 20 and poder6lvl == 1:
                            o.stamina -= 10
                            o.agua -= 20
                            plantas.append([o.x, o.y, 1])
                        elif o.stamina >= 15 and o.agua >= 40 and poder6lvl == 2:
                            o.stamina -= 15
                            o.agua -= 40
                            plantas.append([o.x, o.y, 2])
                        elif o.stamina >= 20 and o.agua >= 80 and poder6lvl == 3:
                            o.stamina -= 20
                            o.agua -= 80
                            plantas.append([o.x, o.y, 3])
                    elif poder == 7:
                        if poder7lvl == 1:
                            if bombas >= 1:
                                bomba.append([[o.x, o.y], o.direction, 0])
                                bombas -= 1
                        elif poder7lvl == 2:
                            if bombas >= 3:
                                bomba.append([[o.x, o.y], o.direction, 0])
                                bomba.append([[o.x, o.y], o.direction+45, 0])
                                bomba.append([[o.x, o.y], o.direction-45, 0])
                                bombas -= 3
                        elif poder7lvl == 3:
                            if bombas >= 1:
                                bomba.append([[o.x, o.y], o.direction+15, -20])
                                bomba.append([[o.x, o.y], o.direction-15, -20])
                                bombas -= 1
                    elif poder == 8 and o.level >= 5:
                        if poder8lvl == 1:
                            if o.stamina >= 12 and o.life > 2:
                                o.stamina -=  12
                                o.life -= 2
                                vines.append([[o.x, o.y], o.direction, 0])
                                vinesSOM.play()
                        if poder8lvl == 2:
                            if o.stamina >= 20 and o.life > 2:
                                o.stamina -=  20
                                o.life -= 2
                                vines.append([[o.x-10, o.y-10], o.direction, -5])
                                vines.append([[o.x+10, o.y+10], o.direction+180, -5])
                                vinesSOM.play()
                        if poder8lvl == 3:
                            for numero in range(8):
                                if o.stamina >= 7 and o.life > 1:
                                    o.stamina -= 7
                                    o.life -= 1
                                    vines.append([[o.x, o.y], o.direction, 0])
                                    vinesSOM.play()
                    elif poder == 9 and o.level >= 6:
                        poder9ativ = 1
                    elif poder == 0 and o.level >= 25:
                        if o.stamina > 40 and o.life > 15 and o.agua > 100:
                            o.stamina -= 40
                            o.life -= 15
                            o.agua -= 100
                            o.Mlife -= 5
                            o.Wlife += 5
                            gameDisplay.fill((255,255,255))
                            for ini in inimigos.copy():
                                i = inimigos.index(ini)
                                danoInimigo(i, ini, 150)
                    if o.rage >= o.Mrage:
                        if poder == 1:
                            for numero in range(120):
                                Pxtemp = random.randrange(50, displayW - 50)
                                Pytemp = random.randrange(50, displayH - 50)
                                spores.append([Pxtemp, Pytemp])
                        elif poder == 2:
                            blast = 255
                            for ini in inimigos.copy():
                                i = inimigos.index(ini)
                                if ((o.x+o.w/2 - inimigos[i][1][0])**2 + (o.y+o.h/2 - inimigos[i][1][1])**2)**(1/2) < (35 + (25*poder2lvl)) or ((o.x+o.w/2 - (inimigos[i][1][0] + inimigos[i][2][0]))**2 + (o.y+o.h/2 - (inimigos[i][1][1] + inimigos[i][2][1]))**2)**(1/2) < (35 + (25*poder2lvl)):
                                    danoInimigo(i, ini, 35)
                            explosaoSOM.play()
                        elif poder == 3:
                            for numero in range(360):
                                thorns.append([[o.x+o.w/2, o.y+o.h/2], numero, -40])
                        elif poder == 4 and level >= 2:
                            escudo += 200
                        elif poder == 5 and level >= 3:
                            minions.append([[o.x, o.y], 50, 0, 4, 0])
                        elif poder == 6 and level >= 4:
                            for numero in range(15):
                                Pxtemp = random.randrange(50, displayW - 50)
                                Pytemp = random.randrange(50, displayH - 50)
                                plantas.append([Pxtemp, Pytemp, 1])
                            Pxtemp = random.randrange(50, displayW - 50)
                            Pytemp = random.randrange(50, displayH - 50)
                            plantas.append([Pxtemp, Pytemp, 2])
                            o.life += 200
                            o.Mlife += 1
                        elif poder == 7:
                            for numero in range(24):
                                bomba.append([[o.x, o.y], numero*15, -20])
                        elif poder == 8 and level >= 5:
                            vines.append([[o.x, o.y], o.R, -40])
                            vines.append([[o.x, o.y], o.R, -40])
                            vines.append([[o.x, o.y], o.R, -40])
                        elif poder == 9 and level >= 6:
                            escudoFogo += 150
                        else:
                            o.Mlife += 5
                            o.Mstamina += 10
                            o.Magua += 15
                        gameDisplay.fill(red)
                        o.rage = 0
                        o.Mrage += 25
                        o.Mstamina += 4

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    l_change = 0
                elif event.key == pygame.K_RIGHT:
                    r_change = 0
                if event.key == pygame.K_UP:
                    u_change = 0
                elif event.key == pygame.K_DOWN:
                    d_change = 0
                if d_change == 0 and r_change != 0:
                    d_change = 0
                    r_change = 5
                if d_change == 0 and l_change != 0:
                    d_change = 0
                    l_change = 5
                if u_change == 0 and r_change != 0:
                    u_change = 0
                    r_change = 5
                if u_change == 0 and l_change != 0:
                    u_change = 0
                    l_change = 5
                if event.key == pygame.K_z:
                    o.v = 1
                if event.key == pygame.K_SPACE:
                    poder4ativ = 0
                    poder9ativ = 0
        o.vx = r_change - l_change
        o.vy = d_change - u_change

        for s in spores:
            spore(s)
        for th in thorns:
            i = thorns.index(th)
            thorns[i][2] += 1
            lim = 25
            if poderPassivo == 4:
                lim = 30
            if poderPassivo == 5:
                lim = 40
            if poderPassivo == 6:
                lim = 50
            if thorns[i][2] >= lim:
                thorns.remove(th)
                continue
            thorns[i][0][0] += 10*math.sin(math.radians(thorns[i][1]))
            thorns[i][0][1] += 10*math.cos(math.radians(thorns[i][1]))
            thorn(thorns[i])
        for th in thornsIni:
            i = thornsIni.index(th)
            thornsIni[i][2] += 1
            if thornsIni[i][2] == 25:
                thornsIni.remove(th)
                continue
            thornsIni[i][0][0] += 10*math.sin(math.radians(thornsIni[i][1]))
            thornsIni[i][0][1] += 10*math.cos(math.radians(thornsIni[i][1]))
            thorn(thornsIni[i])
            if ((o.x>=th[0][0]+4) or (o.x+o.w<=th[0][0]) or (o.y+o.h<=th[0][1]) or (o.y>=th[0][1]+5)):
                pass
            else:
                thornsIni.remove(th)
                o.dano(0.8)
        for seed in sementes:
            i = sementes.index(seed)
            sementes[i][1] += 1
            if sementes[i][1] == 140:
                sementes.remove(seed)
                continue
            dir = math.atan2((o.x - sementes[i][0][0]), (o.y - sementes[i][0][1]))
            sementes[i][0][0] += 2*math.sin(dir)
            sementes[i][0][1] += 2*math.cos(dir)
            semente([sementes[i][0][0], sementes[i][0][1], dir], counter % 40)
            if ((o.x>=sementes[i][0][0]+14) or (o.x+o.w<=sementes[i][0][0]) or (o.y+o.h<=sementes[i][0][1]) or (o.y>=sementes[i][0][1]+14)):
                pass
            else:
                sementes.remove(seed)
                o.dano(1)
        for psc in psychics:
            i = psychics.index(psc)
            dir = math.atan2((o.x - psychics[i][1]), (o.y - psychics[i][2]))
            psychics[i][1] += 4*math.sin(dir)
            psychics[i][2] += 4*math.cos(dir)
            psychic([psychics[i][1], psychics[i][2], dir], psychics[i][0])
            if ((o.x>=psychics[i][1]+8) or (o.x+o.w<=psychics[i][1]) or (o.y+o.h<=psychics[i][2]) or (o.y>=psychics[i][2]+8)):
                pass
            else:
                psychics.remove(psc)
                o.dano(0.25)
                if psc[0] == 1:
                    o.Mlife -= 0.1
                    o.Wlife += 0.1
        for pea in ervilhas:
            i = ervilhas.index(pea)
            ervilhas[i][1] += 1
            if ervilhas[i][1] == 200:
                ervilhas.remove(pea)
                continue
            dir = math.atan2((o.x - ervilhas[i][0][0]), (o.y - ervilhas[i][0][1]))
            ervilhas[i][0][0] += 6*math.sin(dir)
            ervilhas[i][0][1] += 6*math.cos(dir)
            ervilha([ervilhas[i][0][0], ervilhas[i][0][1]], counter % 10)
            if ((o.x>=ervilhas[i][0][0]+12) or (o.x+o.w<=ervilhas[i][0][0]) or (o.y+o.h<=ervilhas[i][0][1]) or (o.y>=ervilhas[i][0][1]+12)):
                pass
            else:
                ervilhas.remove(pea)
                o.dano(2)
        for mg in magias:
            i = magias.index(mg)
            magias[i][2] += 1
            if magias[i][2] == 100:
                magias.remove(mg)
                continue
            dir = math.atan2((o.x - magias[i][0]), (o.y - magias[i][1]))
            magias[i][0] += 5*math.sin(dir)
            magias[i][1] += 5*math.cos(dir)
            magia([magias[i][0], magias[i][1], dir], counter % 30)
            if ((o.x>=magias[i][0]+14) or (o.x+o.w<=magias[i][0]) or (o.y+o.h<=magias[i][1]) or (o.y>=magias[i][1]+14)):
                pass
            else:
                magias.remove(mg)
                o.dano(2)
                o.Wlife += 4
                o.Mlife -= 4
        for ac in acidos:
            i = acidos.index(ac)
            acidos[i][3] += 1
            if acidos[i][3] >= 150:
                acidos.remove(ac)
                continue
            acidos[i][0] += 6*math.sin(acidos[i][2])
            acidos[i][1] += 6*math.cos(acidos[i][2])
            acido([acidos[i][0], acidos[i][1], acidos[i][2]], counter % 10)
            if ((o.x>=acidos[i][0]+3) or (o.x+o.w<=acidos[i][0]) or (o.y+o.h<=acidos[i][1]) or (o.y>=acidos[i][1]+9)):
                pass
            else:
                acidos.remove(ac)
                o.dano(1)
                if o.life > 2:
                    o.life -= 2
                    o.Vlife += 2
        for B in bomba:
            i = bomba.index(B)
            bomba[i][2] += 1
            para = False
            for ini in inimigos:
                if ((ini[1][0]>=bomba[i][0][0]+14) or (ini[1][0]+ini[2][0]<=bomba[i][0][0]) or (ini[1][1]+ini[2][1]<=bomba[i][0][1]) or (ini[1][1]>=bomba[i][0][1]+14)):
                    pass
                else:
                    pygame.draw.circle(gameDisplay, (255,255,255), (B[0][0]+7, B[0][1]+7), 45+(30*poder7lvl))
                    for ini in inimigos.copy():
                        if ((bomba[i][0][0]+7 - ini[1][0])**2 + (bomba[i][0][1]+7 - ini[1][1])**2)**(1/2) < 45+(30*poder7lvl) or ((bomba[i][0][0]+7 - (ini[1][0] + ini[2][0]))**2 + (bomba[i][0][1]+7 - (ini[1][1] + ini[2][1]))**2)**(1/2) < 45+(30*poder7lvl):
                            inid = inimigos.index(ini)
                            danoInimigo(inid, ini, 3+(poder7lvl*2))
                    explosaoSOM.play()
                    bomba.remove(B)
                    para = True
                    break
            if para:
                break
            if bomba[i][2] == 50:
                pygame.draw.circle(gameDisplay, (255,255,255), (B[0][0]+7, B[0][1]+7), 45+(30*poder7lvl))
                for ini in inimigos.copy():
                    if ((bomba[i][0][0]+7 - ini[1][0])**2 + (bomba[i][0][1]+7 - ini[1][1])**2)**(1/2) < 45+(30*poder7lvl) or ((bomba[i][0][0]+7 - (ini[1][0] + ini[2][0]))**2 + (bomba[i][0][1]+7 - (ini[1][1] + ini[2][1]))**2)**(1/2) < 45+(30*poder7lvl):
                        inid = inimigos.index(ini)
                        danoInimigo(inid, ini, 3+(poder7lvl*2))
                explosaoSOM.play()
                bomba.remove(B)
                continue
            bomba[i][0][0] += 7*math.sin(math.radians(bomba[i][1]))
            bomba[i][0][1] += 7*math.cos(math.radians(bomba[i][1]))
            if colisaoBorda([bomba[i][0][0], bomba[i][0][1], 10, 10]):
                bomba[i][1] += 180
            bombaDisplay([bomba[i][0][0], bomba[i][0][1], bomba[i][1]], counter % 45)
        for p in plantas:
            if p[2] == 1:
                if ((p[0]+8 - o.x)**2 + (p[1]+8 - o.y)**2)**(1/2) < 45 or ((p[0]+8 - (o.x+o.w))**2 + (p[1]+8 - (o.y+o.h))**2)**(1/2) < 45:
                    if o.agua >= 0.02 and o.life < o.Mlife:
                        o.life += 0.008
                        o.agua -= 0.02
                    for pl in minions:
                        pl[1] += 0.002
                        o.agua -= 0.02
                planta(p)
            elif p[2] == 2:
                if ((p[0]+8 - o.x)**2 + (p[1]+8 - o.y)**2)**(1/2) < 60 or ((p[0]+8 - (o.x+o.w))**2 + (p[1]+8 - (o.y+o.h))**2)**(1/2) < 60:
                    if o.agua >= 0.04 and o.life < o.Mlife:
                        o.life += 0.02
                        o.agua -= 0.04
                    for pl in minions:
                        pl[1] += 0.02
                        o.agua -= 0.05
                    if o.Wlife > 0:
                        o.Wlife -= 0.01
                        o.Mlife += 0.01
                        o.agua -= 0.1
                planta(p)
            elif p[2] == 3:
                if ((p[0]+8 - o.x)**2 + (p[1]+8 - o.y)**2)**(1/2) < 100 or ((p[0]+8 - (o.x+o.w))**2 + (p[1]+8 - (o.y+o.h))**2)**(1/2) < 100:
                    if o.agua >= 0.08 and o.life < o.Mlife:
                        o.life += 0.06
                        o.agua -= 0.1
                    for pl in minions:
                        pl[1] += 0.1
                        o.agua -= 0.1
                    if o.Wlife > 0:
                        o.Wlife -= 0.1
                        o.Mlife += 0.1
                        o.agua -= 0.3
                planta(p)
        for v in vines:
            i = vines.index(v)
            if v[2] < 6:
                perto = []
                for inimigo in inimigos:
                    Dx = vines[i][0][0] - inimigo[1][0]
                    Dy = vines[i][0][1] - inimigo[1][1]
                    Dt = (Dx**2 + Dy**2)**(1/2)
                    im = inimigos.index(inimigo)
                    perto.append([Dt, im])
                perto.sort()
                try:
                    im = perto[0][1]
                    vines[i][1] = math.atan2((inimigos[im][1][0] - v[0][0]), (inimigos[im][1][1] - v[0][1]))
                except:
                    vines[i][2] += 1
                    continue
            else:
                vines[i][1] = math.atan2((o.x - v[0][0]), (o.y - v[0][1]))
                if ((o.x>=vines[i][0][0]+20) or (o.x+o.w<=vines[i][0][0]) or (o.y+o.h<=vines[i][0][1]) or (o.y>=vines[i][0][1]+10)):
                    pass
                else:
                    vines.remove(v)
                    o.life += v[2] -2
                    continue
            vines[i][0][0] += 10*math.sin(vines[i][1])
            vines[i][0][1] += 10*math.cos(vines[i][1])
            vine([vines[i][0][0], vines[i][0][1], vines[i][1]], counter % 15)
            
        PEX = random.randrange(40, displayW-40)
        PEY = random.randrange(40, displayH-40)
        
        if dificuldade == 1: # Hard
            if counter % (70+dia*2) == 0:
                inimigos.append([0, [PEX, PEY], [12, 18], 0, 1+dia//5]) # pimenta
            if counter % (175-dia*2) == 0:
                inimigos.append([1, [PEX, PEY], [24, 18], 0, 1+dia//3]) # cereja
            if counter % 354 == 0:
                inimigos.append([2, [PEX, PEY], [35, 18], 1, 1+dia//2]) # melancia
            if counter % 2203 == 0:
                inimigos.append([5, [PEX, PEY], [24, 18], 0, 3+dia]) # cereja azul
            if counter % 5200 == 0:
                inimigos.append([8, [PEX, PEY], [14, 16], 1, 12+dia*2]) # pimentão
            if counter % 4100 == 0:
                inimigos.append([9, [PEX, PEY], [24, 24], 1, 15+dia*3, [7, 7]]) # Maçã
            if counter % 6400-dia*100 == 0:
                inimigos.append([10, [PEX, PEY], [16, 16], 0, 9+dia*5]) # tomate
            if counter % (10000-dia*100) == 0:
                inimigos.append([20, [PEX, PEY], [20, 20], 0, 15+dia]) # beterraba
            if counter % 25000 == 0:
                if boss <= 0:
                    boss = 0
                    Mboss = 0
                boss += 100+dia*15
                Mboss += 100+dia*15
                inimigos.append([500, [PEX, PEY], [22, 23], 0, 100+dia*15]) # Morango.
        elif dificuldade == 2: # Extra Hard
            if counter % 98 == 0:
                inimigos.append([12, [PEX, PEY], [15, 15], 0, 3+dia]) # limao
            if counter % 454 == 0:
                inimigos.append([4, [PEX, PEY], [50, 50], 0, 15+dia]) # alface
            if counter % 430 == 0:
                inimigos.append([6, [PEX, PEY], [16, 19], 0, 3+dia]) # brocolis
            if counter % 1201 == 0:
                inimigos.append([13, [PEX, PEY], [14, 16], 0, 3+dia]) # pimentao verde
            if counter % 1245 == 0:
                inimigos.append([7, [PEX, PEY], [25, 25], 0, 5+dia]) # abacate
            if counter % 10000 == 0:
                if boss <= 0:
                    boss = 0
                    Mboss = 0
                boss += 150+dia*35
                Mboss += 150+dia*35
                inimigos.append([600, [PEX, PEY], [30, 50], 0, 150+dia*35]) # Vagem.
        elif dificuldade == 3: # Nightmare
            if counter % 303 == 0:
                inimigos.append([14, [PEX, PEY], [12, 12], 0, 5+dia]) # BlueBerry
            if counter % 434 == 0:
                inimigos.append([15, [PEX, PEY], [12, 18], 0, 10+dia]) # pimenta Preta
            if counter % (249-dia*3) == 0:
                inimigos.append([20, [PEX, PEY], [20, 20], 0, 20+dia]) # beterraba
            if counter % 2840 == 0:
                inimigos.append([25, [PEX, PEY], [14, 16], 0, 25+dia]) # pimentao preto
            if counter % (7500-dia*25) == 0:
                if boss <= 0:
                    boss = 0
                    Mboss = 0
                boss += 80+dia*30
                Mboss += 80+dia*30
                inimigos.append([700, [PEX, PEY], [50, 50], 0, 80+dia*30]) # berinjela
            if counter % 20000 == 0:
                if boss <= 0:
                    boss = 0
                    Mboss = 0
                boss += 200+dia*60
                Mboss += 200+dia*60
                inimigos.append([1000, [PEX, PEY], [43, 44], 0, 200+dia*60]) # grapes
        elif dificuldade == 4 or dificuldade == 7 or dificuldade == 8 or dificuldade == 9: # SALADA
            if dificuldade == 4:
                stats = 1
            else:
                stats = 3
            if counter % (60*stats) == 0:
                inimigos.append([0, [PEX, PEY], [12, 18], 0, 1+dia//2]) # pimenta
            if counter % (101*stats) == 0:
                inimigos.append([1, [PEX, PEY], [24, 18], 0, 1+dia]) # cereja
            if counter % (203*stats) == 0:
                inimigos.append([12, [PEX, PEY], [15, 15], 0, 3+dia]) # limao
            if counter % (507*stats) == 0:
                inimigos.append([2, [PEX, PEY], [35, 18], 1, 2+dia*2]) # melancia
            if counter % (550*stats) == 0:
                inimigos.append([4, [PEX, PEY], [50, 50], 0, 14+dia*3]) # alface
            if counter % (1200*stats) == 0:
                inimigos.append([7, [PEX, PEY], [25, 25], 0, 5]) # abacate
            if counter % (1005*stats) == 0:
                inimigos.append([13, [PEX, PEY], [14, 16], 0, 3+dia]) # pimentao verde
            if counter % (1580*stats) == 0:
                inimigos.append([5, [PEX, PEY], [24, 18], 0, 3+dia]) # cereja azul
            if counter % (610*stats) == 0:
                inimigos.append([6, [PEX, PEY], [16, 19], 0, 3+dia]) # brocolis
            if counter % (4100*stats) == 0:
                inimigos.append([8, [PEX, PEY], [14, 16], 1, 12+dia*2]) # pimentão
            if counter % (6544*stats) == 0:
                inimigos.append([9, [PEX, PEY], [24, 24], 1, 15+dia*5, [7, 7]]) # Maçã
            if counter % (4900*stats) == 0:
                inimigos.append([10, [PEX, PEY], [16, 16], 0, 11+dia*4]) # tomate
            if counter % (303*stats) == 0:
                inimigos.append([14, [PEX, PEY], [12, 12], 0, 5+dia]) # BlueBerry
            if counter % (434*stats) == 0:
                inimigos.append([15, [PEX, PEY], [12, 18], 0, 10+dia*2]) # pimenta Preta
            if counter % (629*stats) == 0:
                inimigos.append([20, [PEX, PEY], [20, 20], 0, 20+dia*2]) # beterraba
            if counter % (3440*stats) == 0:
                inimigos.append([25, [PEX, PEY], [14, 16], 0, 25+dia*3]) # pimentao preto
            if (counter + (10000*stats)) % (20000*stats) == 0:
                if boss <= 0:
                    boss = 0
                    Mboss = 0
                boss += 80+dia*30
                Mboss += 80+dia*30
                inimigos.append([700, [PEX, PEY], [50, 50], 0, 80+dia*30]) # berinjela
            if counter % (20000*stats) == 0:
                if boss <= 0:
                    boss = 0
                    Mboss = 0
                boss += 200+dia*60
                Mboss += 200+dia*60
                inimigos.append([1000, [PEX, PEY], [43, 44], 0, 200+dia*60]) # grapes
            if (counter + (7500*stats)) % (15000*stats) == 0:
                if boss <= 0:
                    boss = 0
                    Mboss = 0
                boss += 120+dia*50
                Mboss += 120+dia*50
                inimigos.append([500, [PEX, PEY], [22, 23], 0, 120+dia*50]) # Morango.
            if counter % (15000*stats) == 0:
                if boss <= 0:
                    boss = 0
                    Mboss = 0
                boss += 80+dia*45
                Mboss += 80+dia*45
                inimigos.append([600, [PEX, PEY], [30, 50], 0, 80+dia*45]) # Vagem.
            if counter % (100000*stats) == 0:
                if boss <= 0:
                    boss = 0
                    Mboss = 0
                boss += dia*1000
                Mboss += dia*1000
                inimigos.append([5000, [PEX, PEY], [32, 32], 0, dia*1000]) # Emerson.
        elif dificuldade == 5:
            if counter % 200 == 0:
                inimigos.append([20, [PEX, PEY], [20, 20], 0, 15+dia*2]) # beterraba
            if counter % 6000 == 0:
                if boss <= 0:
                    boss = 0
                    Mboss = 0
                boss += dia*100
                Mboss += dia*100
                inimigos.append([700, [PEX, PEY], [50, 50], 0, dia*100]) # Berinjela.
            if counter % (20000) == 0:
                if boss <= 0:
                    boss = 0
                    Mboss = 0
                boss += 200+dia*160
                Mboss += 200+dia*160
                inimigos.append([1000, [PEX, PEY], [43, 44], 0, 200+dia*160]) # grapes
        elif dificuldade == 6:
            if counter % 943 == 0:
                if boss <= 0:
                    boss = 0
                    Mboss = 0
                boss += 25+dia*25
                Mboss += 25+dia*25
                inimigos.append([500, [PEX, PEY], [22, 23], 0, 25+dia*25]) # Morango.
            if counter % 3321 == 0:
                if boss <= 0:
                    boss = 0
                    Mboss = 0
                boss += 50+dia*50
                Mboss += 50+dia*50
                inimigos.append([700, [PEX, PEY], [50, 50], 0, 50+dia*50]) # berinjela
            if counter % 6055 == 0:
                if boss <= 0:
                    boss = 0
                    Mboss = 0
                boss += 150+dia*75
                Mboss += 150+dia*75
                inimigos.append([600, [PEX, PEY], [30, 50], 0, 150+dia*75]) # Vagem.
            if counter % 20007 == 0:
                if boss <= 0:
                    boss = 0
                    Mboss = 0
                boss += 200+dia*100
                Mboss += 200+dia*100
                inimigos.append([1000, [PEX, PEY], [43, 44], 0, 200+dia*100]) # grapes

        if counter % (30) == 0 and cicloDia < 0.3 and dificuldade != 9:
            waterDrops.append([PEX, PEY])
        for W in waterDrops:
            water(W)
            if ((o.x>=W[0]+4) or (o.x+o.w<=W[0]) or (o.y+o.h<=W[1]) or (o.y>=W[1]+4)):
                pass
            else:
                waterDrops.remove(W)
                o.agua += 5
                aguaSOM.play()
                continue
        for ini in inimigos:
            dx = 0
            dy = 0
            i = inimigos.index(ini)
            if ini[0] == 0:
                inimigos[i][3] += 1
                if inimigos[i][3] > 10:
                    inimigos[i][3] = 0
                    dx += random.randrange(-5, 6)
                    dy += random.randrange(-5, 6)
                PA = random.randrange(0, 20000)
                if PA == 0:
                    inimigos.append([3, [inimigos[i][1][0], inimigos[i][1][1]], [12, 18], 0, inimigos[i][4]+1])
                    inimigos.remove(ini)
                    continue
                pimenta(ini[1])
            elif ini[0] == 1:
                if inimigos[i][1][0] > o.x:
                    dx -= 4
                elif inimigos[i][1][0] < o.x:
                    dx += 4
                if inimigos[i][1][1] > o.y:
                    dy -= 4
                elif inimigos[i][1][1] < o.y:
                    dy += 4
                cereja(inimigos[i][1])
            elif ini[0] == 2:
                if counter % 800 <= 200:
                    dx += 2
                elif counter % 800 <= 400 and counter % 800 > 200:
                    dy += 2
                elif counter % 800 <= 600 and counter % 800 > 400:
                    dx -= 2
                elif counter % 800 <= 800 and counter % 800 > 600:
                    dy -= 2
                melancia(inimigos[i][1], inimigos[i][3])
                if counter % 10 == 0:
                    inimigos[i][3] += 1
                    if inimigos[i][3] > 3:
                        inimigos[i][3] = 1
            elif ini[0] == 4:
                if inimigos[i][3] == 1:
                    dx += 3
                    dy += 3
                elif inimigos[i][3] == 2:
                    dx += 3
                    dy -= 3
                elif inimigos[i][3] == 3:
                    dx -= 3
                    dy += 3
                elif inimigos[i][3] == 4:
                    dx -= 3
                    dy -= 3
                elif inimigos[i][3] == 5:
                    pass
                if colisaoBorda([inimigos[i][1][0], inimigos[i][1][1], 50, 50]):
                    inimigos[i][3] += random.randrange(1,5)
                if counter % 50 == 0:
                    inimigos[i][3] = random.randrange(1,6)
                alface(inimigos[i][1], counter % 20)
            elif ini[0] == 2.5:
                inimigos[i][3] += 1
                if inimigos[i][3] > 25:
                    inimigos[i][3] = 0
                    dx += random.randrange(-15, 16)
                    dy += random.randrange(-15, 16)
                PA = random.randrange(0, 10000)
                if PA == 0:
                    inimigos.append([3, [inimigos[i][1][0], inimigos[i][1][1]], [12, 18], 0, 2+dia])
                    inimigos.remove(ini)
                    continue
                pimentaVerde(ini[1])
            elif ini[0] == 3:
                if inimigos[i][1][0] > o.x:
                    dx -= 0.25*inimigos[i][4]
                elif inimigos[i][1][0] < o.x:
                    dx += 0.25*inimigos[i][4]
                if inimigos[i][1][1] > o.y:
                    dy -= 0.25*inimigos[i][4]
                elif inimigos[i][1][1] < o.y:
                    dy += 0.25*inimigos[i][4]
                pimentaAzul(inimigos[i][1])
            elif ini[0] == 5:
                if inimigos[i][1][0] > o.x:
                    dx -= 6
                elif inimigos[i][1][0] < o.x:
                    dx += 6
                if inimigos[i][1][1] > o.y:
                    dy -= 6
                elif inimigos[i][1][1] < o.y:
                    dy += 6
                cerejaAzul(inimigos[i][1])
            elif ini[0] == 6:
                inimigos[i][3] += 1
                if inimigos[i][3] == 1000:
                    inimigos[i][3] = 0
                    for ini2 in inimigos:
                        i2 = inimigos.index(ini2)
                        inimigos[i2][4] += 1
                brocolis(inimigos[i][1])
            elif ini[0] == 7:
                if inimigos[i][1][0] > o.x:
                    dx -= 3
                elif inimigos[i][1][0] < o.x:
                    dx += 3
                if inimigos[i][1][1] > o.y:
                    dy -= 3
                elif inimigos[i][1][1] < o.y:
                    dy += 3
                abacate(inimigos[i][1])
            elif ini[0] == 8:
                inimigos[i][3] += 1
                if inimigos[i][3] % 10 == 0:
                    dx += random.randrange(-2, 3)
                    dy += random.randrange(-2, 3)
                if inimigos[i][3] % 80 == 0:
                    inimigos.append([0, [inimigos[i][1][0], inimigos[i][1][1]], [12, 18], 0, 1])
                if counter % 100 < 50:
                    pimentao(inimigos[i][1], 1)
                else:
                    pimentao(inimigos[i][1], 2)
            elif ini[0] == 9:
                inimigos[i][3] += 1
                dx += inimigos[i][5][0]
                dy += inimigos[i][5][1]
                if inimigos[i][1][0] > displayW-40-inimigos[i][2][0]:
                    inimigos[i][5][0] = -6
                if inimigos[i][1][0] < 40:
                    inimigos[i][5][0] = 6
                if inimigos[i][1][1] > displayH-40-inimigos[i][2][1]:
                    inimigos[i][5][1] = -6
                if inimigos[i][1][1] < 40:
                    inimigos[i][5][1] = 6

                if inimigos[i][3] % 50 == 0:
                    sementes.append([[inimigos[i][1][0], inimigos[i][1][1]], 0])
                if counter % 50 >= 0 and counter % 50 <= 25:
                    maca(inimigos[i][1], 2)
                else:
                    maca(inimigos[i][1], 1)
            elif ini[0] == 10:
                if inimigos[i][1][0] > o.x:
                    dx -= 2
                elif inimigos[i][1][0] < o.x:
                    dx += 2
                if inimigos[i][1][1] > o.y:
                    dy -= 2
                elif inimigos[i][1][1] < o.y:
                    dy += 2
                if counter % 50 == 0:
                    thornsIni.append([[inimigos[i][1][0], inimigos[i][1][1]], 90, 0])
                    thornsIni.append([[inimigos[i][1][0], inimigos[i][1][1]], 180, 0])
                    thornsIni.append([[inimigos[i][1][0], inimigos[i][1][1]], 270, 0])
                    thornsIni.append([[inimigos[i][1][0], inimigos[i][1][1]], 0, 0])
                tomate(inimigos[i][1])
            elif ini[0] == 11:
                inimigos[i][3] += 1
                if inimigos[i][3] >= 750:
                    caroco(inimigos[i][1], inimigos[i][3])
                else:
                    caroco(inimigos[i][1], 0)
                if inimigos[i][3] >= 762:
                    inimigos.remove(ini)
                    inimigos.append([7, [ini[1][0], ini[1][1]], [25, 25], 0, 5+dia])
                    continue
            elif ini[0] == 12:
                if counter % 600 <= 150:
                    dx += 3
                elif counter % 600 <= 300 and counter % 600 > 150:
                    dy += 3
                elif counter % 600 <= 450 and counter % 600 > 300:
                    dx -= 3
                elif counter % 600 <= 600 and counter % 600 > 450:
                    dy -= 3
                inimigos[i][3] += 1
                if inimigos[i][3] > 5 + inimigos[i][4]*20:
                    inimigos[i][3] = 0
                    R = math.degrees(math.atan2((o.x - inimigos[i][1][0]), (o.y - inimigos[i][1][1])))
                    acidos.append([inimigos[i][1][0], inimigos[i][1][1], R, 0])
                    Sm = random.randrange(0, 2)
                    if Sm == 1:
                        acidoSOM.play()
                    else:
                        acido2SOM.play()
                limao(inimigos[i][1])
            elif ini[0] == 13:
                inimigos[i][3] += 1
                if counter % 10 == 0:
                    dx += random.randrange(-5, 6)
                    dy += random.randrange(-5, 6)
                if inimigos[i][3] > 100:
                    inimigos[i][3] = 0
                    inimigos.append([2.5, [inimigos[i][1][0], inimigos[i][1][1]], [12, 18], 0, 3])
                    dx += random.randrange(-50, 51)
                    dy += random.randrange(-50, 51)
                pimentaoVerde(inimigos[i][1])
            elif ini[0] == 14:
                if ((o.x - inimigos[i][1][0])**2 + (o.y - inimigos[i][1][1])**2)**(1/2) < 150:
                    if inimigos[i][1][0] > o.x:
                        dx -= 4
                    elif inimigos[i][1][0] < o.x:
                        dx += 4
                    if inimigos[i][1][1] > o.y:
                        dy -= 4
                    elif inimigos[i][1][1] < o.y:
                        dy += 4
                else:
                    if counter % 6 == 0:
                        dx += random.randrange(-4, 5)
                        dy += random.randrange(-4, 5)
                blueBerry(inimigos[i][1])
            elif ini[0] == 15:
                inimigos[i][3] += 1
                if inimigos[i][3] > 300:
                    if inimigos[i][1][0] > o.x:
                        dx -= 8
                    elif inimigos[i][1][0] < o.x:
                        dx += 8
                    if inimigos[i][1][1] > o.y:
                        dy -= 8
                    elif inimigos[i][1][1] < o.y:
                        dy += 8
                else:
                    if counter % 10 == 0:
                        dx += random.randrange(-5, 6)
                        dy += random.randrange(-5, 6)
                PA = random.randrange(0, 5000)
                if PA == 0:
                    inimigos.append([3, [inimigos[i][1][0], inimigos[i][1][1]], [12, 18], 0, inimigos[i][4]])
                    inimigos.remove(ini)
                    continue
                pimentaPreta(inimigos[i][1])
            elif ini[0] == 20:
                if counter % 500 == 0:
                    psychics.append([1, inimigos[i][1][0], inimigos[i][1][1], 0])
                elif counter % 100 == 0:
                    psychics.append([0, inimigos[i][1][0], inimigos[i][1][1], 0])
                beterraba(inimigos[i][1])
            elif ini[0] == 25:
                if inimigos[i][1][0] > o.x:
                    dx += 1
                elif inimigos[i][1][0] < o.x:
                    dx -= 1
                if inimigos[i][1][1] > o.y:
                    dy += 1
                elif inimigos[i][1][1] < o.y:
                    dy -= 1
                if counter % 300 == 0:
                    inimigos.append([15, [inimigos[i][1][0], inimigos[i][1][1]], [12, 18], 0, 10+dia])
                pimentaoPreto(inimigos[i][1])
            elif ini[0] == 500:
                if inimigos[i][1][0] > o.x:
                    dx -= 1
                elif inimigos[i][1][0] < o.x:
                    dx += 1
                if inimigos[i][1][1] > o.y:
                    dy -= 1
                elif inimigos[i][1][1] < o.y:
                    dy += 1
                if counter % 400 <= 100:
                    dx += 3
                elif counter % 400 <= 100 and counter % 400 > 200:
                    dy += 3
                elif counter % 400 <= 200 and counter % 400 > 300:
                    dx -= 3
                elif counter % 400 <= 300 and counter % 400 > 400:
                    dy -= 3
                if counter % 60 == 0:
                    thornsIni.append([[inimigos[i][1][0], inimigos[i][1][1]], 0, -5])
                    thornsIni.append([[inimigos[i][1][0], inimigos[i][1][1]], 90, -5])
                    thornsIni.append([[inimigos[i][1][0], inimigos[i][1][1]], 180, -5])
                    thornsIni.append([[inimigos[i][1][0], inimigos[i][1][1]], 270, -5])
                    thornsIni.append([[inimigos[i][1][0], inimigos[i][1][1]], 45, -5])
                    thornsIni.append([[inimigos[i][1][0], inimigos[i][1][1]], 135, -5])
                    thornsIni.append([[inimigos[i][1][0], inimigos[i][1][1]], 225, -5])
                    thornsIni.append([[inimigos[i][1][0], inimigos[i][1][1]], 315, -5])
                Morango(inimigos[i][1])
            elif ini[0] == 600:
                if inimigos[i][4] < 50:
                    if inimigos[i][1][0] > o.x:
                        dx += 2
                    elif inimigos[i][1][0] < o.x:
                        dx -= 2
                    if inimigos[i][1][1] > o.y:
                        dy += 2
                    elif inimigos[i][1][1] < o.y:
                        dy -= 2
                else:
                    if inimigos[i][1][0] > o.x:
                        dx -= 2
                    elif inimigos[i][1][0] < o.x:
                        dx += 2
                    if inimigos[i][1][1] > o.y:
                        dy -= 2
                    elif inimigos[i][1][1] < o.y:
                        dy += 2
                R = math.degrees(math.atan2((o.x - inimigos[i][1][0]), (o.y - inimigos[i][1][1])))
                if (counter) % 75 == 0:
                    ervilhas.append([[inimigos[i][1][0]+15, inimigos[i][1][1]+10], 0, 0])
                if (counter+15) % 75 == 0:
                    ervilhas.append([[inimigos[i][1][0]+15, inimigos[i][1][1]+20], 0, 0])
                if (counter+30) % 75 == 0:
                    ervilhas.append([[inimigos[i][1][0]+15, inimigos[i][1][1]+30], 0, 0])
                if (counter+45) % 75 == 0:
                    ervilhas.append([[inimigos[i][1][0]+15, inimigos[i][1][1]+40], 0, 0])
                if (counter+60) % 75 == 0:
                    ervilhas.append([[inimigos[i][1][0]+15, inimigos[i][1][1]+50], 0, 0])
                vagem([inimigos[i][1][0], inimigos[i][1][1], R], counter % 40)
            elif ini[0] == 700:
                if counter % 100 == 0:
                    inimigos[i][4] += 1
                    boss += 1
                if inimigos[i][4] > 40+dia*10 or inimigos[i][4] < 50:
                    if inimigos[i][1][0] > o.x:
                        dx -= 4
                    elif inimigos[i][1][0] < o.x:
                        dx += 4
                    if inimigos[i][1][1] > o.y:
                        dy -= 4
                    elif inimigos[i][1][1] < o.y:
                        dy += 4
                else:
                    if inimigos[i][1][0] > o.x:
                        dx += 4
                    elif inimigos[i][1][0] < o.x:
                        dx -= 4
                    if inimigos[i][1][1] > o.y:
                        dy += 4
                    elif inimigos[i][1][1] < o.y:
                        dy -= 4
                berinjela(inimigos[i][1])
            elif ini[0] == 1000:
                if inimigos[i][1][0] > o.x:
                    dx -= 0.25
                elif inimigos[i][1][0] < o.x:
                    dx += 0.25
                if inimigos[i][1][1] > o.y:
                    dy -= 0.25
                elif inimigos[i][1][1] < o.y:
                    dy += 0.25
                if counter % 100 == 0:
                    thornsIni.append([[inimigos[i][1][0], inimigos[i][1][1]], 0, -5])
                    thornsIni.append([[inimigos[i][1][0], inimigos[i][1][1]], 90, -5])
                    thornsIni.append([[inimigos[i][1][0], inimigos[i][1][1]], 180, -5])
                    thornsIni.append([[inimigos[i][1][0], inimigos[i][1][1]], 270, -5])
                    thornsIni.append([[inimigos[i][1][0], inimigos[i][1][1]], 45, -5])
                    thornsIni.append([[inimigos[i][1][0], inimigos[i][1][1]], 135, -5])
                    thornsIni.append([[inimigos[i][1][0], inimigos[i][1][1]], 225, -5])
                    thornsIni.append([[inimigos[i][1][0], inimigos[i][1][1]], 315, -5])
                dx += (r_change - l_change)*o.v
                dy += (d_change - u_change)*o.v
                grapes(inimigos[i][1])
            elif ini[0] == 5000:
                if counter % 150 < 75:
                    if inimigos[i][1][0] > o.x:
                        dx -= 7
                    elif inimigos[i][1][0] < o.x:
                        dx += 7
                    if inimigos[i][1][1] > o.y:
                        dy -= 7
                    elif inimigos[i][1][1] < o.y:
                        dy += 7
                else:
                    if inimigos[i][1][0] > o.x:
                        dx += 7
                    elif inimigos[i][1][0] < o.x:
                        dx -= 7
                    if inimigos[i][1][1] > o.y:
                        dy += 7
                    elif inimigos[i][1][1] < o.y:
                        dy -= 7
                    if counter % 10 == 0:
                        magias.append([inimigos[i][1][0], inimigos[i][1][1], 0])
                R = math.degrees(math.atan2((o.x - inimigos[i][1][0]), (o.y - inimigos[i][1][1])))
                inimigos[i][4] += 1
                boss += 1
                if boss > Mboss:
                    Mboss = boss
                Emerson([inimigos[i][1][0], inimigos[i][1][1], R, counter % 150], counter % 18)
            if not colisaoBorda([inimigos[i][1][0]+dx, inimigos[i][1][1], inimigos[i][2][0], inimigos[i][2][1]]):
                inimigos[i][1][0] += dx
            if not colisaoBorda([inimigos[i][1][0], inimigos[i][1][1]+dy, inimigos[i][2][0], inimigos[i][2][1]]):
                inimigos[i][1][1] += dy

            if ((inimigos[i][1][0]>=o.x+o.w) or (inimigos[i][1][0]+inimigos[i][2][0]<=o.x) or (inimigos[i][1][1]+inimigos[i][2][1]<=o.y) or (inimigos[i][1][1]>=o.y+o.h)):
                pass
            else:
                C = 10
                if poderPassivo >= 10 and poderPassivo <= 12:
                    C = random.randrange(0, 10)
                if (C <= 3 and poderPassivo == 10) or (C <= 6 and poderPassivo == 11) or (C <= 8 and poderPassivo == 12):
                    if C <= 3:
                        o.agua += 1
                    elif C <= 7:
                        o.stamina += 0.4
                    else:
                        o.life += 0.2
                else:
                    o.dano(1)
                    if inimigos[i][0] in [14, 15, 20, 25, 700, 1000, 5000]:
                        o.Mlife -= 0.1
                        o.Wlife += 0.1
                    if escudoFogo > 0:
                        danoInimigo(i, ini, 4+poder9ativ*5*poder9lvl)
                        escudoFogo -= 1
                    else:
                        danoInimigo(i, ini, 1+poder9ativ*5*poder9lvl)
                continue
            for spor in spores:
                if ((inimigos[i][1][0]>=spor[0]+4) or (inimigos[i][1][0]+inimigos[i][2][0]<=spor[0]) or (inimigos[i][1][1]+inimigos[i][2][1]<=spor[1]) or (inimigos[i][1][1]>=spor[1]+4)):
                    pass
                else:
                    spores.remove(spor)
                    danoInimigo(i, ini, 1.1)
                    break
            try:
                for th in thorns:
                    if ((inimigos[i][1][0]>=th[0][0]+10) or (inimigos[i][1][0]+inimigos[i][2][0]<=th[0][0]) or (inimigos[i][1][1]+inimigos[i][2][1]<=th[0][1]) or (inimigos[i][1][1]>=th[0][1]+10)):
                        pass
                    else:
                        thorns.remove(th)
                        danoInimigo(i, ini, 1)
                        break
                for amg in minions:
                    if ((inimigos[i][1][0]>=amg[0][0]+11) or (inimigos[i][1][0]+inimigos[i][2][0]<=amg[0][0]) or (inimigos[i][1][1]+inimigos[i][2][1]<=amg[0][1]) or (inimigos[i][1][1]>=amg[0][1]+9)):
                        pass
                    else:
                        ig = minions.index(amg)
                        minions[ig][1] -= 1
                        if minions[ig][1] <= 0:
                            minions.remove(amg)
                        if minions[ig][3] <= 2:
                            danoInimigo(i, ini, 1) 
                        elif minions[ig][3] == 3:
                            danoInimigo(i, ini, 2)
                        elif minions[ig][3] == 4:
                            danoInimigo(i, ini, 3)
                        break
                for p in plantas:
                    if ((inimigos[i][1][0]>=p[0]+8) or (inimigos[i][1][0]+inimigos[i][2][0]<=p[0]) or (inimigos[i][1][1]+inimigos[i][2][1]<=p[1]) or (inimigos[i][1][1]>=p[1]+8)):
                        pass
                    else:
                        plantas.remove(p)
                for v in vines:
                    if ((inimigos[i][1][0]>=v[0][0]+20) or (inimigos[i][1][0]+inimigos[i][2][0]<=v[0][0]) or (inimigos[i][1][1]+inimigos[i][2][1]<=v[0][1]) or (inimigos[i][1][1]>=v[0][1]+10)):
                        pass
                    else:
                        iv = vines.index(v)
                        vines[iv][2] += 1
                        danoInimigo(i, ini, 1)
            except:
                continue
        
        for amigo in minions:
            i = minions.index(amigo)
            if amigo[1] > minions[i][3]+0.5*minions[i][2] and (len(minions) > 10 or (((o.x - amigo[0][0])**2 + (o.y - amigo[0][1])**2)**(1/2) < (35 + (25*poder5lvl)))):
                perto = []
                for inimigo in inimigos:
                    Dx = o.x - inimigo[1][0]
                    Dy = o.y - inimigo[1][1]
                    Dt = (Dx**2 + Dy**2)**(1/2)
                    if Dt <= (35 + (25*poder5lvl)):
                        ii = inimigos.index(inimigo)
                        perto.append([Dt, ii])
                perto.sort()
                try:
                    ii = perto[0][1]
                    if amigo[0][0] > inimigos[ii][1][0]:
                        amigo[0][0] -= 5
                    elif amigo[0][0] < inimigos[ii][1][0]:
                        amigo[0][0] += 5
                    if amigo[0][1] > inimigos[ii][1][1]:
                        amigo[0][1] -= 5
                    elif amigo[0][1] < inimigos[ii][1][1]:
                        amigo[0][1] += 5
                except:
                    if counter % 5 == 0:
                        amigo[0][0] += random.randrange(-3, 4)
                        amigo[0][1] += random.randrange(-3, 4)
            else:
                if amigo[0][0] > o.x+9:
                    amigo[0][0] -= 3*poder5lvl
                elif amigo[0][0] < o.x+9:
                    amigo[0][0] += 3*poder5lvl
                if amigo[0][1] > o.y+8:
                    amigo[0][1] -= 3*poder5lvl
                elif amigo[0][1] < o.y+8:
                    amigo[0][1] += 3*poder5lvl
            if minions[i][1] < 5*minions[i][3]+minions[i][2]*2:
                minions[i][1] += 0.003*minions[i][3]
            if minions[i][3] == 4:
                minions[i][4] += 1
                if minions[i][4] >= 1500:
                    minions.append([[amigo[0][0], amigo[0][1]], 5, 0, 1])
                    minions[i][4] = 0
            plantinha([amigo[0][0], amigo[0][1]], minions[i][3])
        
        for item in itens:
            if ((o.x >= item[1][0]+item[2][0]) or (o.x+o.w<=item[1][0]) or (o.y+o.h<=item[1][1]) or (o.y>=item[1][1]+item[2][1])):
                if item[0] == 0:
                    gameDisplay.blit(passivo1itemImg, item[1])
                if item[0] == 1:
                    gameDisplay.blit(passivo2itemImg, item[1])
                if item[0] == 2:
                    gameDisplay.blit(cerejaBombaImg, item[1])
                if item[0] == 3:
                    gameDisplay.blit(passivo3itemImg, item[1])
                if item[0] == 4:
                    gameDisplay.blit(passivo4itemImg, item[1])
                if item[0] == 5:
                    gameDisplay.blit(passivo5itemImg, item[1])
                if item[0] == 6:
                    gameDisplay.blit(passivo6itemImg, item[1])
            else:
                if item[0] == 0:
                    o.Mstamina += 5
                    if poderPassivo == 1:
                        poderPassivo = 2
                    elif poderPassivo == 2:
                        poderPassivo = 3
                    elif poderPassivo != 3:
                        poderPassivo = 1
                elif item[0] == 1:
                    o.Magua += 10
                    if poderPassivo == 4:
                        poderPassivo = 5
                    elif poderPassivo == 5:
                        poderPassivo = 6
                    elif poderPassivo != 6:
                        poderPassivo = 4
                elif item[0] == 2:
                    bombas += 1
                elif item[0] == 3:
                    o.Mlife += 4
                    if poderPassivo == 7:
                        poderPassivo = 8
                    elif poderPassivo == 8:
                        poderPassivo = 9
                    elif poderPassivo != 9:
                        poderPassivo = 7
                elif item[0] == 4:
                    if poderPassivo == 10:
                        poderPassivo = 11
                    elif poderPassivo == 11:
                        poderPassivo = 12
                    elif poderPassivo != 12:
                        poderPassivo = 10
                elif item[0] == 5:
                    o.Mlife += 1
                    o.Mstamina += 2.5
                    o.Magua += 10
                    if poderPassivo == 13:
                        poderPassivo = 14
                    elif poderPassivo == 14:
                        poderPassivo = 15
                    elif poderPassivo != 15:
                        poderPassivo = 13
                elif item[0] == 6:
                    if o.Wlife > 1:
                        o.Wlife -= 2
                        o.Mlife += 2
                    if poderPassivo == 16:
                        poderPassivo = 17
                    elif poderPassivo == 17:
                        poderPassivo = 18
                    elif poderPassivo != 18:
                        poderPassivo = 16
                passivoSOM.play()
                itens.remove(item)

        o.R = o.R*7/8 + math.degrees(math.asin((r_change - l_change)/(0.00001+(((r_change - l_change)**2 + (d_change - u_change)**2)**(1/2)))))/8
        o.Rotina(counter, cicloDia, xmont, ymont)
        if escudo > 0:
            gameDisplay.blit(escudoImg, ((o.x+o.w/2)-30, (o.y+o.h/2)-30))
            o.agua += 0.1
            escudo -= 0.1
        if escudoFogo > 0:
            gameDisplay.blit(escudoFogoImg, ((o.x+o.w/2)-30, (o.y+o.h/2)-30))
            o.life -= 0.01
            escudoFogo -= 0.01
        montanha((xmont, ymont))
        if cicloDia < 0.3:
            noite = pygame.Surface((displayW, displayH))
            noite.fill((20, 20, 20))
            lanterna = Luz.convert_alpha()
            lanterna = pygame.transform.scale(lanterna, (120, 120))
            lantRect = lanterna.get_rect()
            lantRect.center = (o.x+o.w/2, o.y+o.h/2)
            noite.blit(lanterna, lantRect)
            gameDisplay.blit(noite, (0,0), special_flags= pygame.BLEND_MULT)
        else:
            surface = pygame.Surface((displayW, displayH), pygame.SRCALPHA)
            pygame.draw.circle(surface, pygame.Color(243, 170, 12, blast),(o.x+o.w/2, o.y+o.h/2), (35 + 25*poder2lvl))
            gameDisplay.blit(surface, (0,0))
                
        if poder == 1:
            if o.level >= 16:
                gameDisplay.blit(poder13Img, (8, 560))
            elif o.level >= 7:
                gameDisplay.blit(poder12Img, (8, 560))
            else:
                gameDisplay.blit(poder11Img, (8, 560))
        elif poder == 2:
            if o.level >= 17:
                gameDisplay.blit(poder23Img, (8, 560))
            elif o.level >= 8:
                gameDisplay.blit(poder22Img, (8, 560))
            else:
                gameDisplay.blit(poder21Img, (8, 560))
        elif poder == 3:
            if o.level >= 18:
                gameDisplay.blit(poder33Img, (8, 560))
            elif o.level >= 9:
                gameDisplay.blit(poder32Img, (8, 560))
            else:
                gameDisplay.blit(poder31Img, (8, 560))
        elif poder == 4:
            if o.level >= 19:
                gameDisplay.blit(poder43Img, (8, 560))
            elif o.level >= 10:
                gameDisplay.blit(poder42Img, (8, 560))
            elif o.level >= 2:
                gameDisplay.blit(poder41Img, (8, 560))
            else:
                gameDisplay.blit(poderBloqueadoImg, (8, 560))
        elif poder == 5:
            if o.level >= 20:
                gameDisplay.blit(poder53Img, (8, 560))
            elif o.level >= 11:
                gameDisplay.blit(poder52Img, (8, 560))
            elif o.level >= 3:
                gameDisplay.blit(poder51Img, (8, 560))
            else:
                gameDisplay.blit(poderBloqueadoImg, (8, 560))
        elif poder == 6:
            if o.level >= 21:
                gameDisplay.blit(poder63Img, (8, 560))
            elif o.level >= 12:
                gameDisplay.blit(poder62Img, (8, 560))
            elif o.level >= 4:
                gameDisplay.blit(poder61Img, (8, 560))
            else:
                gameDisplay.blit(poderBloqueadoImg, (8, 560))
        elif poder == 7:
            if o.level >= 22:
                gameDisplay.blit(poder73Img, (8, 560))
            elif o.level >= 13:
                gameDisplay.blit(poder72Img, (8, 560))
            else:
                gameDisplay.blit(poder71Img, (8, 560))
            escrever('x %d' % bombas, 15, (25, 550))
        elif poder == 8:
            if o.level >= 23:
                gameDisplay.blit(poder83Img, (8, 560))
            elif o.level >= 14:
                gameDisplay.blit(poder82Img, (8, 560))
            elif o.level >= 5:
                gameDisplay.blit(poder81Img, (8, 560))
            else:
                gameDisplay.blit(poderBloqueadoImg, (8, 560))
        elif poder == 9:
            if o.level >= 24:
                gameDisplay.blit(poder93Img, (8, 560))
            elif o.level >= 15:
                gameDisplay.blit(poder92Img, (8, 560))
            elif o.level >= 6:
                gameDisplay.blit(poder91Img, (8, 560))
            else:
                gameDisplay.blit(poderBloqueadoImg, (8, 560))
        elif poder == 0:
            if o.level >= 25:
                gameDisplay.blit(poder0Img, (8, 560))
            else:
                gameDisplay.blit(poderBloqueadoImg, (8, 560))

        if poderPassivo == 0:
            gameDisplay.blit(slotImg, (48, 560))
        elif poderPassivo == 1:
            gameDisplay.blit(passivo11Img, (48, 560))
        elif poderPassivo == 2:
            gameDisplay.blit(passivo12Img, (48, 560))
        elif poderPassivo == 3:
            gameDisplay.blit(passivo13Img, (48, 560))
        elif poderPassivo == 4:
            gameDisplay.blit(passivo21Img, (48, 560))
        elif poderPassivo == 5:
            gameDisplay.blit(passivo22Img, (48, 560))
        elif poderPassivo == 6:
            gameDisplay.blit(passivo23Img, (48, 560))
        elif poderPassivo == 7:
            gameDisplay.blit(passivo31Img, (48, 560))
        elif poderPassivo == 8:
            gameDisplay.blit(passivo32Img, (48, 560))
        elif poderPassivo == 9:
            gameDisplay.blit(passivo33Img, (48, 560))
        elif poderPassivo == 10:
            gameDisplay.blit(passivo41Img, (48, 560))
        elif poderPassivo == 11:
            gameDisplay.blit(passivo42Img, (48, 560))
        elif poderPassivo == 12:
            gameDisplay.blit(passivo43Img, (48, 560))
        elif poderPassivo == 13:
            gameDisplay.blit(passivo51Img, (48, 560))
        elif poderPassivo == 14:
            gameDisplay.blit(passivo52Img, (48, 560))
        elif poderPassivo == 15:
            gameDisplay.blit(passivo53Img, (48, 560))
        elif poderPassivo == 16:
            gameDisplay.blit(passivo61Img, (48, 560))
        elif poderPassivo == 17:
            gameDisplay.blit(passivo62Img, (48, 560))
        elif poderPassivo == 18:
            gameDisplay.blit(passivo63Img, (48, 560))

        cicloDia += diaNoite*0.0004
        if o.Vlife > 0:
            o.Vlife -= 0.01
        if cicloDia < 0:
            cicloDia = 0
            dia += 1
            diaNoite = 1
            o.Mlife += 1.5
            o.Mstamina += 4
            o.Magua += 7
            if o.Wlife > 0:
                o.Wlife -= 1
                o.life += 1
            if o.Wlife < 0:
                o.life += o.Wlife
                o.Wlife = 0
            for amg in minions:
                i = minions.index(amg)
                minions[i][2] += 1
        elif cicloDia > 1:
            diaNoite = -1
        if counter % 80 == 0:
            o.agua -= 1
        if o.agua <= 0:
            o.life += o.agua/100
        if poderPassivo == 18 and o.Wlife > 0:
            o.Mlife += 0.002*o.Wlife
            o.agua -= 0.02*o.Wlife
            o.Wlife -= 0.001*o.Wlife
        if poderPassivo == 16 and o.Wlife > 0:
            o.Wlife -= 0.0006
            o.Mlife += 0.002
            o.agua -= 0.002
        if poderPassivo == 17 and o.Wlife > 0:
            o.Wlife -= 0.002
            o.Mlife += 0.005
            o.agua -= 0.004
        if o.agua >= 0.5*poder4lvl and poder4ativ == 1:
            o.agua -= 0.5*poder4lvl
            if poder4lvl == 3:
                o.agua -= 1
            if o.stamina < o.Mstamina:
                o.stamina += 0.1*poder4lvl**2
        if o.life >= 1 and poder9ativ == 1:
            o.dano(0.3*poder9lvl)
        if poderPassivo >= 1 and poderPassivo <= 3:
            o.agua -= 0.025*poderPassivo
            o.stamina += 0.07*poderPassivo
        
        if boss > 0:
            pygame.draw.rect(gameDisplay, (127, 22, 0), [100, 550, 600, 20])
            pygame.draw.rect(gameDisplay, red, [100, 550, boss*600/Mboss, 20])
        if o.stamina >= o.Mstamina:
            o.stamina = o.Mstamina
        if o.agua > o.Magua:
            o.agua -= 0.05
            if o.agua > 2*o.Magua:
                o.agua = 2*o.Magua
        if (o.life + o.Vlife) > o.Mlife:
            if o.Vlife > 0:
                o.Vlife = 0
            o.life = o.Mlife
        if o.rage < 0:
            o.rage = 0
        if counter % 45 == 0:
            o.rage -= 1
        if o.Mlife*10*TamanhoBarra + o.Wlife*10*TamanhoBarra + o.Vlife*10*TamanhoBarra  > displayW-50 or o.Mstamina*4*TamanhoBarra > displayW-50 or o.Magua*TamanhoBarra > displayW-50:
            TamanhoBarra *= 0.5

        pygame.draw.rect(gameDisplay, (140, 0, 0), [15, 14, (o.Mlife*10+o.Wlife*10)*TamanhoBarra+4, 14])
        pygame.draw.rect(gameDisplay, red, [17, 16, o.Mlife*10*TamanhoBarra, 10])
        if poder9ativ == 0:
            pygame.draw.rect(gameDisplay, green, [17, 16, o.life*10*TamanhoBarra, 10])
            pygame.draw.rect(gameDisplay, (150, 200, 100), [17+o.life*10*TamanhoBarra, 16, o.Vlife*10*TamanhoBarra, 10])
        elif poder9ativ == 1:
            pygame.draw.rect(gameDisplay, (255, 150, 150), [17, 16, o.life*10*TamanhoBarra, 10])
        pygame.draw.rect(gameDisplay, black, [17+o.Mlife*10*TamanhoBarra, 16, o.Wlife*10*TamanhoBarra, 10])
        pygame.draw.rect(gameDisplay, black, [15, 29, o.Mstamina*4*TamanhoBarra+4, 14])
        pygame.draw.rect(gameDisplay, (220, 111, 43), [17, 31, o.Mstamina*4*TamanhoBarra, 10])
        PorRage = o.rage/o.Mrage
        if PorRage > 1 and counter % 10 < 5:
            pygame.draw.rect(gameDisplay, (255, 255, 255), [17, 31, o.Mstamina*4*TamanhoBarra, 10])
        elif PorRage > 1 and counter % 10 < 10:
            pygame.draw.rect(gameDisplay, (255, 0, 0), [17, 31, o.Mstamina*4*TamanhoBarra, 10])
        else:
            pygame.draw.rect(gameDisplay, (255, 150, 150), [17, 31, (PorRage)*o.Mstamina*4*TamanhoBarra, 10])
        pygame.draw.rect(gameDisplay, yellow, [17, 31, o.stamina*4*TamanhoBarra, 10])
        pygame.draw.rect(gameDisplay, black, [15, 44, o.Magua*TamanhoBarra+4, 14])
        pygame.draw.rect(gameDisplay, (0, 137, 114), [17, 46, o.Magua*TamanhoBarra, 10])
        if o.agua < o.Magua:
            if poder4ativ == 0:
                pygame.draw.rect(gameDisplay, blue, [17, 46, o.agua*TamanhoBarra, 10])
            elif poder4ativ == 1:
                pygame.draw.rect(gameDisplay, (8, 244, 225), [17, 46, o.agua*TamanhoBarra, 10])
        else:
            if poder4ativ == 0:
                pygame.draw.rect(gameDisplay, blue, [17, 46, o.Magua*TamanhoBarra, 10])
                pygame.draw.rect(gameDisplay, (77, 169, 190), [17, 46, (o.agua-o.Magua)*TamanhoBarra, 10])
            elif poder4ativ == 1:
                pygame.draw.rect(gameDisplay, (8, 244, 225), [17, 46, o.Magua*TamanhoBarra, 10])
        if poder == 1:
            if o.stamina >= 1 and poder1lvl == 1:
                pygame.draw.rect(gameDisplay, orange, [17, 31, 4*TamanhoBarra, 10])
            elif o.stamina >= 1.5 and poder1lvl == 2:
                pygame.draw.rect(gameDisplay, orange, [17, 31, 6*TamanhoBarra, 10])
            elif o.stamina >= 2 and poder1lvl == 3:
                pygame.draw.rect(gameDisplay, orange, [17, 31, 8*TamanhoBarra, 10])
        elif poder == 2:
            if o.stamina >= 5 and poder2lvl == 1:
                pygame.draw.rect(gameDisplay, orange, [17, 31, 20*TamanhoBarra, 10])
            elif o.stamina >= 10 and poder2lvl == 2:
                pygame.draw.rect(gameDisplay, orange, [17, 31, 40*TamanhoBarra, 10])
            elif o.stamina >= 15 and poder2lvl == 3:
                pygame.draw.rect(gameDisplay, orange, [17, 31, 60*TamanhoBarra, 10])
        elif poder == 3:
            if o.stamina > 2 and poder3lvl == 1:
                pygame.draw.rect(gameDisplay, orange, [17, 31, 8*TamanhoBarra, 10])
            elif o.stamina > 3 and poder3lvl == 2:
                pygame.draw.rect(gameDisplay, orange, [17, 31, 12*TamanhoBarra, 10])
            elif o.stamina > 5 and poder3lvl == 3:
                pygame.draw.rect(gameDisplay, orange, [17, 31, 20*TamanhoBarra, 10])
        elif poder == 4:
            pass
        elif poder == 5:
            if poder5lvl == 1 and o.stamina > 10 and o.life > 3 and o.agua > 25:
                pygame.draw.rect(gameDisplay, orange, [17, 31, 40*TamanhoBarra, 10])
                pygame.draw.rect(gameDisplay, (0, 200, 0), [17, 16, 30*TamanhoBarra, 10])
                pygame.draw.rect(gameDisplay, (0, 0, 200), [17, 46, 25*TamanhoBarra, 10])
            elif poder5lvl == 2 and o.stamina > 15 and o.life > 6 and o.agua > 50:
                pygame.draw.rect(gameDisplay, orange, [17, 31, 60*TamanhoBarra, 10])
                pygame.draw.rect(gameDisplay, (0, 200, 0), [17, 16, 60*TamanhoBarra, 10])
                pygame.draw.rect(gameDisplay, (0, 0, 200), [17, 46, 50*TamanhoBarra, 10])
            elif poder5lvl == 3 and o.stamina > 20 and o.life > 9 and o.agua > 100:
                pygame.draw.rect(gameDisplay, orange, [17, 31, 80*TamanhoBarra, 10])
                pygame.draw.rect(gameDisplay, (0, 200, 0), [17, 16, 90*TamanhoBarra, 10])
                pygame.draw.rect(gameDisplay, (0, 0, 200), [17, 46, 100*TamanhoBarra, 10])
        elif poder == 6:
            if poder6lvl == 1 and o.stamina > 10 and o.agua > 20:
                pygame.draw.rect(gameDisplay, orange, [17, 31, 40*TamanhoBarra, 10])
                pygame.draw.rect(gameDisplay, (0, 0, 200), [17, 46, 20*TamanhoBarra, 10])
            elif poder6lvl == 2 and o.stamina > 15 and o.agua > 40:
                pygame.draw.rect(gameDisplay, orange, [17, 31, 60*TamanhoBarra, 10])
                pygame.draw.rect(gameDisplay, (0, 0, 200), [17, 46, 40*TamanhoBarra, 10])
            elif poder6lvl == 3 and o.stamina > 20 and o.agua > 80:
                pygame.draw.rect(gameDisplay, orange, [17, 31, 80*TamanhoBarra, 10])
                pygame.draw.rect(gameDisplay, (0, 0, 200), [17, 46, 80*TamanhoBarra, 10])
        elif poder == 7:
            pass
        elif poder == 8:
            if poder8lvl == 1 and o.stamina >= 12 and o.life > 2:
                pygame.draw.rect(gameDisplay, orange, [17, 31, 48*TamanhoBarra, 10])
                pygame.draw.rect(gameDisplay, (0, 200, 0), [17, 16, 20*TamanhoBarra, 10])
            elif poder8lvl == 2 and o.stamina >= 20 and o.life > 2:
                pygame.draw.rect(gameDisplay, orange, [17, 31, 80*TamanhoBarra, 10])
                pygame.draw.rect(gameDisplay, (0, 200, 0), [17, 16, 20*TamanhoBarra, 10])
            elif poder8lvl == 3 and o.stamina >= 7 and o.life > 1:
                TempStamina = o.stamina
                Templife = o.life
                vezes = 0
                for numero in range(8):
                    if TempStamina >= 7 and Templife > 1:
                        vezes += 1
                        TempStamina -= 7
                        Templife -= 1
                pygame.draw.rect(gameDisplay, orange, [17, 31, vezes*28*TamanhoBarra, 10])
                pygame.draw.rect(gameDisplay, (0, 200, 0), [17, 16, 10*vezes*TamanhoBarra, 10])
        elif poder == 9 and o.stamina > 1:
            pass
        elif poder == 0 and o.stamina > 40 and o.life > 15 and o.agua > 100:
            pygame.draw.rect(gameDisplay, orange, [17, 31, 160*TamanhoBarra, 10])
            pygame.draw.rect(gameDisplay, (0, 200, 0), [17, 16, 150*TamanhoBarra, 10])
            pygame.draw.rect(gameDisplay, (0, 0, 200), [17, 46, 100*TamanhoBarra, 10])

        escreverCanto('Score: %d' % score, 15, (17, 75))
        escreverCanto('Dias sobrevividos: %d' % dia, 15, (17, 95))

        counter += 1
        clock.tick(30)
        pygame.display.update()
    SALADAMUSICA.stop()
    extrahard.stop()
    hard.stop()
    Nightmare.stop()
    return score, dia

def upXP(score):
    global o
    o.xp += score
    while o.xp >= 250*(1.1**(o.level - 1)):
        o.xp -= 250*(1.1**(o.level - 1))
        o.level += 1
    orquideas[iorq][5] = o.level
    orquideas[iorq][6] = o.xp
    with open('Imagens/Statos.txt', 'w') as file:
        file.writelines('1|8|20|100|1|%s|%s \n' % (orquideas[0][5], orquideas[0][6]))
        file.writelines('2|20|5|80|0.8|%s|%s \n' % (orquideas[1][5], orquideas[1][6]))
        file.writelines('3|5|10|250|1.25|%s|%s \n' % (orquideas[2][5], orquideas[2][6]))
        file.writelines('4|15|20|200|1.5|%s|%s' % (orquideas[3][5], orquideas[3][6]))
        
def helpp():
    Mostra = True
    with open('Imagens/Statos.txt', 'r') as file:
        info = file.read()
        info = info.split('\n')
        Mlevel = 0
        for orq in info:
            orqs = [float(temp) for temp in orq.split('|')]
            level = orqs[5]
            if level > Mlevel:
                Mlevel = level
    while Mostra:
        gameDisplay.fill((221, 155, 11))
        gameDisplay.blit(poder11Img, (50, 10))
        escreverCanto('Leaves a trail of spores that damage enemies that step on it', 10, (50, 50))
        escreverCanto('Good for: Defending against suprise attacks from cherries', 10, (50, 65))
        escreverCanto('Rage: Summons 120 spores randomly in the field', 10, (50, 80))
        if Mlevel > 6:
            gameDisplay.blit(poder12Img, (85, 10))
        else:
            gameDisplay.blit(poderBloqueadoImg, (85, 10))
        if Mlevel > 15:
            gameDisplay.blit(poder13Img, (120, 10))
        else:
            gameDisplay.blit(poderBloqueadoImg, (120, 10))

        gameDisplay.blit(poder21Img, (50, 125))
        escreverCanto('Deals heavy damage to all enemies inside your light', 10, (50, 165))
        escreverCanto('Good for: Crowd control, killing lots of strong enemies', 10, (50, 180))
        escreverCanto('Rage: Deals insane damage to enemies inside your light', 10, (50, 195))
        if Mlevel > 7:
            gameDisplay.blit(poder22Img, (85, 125))
        else:
            gameDisplay.blit(poderBloqueadoImg, (120, 125))
        if Mlevel > 16:
            gameDisplay.blit(poder23Img, (120, 125))
        else:
            gameDisplay.blit(poderBloqueadoImg, (85, 125))

        gameDisplay.blit(poder31Img, (50, 245))
        escreverCanto('Shoots thorns that damage enemies', 10, (50, 285))
        escreverCanto('Good for: Crowd control, destroying high quantities of weak enemies', 10, (50, 300))
        escreverCanto('Rage: Shoots 360 thorns in a circle, they go farther than average', 10, (50, 315))
        if Mlevel > 8:
            gameDisplay.blit(poder32Img, (85, 245))
        else:
            gameDisplay.blit(poderBloqueadoImg, (85, 245))
        if Mlevel > 17:
            gameDisplay.blit(poder33Img, (120, 245))
        else:
            gameDisplay.blit(poderBloqueadoImg, (120, 245))
        
        if Mlevel > 1:
            gameDisplay.blit(poder41Img, (50, 365))
            escreverCanto('Fastly generates energy by consuming water, while also rising momentarily your defense', 10, (50, 405))
            escreverCanto('Good for: Not wasting extra water and protecting against highly resistent enemies', 10, (50, 420))
            escreverCanto('Rage: Creates a shield bubble, negating 90% of any damage and regenerating water', 10, (50, 435))
        else:
            gameDisplay.blit(poderBloqueadoImg, (50, 365))
            escreverCanto('???', 10, (50, 405))
            escreverCanto('Good for: ???', 10, (50, 420))
            escreverCanto('Rage: ???', 10, (50, 435))
        if Mlevel > 9:
            gameDisplay.blit(poder42Img, (85, 365))
        else:
            gameDisplay.blit(poderBloqueadoImg, (85, 365))
        if Mlevel > 18:
            gameDisplay.blit(poder43Img, (120, 365))
        else:
            gameDisplay.blit(poderBloqueadoImg, (120, 365))
        
        if Mlevel > 2:
            gameDisplay.blit(poder51Img, (50, 485))
            escreverCanto('Summons a little plant that will attack enemies in your range.', 10, (50, 525))
            escreverCanto('(Takes shelter in you when at low hp)', 10, (50, 535))
            escreverCanto('Good for: Killing enemies you shouldn\'t touch and protecting against cherries', 10, (50, 550))
            escreverCanto('Rage: Summons a giant plant with even higher stats. It can also create little plants.', 10, (50, 565))
        else:
            gameDisplay.blit(poderBloqueadoImg, (50, 485))
            escreverCanto('???', 10, (50, 525))
            escreverCanto('Good for: ???', 10, (50, 540))
            escreverCanto('Rage: ???', 10, (50, 555))
        if Mlevel > 10:
            gameDisplay.blit(poder52Img, (85, 485))
        else:
            gameDisplay.blit(poderBloqueadoImg, (85, 485))
        if Mlevel > 19:
            gameDisplay.blit(poder53Img, (120, 485))
        else:
            gameDisplay.blit(poderBloqueadoImg, (120, 485))

        if Mlevel > 3:
            gameDisplay.blit(poder61Img, (500, 10))
            escreverCanto('Creates a plant that heals you and your plants', 10, (500, 50))
            escreverCanto('at the cost of watering it (also removes wither effect)', 10, (500, 60))
            escreverCanto('Good for: Fast healing', 10, (500, 75))
            escreverCanto('Rage: Spreads level 1 and 2 plants.', 10, (500, 90))
            escreverCanto('Heals you and extends your maximum life', 10, (500, 100))
        else:
            gameDisplay.blit(poderBloqueadoImg, (500, 10))
            escreverCanto('???', 10, (500, 50))
            escreverCanto('Good for: ???', 10, (500, 65))
            escreverCanto('Rage: ???', 10, (500, 80))
        if Mlevel > 11:
            gameDisplay.blit(poder62Img, (535, 10))
        else:
            gameDisplay.blit(poderBloqueadoImg, (535, 10))
        if Mlevel > 20:
            gameDisplay.blit(poder63Img, (570, 10))
        else:
            gameDisplay.blit(poderBloqueadoImg, (570, 10))
        
        gameDisplay.blit(poder71Img, (500, 125))
        escreverCanto('Throw bombs that explodes on enemy contact', 10, (500, 165))
        escreverCanto('dealing high damage, but are consumable', 10, (500, 175))
        escreverCanto('Good for: Crowd control and destroying bosses', 10, (500, 190))
        escreverCanto('Rage: Throws 24 bombs at every direction', 10, (500, 205))
        if Mlevel > 12:
            gameDisplay.blit(poder72Img, (535, 125))
        else:
            gameDisplay.blit(poderBloqueadoImg, (535, 125))
        if Mlevel > 21:
            gameDisplay.blit(poder73Img, (570, 125))
        else:
            gameDisplay.blit(poderBloqueadoImg, (570, 125))

        if Mlevel > 4:
            gameDisplay.blit(poder81Img, (500, 245))
            escreverCanto('Shoots vampire vines that chase enemies and heals you', 10, (500, 285))
            escreverCanto('Good for: Fast healing and killing lots of small enemies', 10, (500, 300))
            escreverCanto('Rage: Shoots 3 vines each capable of dealing 40 damage', 10, (500, 315))
            escreverCanto('before returning', 10, (500, 325))
        else:
            gameDisplay.blit(poderBloqueadoImg, (500, 245))
            escreverCanto('???', 10, (500, 285))
            escreverCanto('Good for: ???', 10, (500, 300))
            escreverCanto('Rage: ???', 10, (500, 315))
        if Mlevel > 13:
            gameDisplay.blit(poder82Img, (535, 245))
        else:
            gameDisplay.blit(poderBloqueadoImg, (535, 245))
        if Mlevel > 22:
            gameDisplay.blit(poder83Img, (570, 245))
        else:
            gameDisplay.blit(poderBloqueadoImg, (570, 245))

        if Mlevel > 5:
            gameDisplay.blit(poder91Img, (500, 365))
            escreverCanto('Ignites you, dealing 5x more contact damage', 10, (500, 405))
            escreverCanto('but also damaging you', 10, (500, 415))
            escreverCanto('Good for: killing bosses, better with higher life', 10, (500, 430))
            escreverCanto('Rage: Creates a fire shield around you', 10, (500, 445))
            escreverCanto('that deals triple contact damage', 10, (500, 455))
        else:
            gameDisplay.blit(poderBloqueadoImg, (500, 365))
            escreverCanto('???', 10, (500, 405))
            escreverCanto('Good for: ???', 10, (500, 420))
            escreverCanto('Rage: ???', 10, (500, 435))
        if Mlevel > 14:
            gameDisplay.blit(poder92Img, (535, 365))
        else:
            gameDisplay.blit(poderBloqueadoImg, (535, 365))
        if Mlevel > 23:
            gameDisplay.blit(poder93Img, (570, 365))
        else:
            gameDisplay.blit(poderBloqueadoImg, (570, 365))
        
        if Mlevel > 24:
            gameDisplay.blit(poder0Img, (500, 485))
            escreverCanto('Deals insane damage to all enemies on the screen', 10, (500, 525))
            escreverCanto('at the cost of your life', 10, (500, 535))
            escreverCanto('Good for: Cleaning the screen if there are too much enemies', 10, (500, 550))
            escreverCanto('Rage: N/A', 10, (500, 565))
        else:
            gameDisplay.blit(poderBloqueadoImg, (500, 485))
            escreverCanto('???', 10, (500, 525))
            escreverCanto('Good for: ???', 10, (500, 540))
            escreverCanto('Rage: ???', 10, (500, 555))
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Mostra = False
        clock.tick(30)
        pygame.display.update()
    Mostra = True
    while Mostra:
        gameDisplay.fill((221, 155, 11))

        gameDisplay.blit(passivo11Img, (100, 50))
        gameDisplay.blit(passivo12Img, (135, 50))
        gameDisplay.blit(passivo13Img, (170, 50))
        escreverCanto('Pepper: Raises your energy regeneration, but consumes more water. Extends your maximum energy', 10, (100, 90))

        gameDisplay.blit(passivo21Img, (100, 150))
        gameDisplay.blit(passivo22Img, (135, 150))
        gameDisplay.blit(passivo23Img, (170, 150))
        escreverCanto('Watermelon jelly: Killing enemies regenerates water. Extends your maximum water', 10, (100, 190))
        
        gameDisplay.blit(passivo31Img, (100, 250))
        gameDisplay.blit(passivo32Img, (135, 250))
        gameDisplay.blit(passivo33Img, (170, 250))
        escreverCanto('Helmet: Lowers the damage you take. Extends your maximum life', 10, (100, 290))
        
        gameDisplay.blit(passivo41Img, (100, 350))
        gameDisplay.blit(passivo42Img, (135, 350))
        gameDisplay.blit(passivo43Img, (170, 350))
        escreverCanto('Lettuce cape: Gives you a chance to evade attacks. successful evades regenerates your water, energy and life', 10, (100, 390))
        
        gameDisplay.blit(passivo51Img, (100, 450))
        gameDisplay.blit(passivo52Img, (135, 450))
        gameDisplay.blit(passivo53Img, (170, 450))
        escreverCanto('Trophy: Killing enemies generates energy shield, level 3 can also generates a fire shield', 10, (100, 490))
        
        gameDisplay.blit(passivo61Img, (100, 530))
        gameDisplay.blit(passivo62Img, (135, 530))
        gameDisplay.blit(passivo63Img, (170, 530))
        escreverCanto('Poisoned Apple: Passively heals wither effect, giving back double the Life points withered', 10, (100, 570))
        
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Mostra = False
        clock.tick(30)
        pygame.display.update()
    
    Mostra = True
    tempMaxRage = 200
    tempRage = 0
    tempMaxStamina = 40
    counter = 1
    tempStamina = 5
    tempMaxLife = 20
    TempMaxWLife = 5
    TempLife = 10
    while Mostra:
        gameDisplay.fill((221, 155, 11))

        escreverCanto('Rage: Killing enemies or taking damage will raise your rage bar', 10, (50, 50))
        escreverCanto('shown as the white part of your maxium energy bar)', 10, (50, 60))
        escreverCanto('When your Rage bar gets full, it will flash in red', 10, (50, 70))
        escreverCanto('if you attack while the bar is full, you will release a powerful attack based on the power you have selected', 10, (50, 80))
        escreverCanto('After the attack, your energy bar will be depleated and your maximum energy raised by 4', 10, (50, 90))
        tempRage += 1
        counter += 1
        tempStamina += 0.1
        pygame.draw.rect(gameDisplay, black, [48, 108, tempMaxStamina*4+4, 14])
        pygame.draw.rect(gameDisplay, (220, 111, 43), [50, 110, tempMaxStamina*4, 10])
        PorRage = tempRage/tempMaxRage
        if PorRage > 1 and counter % 10 < 5:
            pygame.draw.rect(gameDisplay, (255, 255, 255), [50, 110, tempMaxStamina*4, 10])
        elif PorRage > 1 and counter % 10 < 10:
            pygame.draw.rect(gameDisplay, (255, 0, 0), [50, 110, tempMaxStamina*4, 10])
        else:
            pygame.draw.rect(gameDisplay, (255, 150, 150), [50, 110, (PorRage)*tempMaxStamina*4, 10])
        pygame.draw.rect(gameDisplay, yellow, [50, 110, tempStamina*4, 10])
        if tempRage > 250:
            tempRage = 0
            tempStamina = 0
            tempMaxStamina += 4
            if tempMaxStamina > 100:
                tempMaxStamina = 40

        escreverCanto('Certain enemies and powers can wither your maximum life, this will be shown as the black part in your life bar', 10, (50, 140))
        escreverCanto('This temporarily reduces your maximum life. You will gradually recover it, (at the rate of 1 life/day)', 10, (50, 150))
        escreverCanto('but certain powers can help recover it faster', 10, (50, 160))
        pygame.draw.rect(gameDisplay, (140, 0, 0), [48, 198, tempMaxLife*10+4+TempMaxWLife*10, 14])
        pygame.draw.rect(gameDisplay, red, [50, 200, tempMaxLife*10, 10])
        pygame.draw.rect(gameDisplay, green, [50, 200, TempLife*10, 10])
        pygame.draw.rect(gameDisplay, black, [50+tempMaxLife*10, 200, TempMaxWLife*10, 10])


        escreverCanto('This is your water bar, if it reaches 0, you will start taking damage', 10, (50, 250))
        escreverCanto('The higher your bar is, the more energy and life you\'ll regenerate over time (this is also limited by time, at night your regeneration is much slower)', 10, (50, 260))
        pygame.draw.rect(gameDisplay, black, [48, 298, 154, 14])
        pygame.draw.rect(gameDisplay, (0, 137, 114), [50, 300, 150, 10])
        pygame.draw.rect(gameDisplay, blue, [50, 300, 130, 10])

        escreverCanto('You can run by pressing Z', 10, (50, 350))
        escreverCanto('If your health, energy or water bar gets too big for the screen', 10, (50, 400))
        escreverCanto('it will be cut in half, this does not affect your total stats, it\'s purely visual.', 10, (50, 410))
        escreverCanto('Some enemies have special abilities, Lemons can poison you, black enemies can wither your life, Broccoli can Heal enemies... etc', 10, (50, 460))
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Mostra = False
        clock.tick(30)
        pygame.display.update()

def board():
    while True:
        gameDisplay.blit(gameMenu, (0, 0))
        with open('Imagens/LeaderBoard.txt', 'r') as file:
            Leaders = file.read()
            Leaders = Leaders.split('\n')
        yt = 100
        LeadersOrdem = []
        for l in Leaders:
            l = l.split(', ')
            if len(l) < 2:
                break
            LeadersOrdem.append([int(l[0]), int(l[1])])
        LeadersOrdem.sort(reverse=True)
        for l in LeadersOrdem:
            escreverCanto('Score: %s | Dias: %s' % (l[0], l[1]), 15, (200, yt))
            yt += 20
            if yt > 400:
                break
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return 0
Start = True
dificuldade = 1
orquidea = 1
nome = 'Cycnoches'
leveis = []
chacList = ["orquidea", "nome", "orc1Img", "orc2Img"]
chacList[1] = 'Cycnoches'
chacList[2] = cycnoches1Img
chacList[3] = cycnoches2Img
sel = 1
with open('Imagens/Statos.txt', 'r') as file:
    info = file.read()
    info = info.split('\n')
    for orq in info:
        orqs = [float(temp) for temp in orq.split('|')]
        leveis.append(orqs[5])
while Start:
    Play = True
    gameMenu = pygame.image.load('imagens\Garden.png')
    gameDisplay.blit(gameMenu, (0, 0))
    escrever("Orchiller", 50, [400, 50])
    escrever("Use the arrows to navigate through this menu.", 25, [400, 540])
    dislaySel()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Start = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if sel == 1:
                    sel = 6                    
                else:
                    sel -= 1
            elif event.key == pygame.K_DOWN:
                if sel == 6:
                    sel = 1
                else:
                    sel += 1
            if event.key == pygame.K_SPACE:
                if sel == 6:
                    Start = False
                elif sel == 3:
                    chacList, orquidea = character(chacList, orquidea)
                elif sel == 5:
                    dificuldade = difficulty(dificuldade)
                elif sel == 2:
                    helpp()
                elif sel == 4:
                    board()
                elif sel == 1:
                    nome = chacList[1]
                    orc1Img = chacList[2]
                    orc2Img = chacList[3]
                    score, dia = gameLoop(dificuldade)
                    deathSOM.play()
                    with open('Imagens/LeaderBoard.txt', 'a') as file:
                        file.writelines('%d, %d \n' % (score, dia))
                    if dificuldade in [1, 2, 3, 4]:
                        score = score*dificuldade - 100*(dificuldade-1)
                        upXP(score)
                    else:
                        score = 0
                    with open('Imagens/Statos.txt', 'r') as file:
                        info = file.read()
                        info = info.split('\n')
                        leveis = []
                        for orq in info:
                            orqs = [float(temp) for temp in orq.split('|')]
                            leveis.append(orqs[5])
                    pygame.time.delay(500)
                    while Play:
                        gameDisplay.fill((221, 155, 11))
                        escrever("You died. Press SPACE to go to the menu and ESCAPE to quit", 15, (400, 300))
                        escrever("Your highscore was %d, and you survived for %d day(s)" % (score, dia), 15, (400, 350))
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                Start = False
                                Play = False
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    Start = True
                                    Play = False                            
                                if event.key == pygame.K_ESCAPE:
                                    Start = False
                                    Play = False