import os
import pandas as pd
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

DATA_DIR = "../data"
VECTOR_DB_DIR = "../vector_db"

def read_txt_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def read_pdf_file(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"
    return text

def read_csv_file(path):
    df = pd.read_csv(path)
    rows = []
    for _, row in df.iterrows():
        content = (
            f"Crop: {row.get('crop_name', '')}\n"
            f"Soil: {row.get('soil_type', '')}\n"
            f"Fertilizer: {row.get('fertilizer_recommendation', '')}\n"
            f"Irrigation: {row.get('irrigation_method', '')}\n"
            f"Pest Control: {row.get('pest_control_methods', '')}\n"
            f"Harvest Time: {row.get('harvest_time', '')}\n"
            f"Question: {row.get('question', '')}\n"
            f"Answer: {row.get('answer', '')}\n"
        )
        rows.append(content)
    return "\n".join(rows)

def load_documents():
    all_docs = []

    for file_name in os.listdir(DATA_DIR):
        path = os.path.join(DATA_DIR, file_name)

        if file_name.endswith(".txt"):
            all_docs.append(read_txt_file(path))
        elif file_name.endswith(".pdf"):
            all_docs.append(read_pdf_file(path))
        elif file_name.endswith(".csv"):
            all_docs.append(read_csv_file(path))

    return all_docs

def ingest():
    docs = load_documents()
    combined_text = "\n".join(docs)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    chunks = splitter.split_text(combined_text)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    vectorstore = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        persist_directory=VECTOR_DB_DIR
    )
    vectorstore.persist()

    print(f"Ingestion complete. Stored {len(chunks)} chunks in {VECTOR_DB_DIR}")

if __name__ == "__main__":
    ingest()