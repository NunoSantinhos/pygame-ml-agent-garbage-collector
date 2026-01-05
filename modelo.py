import pickle
from sklearn.feature_extraction.text import CountVectorizer

def load_model_and_vectorizer(model_filename='naive_bayes_model.pkl', vectorizer_filename='vectorizer.pkl'):
    # Carregamento do modelo Naive Bayes
    with open(model_filename, 'rb') as model_file:
        loaded_naive_bayes_model = pickle.load(model_file)

    # Carregamento do vetorizador
    with open(vectorizer_filename, 'rb') as vectorizer_file:
        loaded_vectorizer = pickle.load(vectorizer_file)

    return loaded_naive_bayes_model, loaded_vectorizer

def predict_action(new_data, model, vectorizer):
    # Preparação dos novos dados para previsão
    new_data_vectorized = vectorizer.transform(new_data)

    # Realização de previsões
    prediction = model.predict(new_data_vectorized)

    return prediction[0]
