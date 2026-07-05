import numpy as np
from pathlib import Path

from src.data_loader import load_recipes
from src.preprocess import create_documents
from src.embedding import create_embeddings


EMBADDED_PATH = Path('data/embeddings.npy')


def save_embeddings(embeddings):
    np.save(EMBADDED_PATH,embeddings)

def load_embeddings():
    return np.load(EMBADDED_PATH)

def get_embeddings(documents):
    if EMBADDED_PATH.exists():
        return load_embeddings()
    else:
        embeddings = create_embeddings(documents)
        save_embeddings(embeddings)
    return embeddings
 
