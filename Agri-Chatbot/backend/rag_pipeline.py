from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from model_loader import generate_with_ollama

VECTOR_DB_DIR = "../vector_db"

class AgriculturalRAG:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        self.vectorstore = Chroma(
            persist_directory=VECTOR_DB_DIR,
            embedding_function=self.embeddings
        )

    def retrieve_context(self, query: str, k: int = 4):
        results = self.vectorstore.similarity_search(query, k=k)
        return "\n\n".join([doc.page_content for doc in results])

    def build_prompt(self, user_query: str, context: str) -> str:
        return f"""
You are an expert agricultural advisory assistant.

Use the retrieved agricultural knowledge below to answer the user's question accurately.
If the answer is not directly available, provide a practical agriculture-based suggestion.
Keep the answer simple, clear, and farmer-friendly.
If possible, include prevention and best practices.
If the query appears in Tamil, respond in simple Tamil.

Retrieved Context:
{context}

User Question:
{user_query}

Answer:
"""

    def ask(self, query: str) -> str:
        context = self.retrieve_context(query)
        prompt = self.build_prompt(query, context)
        return generate_with_ollama(prompt)