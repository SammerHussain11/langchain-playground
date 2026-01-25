from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import pipeline
import numpy as np

# -------------------------------
# Documents
# -------------------------------
documents = [
    "Quaid-e-Azam Muhammad Ali Jinnah was the founder of Pakistan.",
    "He was born on 25 December 1876 in Karachi.",
    "He studied law at Lincoln’s Inn in London.",
    "He became the first Governor-General of Pakistan.",
    "He believed in unity, faith, and discipline."
]

query = "Who is Quaid-e-Azam Muhammad Ali Jinnah?"

# -------------------------------
# Local Embeddings
# -------------------------------
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
doc_embeddings = embedding_model.encode(documents)
query_embedding = embedding_model.encode([query])

# -------------------------------
# Similarity Search
# -------------------------------
similarities = cosine_similarity(query_embedding, doc_embeddings)[0]
top_index = np.argmax(similarities)
context = documents[top_index]

print("Most relevant document:")
print(context)

# -------------------------------
# Lightweight LLM using HuggingFace (Free, CPU)
# -------------------------------
qa_pipeline = pipeline(
    "summarization",  # works well for short QA prompts
    model="sshleifer/distilbart-cnn-12-6",
    device=-1  # CPU
)

prompt = f"Context: {context}\nQuestion: {query}\nAnswer concisely:"

response = qa_pipeline(prompt, max_length=100, min_length=30, do_sample=False)[0]["summary_text"]

print("\nAnswer:")
print(response)
