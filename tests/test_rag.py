from rag.retriever import search_documents

query = "What are the user stories?"

results = search_documents(query)

for doc in results:

    print("\n====================\n")

    print(doc.page_content)




from rag.retriever import answer_query

question = "What are the functional requirements?"

answer = answer_query(question)

print(answer)