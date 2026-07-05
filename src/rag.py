from src.hybrid_retriever import hybrid_retrieve
from src.prompt import build_prompt
from llm.gemini import generate_answer

def ask(query, index, bm25, documents):
    """
    Complete RAG Pipeline
    """

    retrieved_documents = hybrid_retrieve(query,index,bm25,documents,top_k=3)

    prompt = build_prompt(query, retrieved_documents)

    answer = generate_answer(prompt)

    return answer, retrieved_documents
