from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

texts = [
    "Food delivery app requirements",
    "E-commerce platform design",
    "Chat application with real-time messaging"
]

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

db = FAISS.from_texts(texts, embeddings)

os.makedirs("faiss_index", exist_ok=True)

db.save_local("faiss_index", index_name="index")

print("FAISS index created successfully")