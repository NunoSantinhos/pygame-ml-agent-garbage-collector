import pygame
import numpy as np
import random
import pandas as pd
import joblib

class Matrix(object):

    def __init__(self, height, width, iconSize):
        self._height = height
        self._width = width
        self._iconSize = iconSize
        self._matrixRows = self._height // iconSize[0]
        self._matrixCols = self._width // iconSize[1]
        self.matrix = np.ndarray((self._matrixRows, self._matrixCols), dtype=object)
        self.matrix[:, :] = 'empty'
        self.yIron = None
        self.xIron = None
        self.lastvalue_temp = None

    def fillEmptyMatrix(self, y, x):

        self.matrix[y, x] = 'empty'

    def fillIronMatrix(self, y, x):
        self.matrix[y, x] = 'iron'
        self.yIron = y
        self.xIron = x

    def spwanGarbageRandom(self, numberOfTimes):

        for _ in range(numberOfTimes):
            while True:
                x = random.randrange(0, self._matrixCols, 1)
                y = random.randrange(0, self._matrixRows, 1)

                if self.matrix[y, x] != 'empty':
                    continue
                else:
                    # print(f'Appel->{[self.y, self.x]}')
                    # print(f'Snake->{tmp}')
                    self.matrix[y, x] = 'garbage'
                    break

    def drawMatrix(self, surface, _image_iron_man, _image_garbage, iconSize):

        surface.fill((255, 255, 255))

        for y in range(self._matrixRows):
            for x in range(self._matrixCols):
                if self.matrix[y, x] == 'iron':
                    surface.blit(_image_iron_man, (x * iconSize[1], y * iconSize[0]), (0, 0, iconSize[1], iconSize[0]))
                elif self.matrix[y, x] == 'garbage':
                    surface.blit(_image_garbage, (x * iconSize[1], y * iconSize[0]), (0, 0, iconSize[1], iconSize[0]))

        for y in range(0, self._height, self._iconSize[0]):
            pygame.draw.line(surface, (0, 0, 0), (0, y), (self._width - 1, y), 2)

        for x in range(0, self._width, self._iconSize[1]):
            pygame.draw.line(surface, (0, 0, 0), (x, 0), (x, self._height - 1), 2)
    pass

    def guardar_txt(self, xIron, yIron, evento):
        f = open("treino.txt", "a")
        f.write(str(self.matrix[yIron, xIron]) + ",")


        if yIron + 1 < len(self.matrix):
            if str(self.matrix[yIron + 1, xIron]) == 'None':
                f.write('empty,')
            else:
                f.write(str(self.matrix[yIron + 1, xIron]) + ",")
        else:
            f.write("wall,") #baixo

        if yIron - 1 >= 0:
            if str(self.matrix[yIron - 1, xIron]) == 'None':
                f.write('empty,')
            else:
                f.write(str(self.matrix[yIron - 1, xIron]) + ",")
        else:
            f.write("wall,") #cima
            

        if xIron + 1 < len(self.matrix[0]):
            if str(self.matrix[yIron, xIron + 1]) == 'None':
                f.write('empty,')
            else:
                f.write(str(self.matrix[yIron, xIron + 1]) + ",")
        else:
            f.write("Wall,") #dir


        if xIron - 1 >= 0:
            if str(self.matrix[yIron, xIron - 1]) == 'None':
                f.write('empty,')
            else:
                f.write(str(self.matrix[yIron, xIron - 1]) + ",")
        else:
            f.write("Wall,") #esq
            
        f.write(str(evento) + "\n")
        f.close()


    def savetest_txt(self, xIron, yIron, evento):
        f = open("treino.txt", "a")
        f.write(str(self.matrix[yIron, xIron]) + ",")
        f.write(str(self.matrix[yIron + 1, xIron]) + ",") if yIron + 1 < len(self.matrix) else f.write("Wall,") #baixo
        f.write(str(self.matrix[yIron - 1, xIron]) + ",") if yIron - 1 >= 0 else f.write("Wall,") #cima
        f.write(str(self.matrix[yIron, xIron + 1]) + ",") if xIron + 1 < len(self.matrix[0]) else f.write("Wall,") #dir
        f.write(str(self.matrix[yIron, xIron - 1]) + ",") if xIron - 1 >= 0 else f.write("Wall,") #esq
        f.write(str(evento) + "\n")
        f.close()


    def make_decision(self):
        # Extrai as características do estado atual para passar para o modelo
        features = [self.matrix[self.yIron, self.xIron],
                    self.matrix[self.yIron + 1, self.xIron] if self.yIron + 1 < len(self.matrix) else 'Wall',
                    self.matrix[self.yIron - 1, self.xIron] if self.yIron - 1 >= 0 else 'Wall',
                    self.matrix[self.yIron, self.xIron + 1] if self.xIron + 1 < len(self.matrix[0]) else 'Wall',
                    self.matrix[self.yIron, self.xIron - 1] if self.xIron - 1 >= 0 else 'Wall']

        # Crie um DataFrame de referência para as colunas dummy
        dummy_reference = pd.DataFrame(np.zeros((1, len(features))), columns=range(len(features)))

        # Crie um DataFrame com as colunas dummy
        features_df = pd.DataFrame([features])


        # Atualize o valor correspondente a cada feature
        for idx, value in enumerate(features):
            dummy_reference.iloc[0, idx] = 1
            features_df.rename(columns={idx: value}, inplace=True)

        # Faz a previsão usando o modelo
        prediction = model.predict(features_df)[0]


        # Mapeia a previsão de volta para uma ação
        if prediction == 0:
            action = 'left'
        elif prediction == 1:
            action = 'right'
        elif prediction == 2:
            action = 'up'
        elif prediction == 3:
            action = 'down'
        elif prediction == 4:
            action = 'e'

        # Adicione as colunas ausentes no DataFrame
        directions = ['A', 'B', 'C', 'D', 'E']  # Adicione todas as direções ao redor do personagem
        columns_to_add = [f"{direction}_{element}" for direction in directions for element in
                          ['Wall', 'empty', 'garbage', 'iron']]

        for col in columns_to_add:
            features_df[col] = 0

        training_columns = [0,1,2,3,4]
        feature_columns = [f"{direction}_{element}" for direction in directions for element in ['iron', 'Wall', 'empty', 'garbage']]
        training_columns += feature_columns
        features_df = features_df[training_columns]


        # Atualiza o estado futuro
        new_state = self.matrix.copy()
        # Faça as atualizações necessárias no novo estado com base na ação tomada

        return action, new_state

model = joblib.load(r'C:\Users\nmate\Desktop\LCiD\2º Ano\1º Semestre\Introdução à Inteligência Artificial\trabalho_final\modelo_treinado.joblib')