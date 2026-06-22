import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import os
import pickle

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

INDEX_PATH = "database/faiss_index.bin"
META_PATH = "database/faiss_metadata.pkl"


def save_to_faiss(project_name, text):

    embedding = model.encode([text])

    dimension = embedding.shape[1]

    if os.path.exists(INDEX_PATH):
        index = faiss.read_index(INDEX_PATH)

        with open(META_PATH, "rb") as f:
            metadata = pickle.load(f)

    else:
        index = faiss.IndexFlatL2(dimension)
        metadata = []

    index.add(
        np.array(embedding).astype("float32")
    )

    metadata.append(project_name)

    faiss.write_index(
        index,
        INDEX_PATH
    )

    with open(META_PATH, "wb") as f:
        pickle.dump(metadata, f)

    return True


# search function 

def search_faiss(query, k=3):
    import numpy as np

    if not os.path.exists(INDEX_PATH):
        return []

    index = faiss.read_index(INDEX_PATH)

    with open(META_PATH, "rb") as f:
        metadata = pickle.load(f)

    query_vec = model.encode([query]).astype("float32")

    distances, indices = index.search(query_vec, k)

    results = []

    for i in indices[0]:
        if i < len(metadata):
            results.append(metadata[i])

    return results