from openpyxl.packaging import manifest
from src.retriever import retrieve
from src.prompt import build_prompt
from llm.gemini import generate_answer

def aks(quary,index,documents):
    retrieved_documents = retrieve(quary,index,documents)
    prompt = build_prompt(quary,retrieved_documents)
    answer = generate_answer(prompt)
    return answer
