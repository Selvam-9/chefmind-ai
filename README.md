                User Query
                     │
                     ▼
          Sentence Transformer
                     │
                     ▼
         ┌─────────────────────┐
         │ Hybrid Retriever    │
         │                     │
         │  FAISS + BM25       │
         └─────────────────────┘
                     │
                     ▼
             Retrieved Recipes
                     │
                     ▼
             Prompt Builder
                     │
                     ▼
          Google Gemini 2.5 Flash
                     │
                     ▼
               Final Response