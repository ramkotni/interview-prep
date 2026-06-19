from rag.retriever import retriever

def search_agent(state):

    query = state["question"]

    docs = retriever.invoke(query)

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    state["context"] = context

    return state