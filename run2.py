from pygame.locals import *
import pygame
import time
import random

from scripts.Matrix import Matrix

iconSize = (150, 150)  # (y, x)
totalWidthAndHeight = 5
windowWidth = iconSize[0] * totalWidthAndHeight
windowHeight = iconSize[0] * totalWidthAndHeight

pygame.init()
boardGame = pygame.display.set_mode((windowWidth, windowHeight), pygame.HWSURFACE)
boardGame.fill((255, 255, 255))
pygame.display.set_caption('Pygame pythonspot.com example')

_image_iron_man = pygame.image.load(r"C:\Users\franc\Desktop\Francisco\2ºano\Intro_ai\trabalho_final\trabalho_final\pygame_iia_trab_final\textures\iron-man.png").convert_alpha()
_image_iron_man = pygame.transform.scale(_image_iron_man, (iconSize[0], iconSize[1]))

_image_garbage = pygame.image.load(r"C:\Users\franc\Desktop\Francisco\2ºano\Intro_ai\trabalho_final\trabalho_final\pygame_iia_trab_final\textures\garbage.jpg").convert_alpha()
_image_garbage = pygame.transform.scale(_image_garbage, (iconSize[0], iconSize[1]))

m = Matrix(windowHeight, windowWidth, iconSize)
m.fillIronMatrix(random.randrange(0,totalWidthAndHeight),random.randrange(0,totalWidthAndHeight))

totalSquares = totalWidthAndHeight * totalWidthAndHeight
garbagePercentage = int(0.3 * totalSquares)
m.spwanGarbageRandom(garbagePercentage)

isLeftClicked = False
isRightClicked = False
isUpClicked = False
isDownClicked = False
isEClicked = False
event_counter = 0
score = 0
no_garbage = 1
wall_collision = 5
grab_garbage = 10

while True:
    pygame.event.pump()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE] or event_counter >= 20:
        break

    tecla_selecionada, novo_estado = m.make_decision()  # Chame a função make_decision
    m.savetest_txt(m.xIron, m.yIron, tecla_selecionada)

    m.drawMatrix(boardGame, _image_iron_man, _image_garbage, iconSize)
    pygame.display.flip()