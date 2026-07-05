from src.embedding import create_embedding

def retrieve(query, index, documents, top_k=3):
    """
    Retrieve the most relevant documents for a given query.
    """

    # Step 1: Convert the user query into an embedding
    query_embedding = create_embedding(query)

    # Step 2: FAISS expects shape (number_of_queries, embedding_dimension)
    query_embedding = query_embedding.reshape(1, -1)

    # Step 3: Search the existing FAISS index
    distances, indices = index.search(query_embedding, top_k)

    # Step 4: Convert the returned indices into actual documents
    retrieved_documents = [documents[idx] for idx in indices[0]]

    print("=" * 50)
    print("Retrieved Documents")
    print("=" * 50)

    for doc in retrieved_documents:
        print(doc)
        print("-" * 30)

    return retrieved_documents