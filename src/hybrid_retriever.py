from src.retriever import retrieve
from src.bm25_retriever import bm25_retrieve


def hybrid_retrieve(query, index, bm25, documents, top_k=3):

    faiss_results = retrieve(query, index, documents, top_k)

    bm25_results = bm25_retrieve(query, bm25, documents, top_k)

    merged_results = []

    for doc in faiss_results:
        if doc not in merged_results:
            merged_results.append(doc)

    for doc in bm25_results:
        if doc not in merged_results:
            merged_results.append(doc)

    return merged_results[:top_k]