                     final_recipes.json
                            │
                            ▼
                  data_loader.py
                  load_recipes()
                            │
                            ▼
         List[Recipe Dictionary] (1016 recipes)
                            │
                            ▼
                   preprocess.py
              create_document(recipe)
                            │
                            ▼
                One Document (string)
                            │
                            ▼
              create_documents(recipes)
                            │
                            ▼
               List[Document String]
                            │
                            ▼
                  embedding.py
           create_embedding(document)
                            │
                            ▼
            NumPy Array (384 dimensions)


Complete pipeline 
Recipe JSON
      │
      ▼
Data Cleaning
      │
      ▼
Document + Metadata
      │
      ▼
Embedding Model
      │
      ▼
Embedding Vectors
      │
      ▼
FAISS Index
══════════════════════════════
      User asks question
══════════════════════════════
      │
      ▼
Question → Embedding
      │
      ▼
FAISS Search
      │
      ▼
Top K Recipes
      │
      ▼
Prompt Builder
      │
      ▼
LLM
      │
      ▼
Final Answer


✅ Load Data
✅ Preprocess
✅ Create Documents
✅ Generate Embeddings

⬜ Build FAISS Index      ← Next
⬜ Save Index
⬜ Load Index
⬜ Retrieval
⬜ Prompt Builder
⬜ LLM Integration
⬜ Streamlit UI
⬜ Hybrid Search
⬜ Evaluation


1. Load recipes from JSON

↓

2. Convert each recipe into a document

↓

3. Convert documents into embeddings

↓

4. Store embeddings in FAISS

↓

5. Convert the user's query into an embedding

↓

6. Retrieve the most similar recipes

↓

7. Build a prompt with the retrieved recipes

↓

8. Send the prompt to Gemini

↓

9. Return the answer