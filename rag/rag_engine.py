from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def load_docs():

    with open("rag/knowledge_base.txt","r") as f:
        docs = f.readlines()

    return docs


def build_index(docs):

    embeddings = model.encode(docs)

    dim = embeddings.shape[1]

    index = faiss.IndexFlatL2(dim)

    index.add(np.array(embeddings))

    return index, embeddings


def retrieve(query, docs, index):

    q_emb = model.encode([query])

    D,I = index.search(np.array(q_emb),3)

    results = [docs[i] for i in I[0]]

    return results