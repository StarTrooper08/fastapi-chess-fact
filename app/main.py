from fastapi import FastAPI
import random

app = FastAPI()
chess_facts = [
    "The longest recorded game of chess took 20 hours and 15 minutes!",
    "The word 'checkmate' comes from the Persian phrase 'Shah Mat,' which means 'the King is helpless.'",
    "The number of possible ways of playing the first four moves per side in chess is 318,979,564,000.",
    "The queen used to only be able to move one square at a time, and it wasn't until the 15th century in Spain that the queen gained its current powerful abilities.",
    "The folding chess board was invented by a priest in 1125 who was forbidden to play chess.",
    "The longest confirmed unbeaten streak at an elite level belongs to Magnus Carlsen, who achieved an unbeaten streak of 125 games in the classical time format.",
]


@app.get("/")
def get_chess_fact():
    """Returns a random interesting fact about chess."""
    random_fact = random.choice(chess_facts)
    return {"chess_fact": random_fact}