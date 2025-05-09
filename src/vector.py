from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os 
import pandas as pd

# Loading the dataset/dataframe
df = pd.read_csv('data/realistic_restaurant_reviews.csv')
# define the embeddings model 
embeddings = OllamaEmbeddings(model = 'mxbai-embed-large')

# location where we want to save our vector database 
db_location = "./chrome_langchain_db"

"""check if the above database already exists and if yes then we have already performed the process of
   converting the csv file into vectors and adding it to the database and if it dosen't exist then it 
   means we need to do that  """ 

add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []

    for i, row in df.iterrows():
        document = Document(
            # what will be actually vectorising and what we'll be actually looking up - basically any content you want to use to look up the information in the database - that needs  to be here in the page content 
            page_content= row["Title"] + " " + row["Review"],
            # metadata is the additional information that we will grab along with the docuement but wont be querying with it  
            metadata = {"rating": row["Rating"], "date": row["Date"]},
            id = str(i)
        )
        ids.append(str(i))
        documents.append(document)

vector_store = Chroma(
    collection_name="restaurant_reviews", 
    persist_directory=db_location, # to store the data persistently 
    embedding_function=embeddings
)

if add_documents:
    vector_store.add_documents(documents=documents, ids = ids)


# now to connect the model to the vector store database
retriever = vector_store.as_retriever(
    # no. of documents we want to look up 
    search_kwargs = {"k": 5} # it will pick up 5 relevant reviews and pass them to the LLM
)
