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

_image_iron_man = pygame.image.load(r"C:\Users\nmate\Desktop\LCiD\2º Ano\1º Semestre\Introdução à Inteligência Artificial\trabalho_final\pygame_iia_trab_final\textures\iron-man.png").convert_alpha()
_image_iron_man = pygame.transform.scale(_image_iron_man, (iconSize[0], iconSize[1]))

_image_garbage = pygame.image.load(r"C:\Users\nmate\Desktop\LCiD\2º Ano\1º Semestre\Introdução à Inteligência Artificial\trabalho_final\pygame_iia_trab_final\textures\garbage.jpg").convert_alpha()
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

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            event_counter += 1

            if event.key == pygame.K_LEFT and isLeftClicked == False:
                tecla_selecionada = 'left'
                if m.xIron > 0:
                    m.futurevalue = m.matrix[m.yIron, m.xIron - 1]
                    m.matrix[m.yIron, m.xIron] = m.lastvalue_temp
                    m.fillIronMatrix(m.yIron, m.xIron - 1)
                else:
                    score -= wall_collision
                isLeftClicked = True
            if event.key == pygame.K_RIGHT and isRightClicked == False:
                tecla_selecionada = 'right'
                if m.xIron < totalWidthAndHeight - 1:
                    m.futurevalue = m.matrix[m.yIron, m.xIron + 1]
                    m.matrix[m.yIron, m.xIron] = m.lastvalue_temp
                    m.fillIronMatrix(m.yIron, m.xIron + 1)
                else:
                    score -= wall_collision
                isRightClicked = True
            if event.key == pygame.K_UP and isUpClicked == False:
                tecla_selecionada = 'up'
                if m.yIron > 0:
                    m.futurevalue = m.matrix[m.yIron - 1, m.xIron]
                    m.matrix[m.yIron, m.xIron] = m.lastvalue_temp
                    m.fillIronMatrix(m.yIron - 1, m.xIron)
                else:
                    score -= wall_collision
                isUpClicked = True
            if event.key == pygame.K_DOWN and isDownClicked == False:
                tecla_selecionada = 'down'
                if m.yIron < totalWidthAndHeight - 1:
                    m.futurevalue = m.matrix[m.yIron + 1, m.xIron]
                    m.matrix[m.yIron, m.xIron] = m.lastvalue_temp
                    m.fillIronMatrix(m.yIron + 1, m.xIron)
                else:
                    score -= wall_collision
                isDownClicked = True

            m.lastvalue_temp = m.futurevalue

            if event.key == pygame.K_e and isEClicked == False:
                tecla_selecionada = 'e'
                if m.lastvalue_temp == 'empty':
                    score -= no_garbage
                elif m.lastvalue_temp == 'garbage':
                    m.matrix[m.yIron, m.xIron] = 'iron'
                    score += grab_garbage

                isEClicked = True

            if event.key == pygame.K_e and isEClicked == True:
                tecla_selecionada = 'e'
                isEClicked = False
                if m.lastvalue_temp == 'garbage':
                    m.lastvalue_temp = 'empty'

            m.guardar_txt(m.xIron, m.yIron, tecla_selecionada)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and isLeftClicked == True:
                isLeftClicked = False
            if event.key == pygame.K_RIGHT and isRightClicked == True:
                isRightClicked = False
            if event.key == pygame.K_UP and isUpClicked == True:
                isUpClicked = False
            if event.key == pygame.K_DOWN and isDownClicked == True:
                isDownClicked = False
            if event.key == pygame.K_e and isEClicked == True:
                isEClicked = False

    m.drawMatrix(boardGame, _image_iron_man, _image_garbage, iconSize)
    pygame.display.flip()

#f = open("treino.txt", "a")
#f.write(str(score) + "\n")
#f.close()
