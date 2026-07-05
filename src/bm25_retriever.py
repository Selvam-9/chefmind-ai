from rank_bm25 import BM25Okapi

def create_bm25(documents):
    """
    Create BM25 index
    """

    tokenized_documents = [document.lower().split() for document in documents]
    bm25 = BM25Okapi(tokenized_documents)
    return bm25

def bm25_retrieve(query, bm25, documents, top_k=3):
    """
    Retrieve documents using BM25
    """
    query_tokens = query.lower().split()
    scores = bm25.get_scores(query_tokens)
    top_k_indices = scores.argsort()[-top_k:][::-1]
    retrieved_documents = [documents[idx] for idx in top_k_indices]
    return retrieved_documents
