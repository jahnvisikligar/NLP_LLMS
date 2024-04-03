#Chat with PDF
#installing necessary libraries by uncommenting the below line
#!pip install langchain-community pypdf -U langchain-openai faiss-cpu --upgrade langchain python-dotenv

"""Code and data references: 
   https://python.langchain.com/docs/get_started/introduction 
   https://medium.com/getpieces/how-to-build-a-langchain-pdf-chatbot-b407fcd750b9
   https://github.com/sophiamyang/tutorials-LangChain/blob/main/LangChain_QA.ipynb
"""

"""Working with Code"""

#compilation of all libraries
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
import langchain

langchain.debug=True

loader=PyPDFLoader("input_your.pdf")
pages=loader.load_and_split(RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=100,length_function=len,is_separator_regex=False))

"""to check the splitting and length of the documents, uncomment the below lines."""
#for i in range(0,5):print(i,'Pages response:\n',pages[i])
#print("Total length of pages:",len(pages))

#implementing prompt template for better understanding
#Build prompt
template = """Use the following pieces of context to answer the question at the end.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Use three sentences maximum. Keep the answer as concise as possible.
Must answer in English language only.
Always say "thanks for asking!" at the end of the answer.
{context}
Question: {question}
Helpful Answer:"""
QA_CHAIN_PROMPT=PromptTemplate(input_variables=["context","question"],template=template)

#working with embeddings and vectorstore
#performing embedding to store text in a vectorstore
#Download embeddings from OpenAI
embeddings=OpenAIEmbeddings(openai_api_key="YOUR_API_KEY")
db=FAISS.from_documents(pages, embeddings)

# expose this index in a retriever interface
#k=value return the top 2 most similar chunks
# create a chain to answer questions
qa=ConversationalRetrievalChain.from_llm(ChatOpenAI(model_name="gpt-3.5-turbo-0613",temperature=0,openai_api_key="YOUR_API_KEY"),
                                         retriever=FAISS.from_documents(pages, OpenAIEmbeddings(openai_api_key="YOUR_API_KEY")).as_retriever(search_type="similarity",search_kwargs={"k":2}),
                                         memory=ConversationBufferMemory(k=5,memory_key="chat_history",return_messages=True),
                                         combine_docs_chain_kwargs={"prompt":QA_CHAIN_PROMPT},verbose=True)

chat_history=[]
query="How to measure quality of AI projects?"
result=qa({"question":query,"chat_history":chat_history})
result["answer"]
