# case_memory/vectorize_knowledge.py

from llama_index import VectorStoreIndex, download_loader
import os

PERSIST_DIR = "./case_memory/index"
SOURCE_DIR = "./case_memory/knowledge"

# Load text-based documents
SimpleDirectoryReader = download_loader("SimpleDirectoryReader")
reader = SimpleDirectoryReader(input_dir=SOURCE_DIR)
docs_txt = reader.load_data()

# Load PDF files using PyMuPDFReader
docs_pdf = []
PyMuPDFReader = download_loader("PyMuPDFReader")

for file in os.listdir(SOURCE_DIR):
    if file.lower().endswith(".pdf"):
        pdf_path = os.path.join(SOURCE_DIR, file)
        pdf_docs = PyMuPDFReader().load(file_path=pdf_path)
        docs_pdf.extend(pdf_docs)

# Combine and index
all_docs = docs_txt + docs_pdf
index = VectorStoreIndex.from_documents(all_docs)
index.storage_context.persist(persist_dir=PERSIST_DIR)

print("✅ CASE memory index built successfully.")
