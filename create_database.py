from langchain_community.document_loaders import DirectoryLoader
# Used to load documents from a specified directory
from langchain.text_splitter import RecursiveCharacterTextSplitter
# RecursiveCharacterTextSplitter: Splits text documents into smaller chunks based on character count.
from langchain.schema import Document
# Imports the Document class, which is used to represent text documents in the LangChain library
from langchain_openai import OpenAIEmbeddings
# Provides embeddings for text using OpenAI’s models
from langchain_community.vectorstores import Chroma
# A vector store that stores an retrieves documents based on embeddings
import openai 
# OpenAI Python client library for making API calls to OpenAI’s services
import os
# For interacting with the operating system (e.g., file path operations)
import shutil
# Shutil provides high-level file operations (e.g., removing directories)

openai.api_key = 'sk-xxxxxxxxxx'

CHROMA_PATH = "chroma" # the directory where the Chroma vector store will be persisted

DATA_PATH = "data/books" # the directory containing the documents to be loaded and processed

def main(): # entry point of the script
    generate_data_store()

# Load, split data into chunks and then save the chunks to a chroma vector store
def generate_data_store():
    # Check if the database directory exists
    if os.path.exists(CHROMA_PATH):  # <-- Added this block to check and remove the existing database
        print(f"Database exists at {CHROMA_PATH}, recreating it...")
        shutil.rmtree(CHROMA_PATH)  # <-- Removes the existing Chroma directory

    documents = load_documents()  
    chunks = split_text(documents)  
    save_to_chroma(chunks)  

# Intialise a DirectoryLoader to load .md (Markdown) files from the DATA_PATH directory. Returns a list of Document objects.
def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob="*.md")
    documents = loader.load()
    return documents

def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,  # Maximum size of each chunk (in characters)
        chunk_overlap=100, # Number of overlapping characters between chunks 
        # Overlap ensures that important information near the boundaries of chunks isn't lost
        length_function=len,
        add_start_index=True, # Includes an index at the start of each chunk
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.") # Print the number of documents and chunks created.

    return chunks

# Chroma.from_documents used to create a new vector store from the chunks
# OpenAIEmbeddings for generating embeddings
def save_to_chroma(chunks: list[Document]):

    db = Chroma.from_documents(
        chunks, OpenAIEmbeddings(openai_api_key=openai.api_key), persist_directory=CHROMA_PATH, collection_name='v_db'
    ) # Text-embedding-ada-002-v2 is the default embeddings model
    db.persist() # In the context of databases or data storage, "persisted" refers to the process of saving data 
# in a way that it remains available even after the program or system that created it has stopped 
# running
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")

if __name__ == "__main__":

    main()
