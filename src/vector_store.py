import faiss
from pathlib import Path

FAISS_PATH = Path('data/index.faiss')



def create_index(embeddings):
      dimension = embeddings.shape[1]
      index = faiss.IndexFlatL2(dimension)
      index.add(embeddings)
      return index

def save_index(index):
      faiss.write_index(index,str(FAISS_PATH))
      return index

def load_index():
      return faiss.read_index(str(FAISS_PATH))

def get_index(embeddings):
      if FAISS_PATH.exists():
            return load_index()
      index = create_index(embeddings)
      save_index(index)
      return index
