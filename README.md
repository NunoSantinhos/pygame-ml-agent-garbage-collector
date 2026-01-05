# Pygame ML Agent — Garbage Collector (Grid World)

Grid-based game built with **Pygame** where an agent navigates a 2D board to collect garbage while avoiding walls/invalid moves.
The agent’s actions are predicted using a simple **Machine Learning** model (Naive Bayes) trained from gameplay data.

## Context
Academic project developed for the course **Introduction to Artificial Intelligence**.

## Features
- Grid-world environment (2D matrix)
- Pygame-based visual interface
- Data collection for training (state → action)
- Supervised ML model to predict the next action (e.g., left/right/up/down/grab)

## Tech Stack
- Python
- Pygame
- NumPy / Pandas
- scikit-learn (Naive Bayes)
- joblib / pickle (model persistence)

## Project Structure
- `run.py` / `run2.py` — game loop and interface
- `scripts/Matrix.py` — grid logic + decision-making
- `train2.py` — model training script
- `modelo.py` — load model/vectorizer + prediction helper
- `textures/` — sprites/assets (if included)

## How to Run
```bash
pip install -r requirements.txt
python run.py
