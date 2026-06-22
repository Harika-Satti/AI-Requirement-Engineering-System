from langchain_community.vectorstores import FAISS

from langchain_huggingface import HuggingFaceEmbeddings


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

from langchain_core.documents import Document


def save_project_documents(state):

    documents = [

        Document(
            page_content=state["analyzed_requirement"],
            metadata={"type": "analysis"}
        ),

        Document(
            page_content=state["ambiguities"],
            metadata={"type": "ambiguity"}
        ),

        Document(
            page_content=state["user_stories"],
            metadata={"type": "user_stories"}
        ),

        Document(
            page_content=state["use_cases"],
            metadata={"type": "use_cases"}
        ),

        Document(
            page_content=state["srs_document"],
            metadata={"type": "srs"}
        ),

        Document(
            page_content=state["review_report"],
            metadata={"type": "review"}
        )
    ]

    vector_db = FAISS.from_documents(
        documents,
        embeddings
    )

    vector_db.save_local("faiss_index")

    return "Documents Stored Successfully"