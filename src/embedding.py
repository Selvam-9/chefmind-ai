from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def create_embedding(document):
    return model.encode(document)

def create_embeddings(documents):
    return model.encode(documents)