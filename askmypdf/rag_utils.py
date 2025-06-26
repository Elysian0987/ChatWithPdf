import os
# import openai
import chromadb
from chromadb.config import Settings
# from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

# 🧠 Load local sentence-transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# 🗃️ Setup ChromaDB
client = chromadb.Client(Settings())
collection = client.get_or_create_collection(name="pdf_chunks")

# ⛔ Commented out - OpenAI dotenv + API key (not needed now)
# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

# 🧩 Split long text into overlapping chunks
def split_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

# ⛔ Commented out - OpenAI embedding version
# def get_embedding(text):
#     response = openai.embeddings.create(
#         input=text,
#         model="text-embedding-3-small"
#     )
#     return response.data[0].embedding

# ✅ ✅ Use sentence-transformer instead
def get_embedding(text):
    return model.encode(text).tolist()

# 🧠 Store chunk embeddings in ChromaDB
def add_chunks_to_chroma(chunks):
    for i, chunk in enumerate(chunks):
        embedding = get_embedding(chunk)
        collection.add(
            documents=[chunk],
            ids=[str(i)],
            embeddings=[embedding]
        )

# ⛔ Commented out - original OpenAI GPT query
# def query_gpt(query):
#     query_embedding = get_embedding(query)
#     results = collection.query(query_embeddings=[query_embedding], n_results=3)
#     top_chunks = results['documents'][0]
#     context = "\n\n".join(top_chunks)

#     prompt = f"""Use the following content to answer the question:\n\n{context}\n\nQuestion: {query}"""

#     response = openai.chat.completions.create(
#         model="gpt-4",
#         messages=[
#             {"role": "system", "content": "Answer only based on the provided context."},
#             {"role": "user", "content": prompt}
#         ]
#     )
#     return response.choices[0].message.content

# ✅ ✅ New: Local-only dummy GPT response
def query_gpt(query):
    query_embedding = get_embedding(query)
    results = collection.query(query_embeddings=[query_embedding], n_results=3)
    top_chunks = results['documents'][0]
    context = "\n\n".join(top_chunks)

    return f"🧠 (LocalBot): Based on your document, this might help:\n\n{context[:500]}..."
