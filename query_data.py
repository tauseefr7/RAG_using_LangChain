import argparse
from langchain_community.vectorstores import Chroma #
from langchain_openai import OpenAIEmbeddings, ChatOpenAI #
from langchain.prompts import ChatPromptTemplate
import openai

CHROMA_PATH = "chroma" 

# Defining the prompt template
PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

openai.api_key = 'sk-xxxxxxxxxx'

def main():
    # Set up argument parser to accept a query string from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text
    #print(f"Query Text: {query_text}")

    # Initialise the Chroma vector store with OpenAI embeddings
    embedding_function = OpenAIEmbeddings(openai_api_key=openai.api_key)
    db = Chroma(collection_name='v_db',persist_directory=CHROMA_PATH, embedding_function=embedding_function)
    print("Database initialised.")

   # Perform a similarity search in the database to find the top 3 most relevant chunks
    results = db.similarity_search_with_relevance_scores(query_text, k=3)
    print(f"Search Results: {results}")

    # Check if any relevant results were found and if their relevance score is above a threshold     
    if len(results) == 0 or results[0][1] < 0.7:
        print("Unable to find matching results.")
        print(f"Results length: {len(results)}")
        if len(results) > 0:
            print(f"Top result relevance score: {results[0][1]}")
        return

    # Generate a prompt using the context from the search results and the user's query
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    print("Generated Prompt:")
    print(prompt)

    # Use the language model to predict a response based on the generated prompt
    model = ChatOpenAI(openai_api_key=openai.api_key)
    response_text = model.invoke(prompt)

    # Collect sources used to answer the prompt and then print the response and sources
    sources = [doc.metadata.get("source", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    print(formatted_response)

if __name__ == "__main__":
    print("Running script directly")
    main() # Execute the main function if the script is run directly
