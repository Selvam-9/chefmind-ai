from src.data_loader import load_recipes
from src.preprocess import create_documents
from src.embedding_store import get_embeddings
from src.vector_store import get_index
from src.rag import ask
from src.bm25_retriever import create_bm25

# -------------------------------
# Initialize the RAG System
# -------------------------------

recipes = load_recipes()
documents = create_documents(recipes)
embeddings = get_embeddings(documents)
index = get_index(embeddings)
bm25 = create_bm25(documents)


print("=" * 50)
print("🍳 Welcome to ChefMind AI")
print("=" * 50)
print("Type 'exit' to quit.\n")


while True:

    query = input("👤 You: ")

    if query.lower() == "exit":
        print("\n👋 Thank you for using ChefMind AI!")
        break

    answer = ask(query, index, bm25, documents)

    print(f"\n🤖 ChefMind:\n{answer}\n")
    print("=" * 50)