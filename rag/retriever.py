from langchain_community.vectorstores import FAISS

from langchain_huggingface import HuggingFaceEmbeddings

from langchain_groq import ChatGroq


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def load_vector_db():

    return FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )


def search_documents(query):

    db = load_vector_db()

    results = db.similarity_search(
        query,
        k=3
    )

    return results



llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0

)


def answer_query(query):

    docs = search_documents(query)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
    Answer the question using the context.

    Context:
    {context}

    Question:
    {query}
    """

    response = llm.invoke(prompt)

    return response.content