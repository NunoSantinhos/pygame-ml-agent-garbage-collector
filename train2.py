import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import joblib

# Leitura dos dados do arquivo txt
data = []
with open("treino.txt", 'r') as file:
    for line in file:
        data.append(line.strip().split(','))


# Criação de um DataFrame pandas
columns = ['A', 'B', 'C', 'D', 'E', 'Target']
df = pd.DataFrame(data, columns=columns)
print('\n\n\n dataframe \n')
print(df)

# Mapeamento de strings para números usando LabelEncoder para a coluna alvo
label_encoder = LabelEncoder()
df['Target'] = label_encoder.fit_transform(df['Target'])
print('\n\n\n LabelEncoder \n')
print(df)

# Aplicação da codificação one-hot nas variáveis categóricas
df = pd.get_dummies(df, columns=['A', 'B', 'C', 'D', 'E'])
print('\n\n\n get_dummies \n')
print(df)

# Divisão dos dados em recursos (X) e rótulos (y)
X = df.drop('Target', axis=1)
y = df['Target'].astype(int)
print('\n\n\n Divisão dos dados em recursos X \n')
print(X)
print('\n\n\n Divisão dos dados em rotulos y \n')
print(y)


# Treinamento do modelo Naive Bayes
model = MultinomialNB()
model.fit(X, y)

# Previsões no conjunto de dados completo
predictions = model.predict(X)
print('\n\n\n predictions \n')
print(predictions)


# Avaliação do modelo
accuracy = accuracy_score(y, predictions)
print('\n\n\n')
print(f'Acurácia do modelo: {accuracy:.2f}')

# Relatório de classificação
print('\n\n\n Relatório de classificação \n')
print(classification_report(y, predictions, target_names=label_encoder.classes_))


joblib.dump(model, 'modelo_treinado.joblib')