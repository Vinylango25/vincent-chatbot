import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
import os
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

# 🔐 Set your OpenRouter API key
os.environ["OPENROUTER_API_KEY"] = "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"

# 📂 Load and merge text data from multiple sources
all_files = ["cv_text.txt", "github_data.txt", "portfolio_text.txt"]
all_text = ""

for file in all_files:
    with open(file, "r", encoding="utf-8") as f:
        all_text += f.read() + "\n\n"

with open("profile_data.txt", "w", encoding="utf-8") as f:
    f.write(all_text)

# 📄 Load combined profile data
loader = TextLoader("profile_data.txt", encoding="utf-8")
docs = loader.load()

# ✂️ Split long text into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
chunks = splitter.split_documents(docs)

# 🧠 Embed documents using Hugging Face model
embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# 🧷 Store embeddings in a vector store (Chroma)
vectordb = Chroma.from_documents(documents=chunks, embedding=embedding, persist_directory="db")
retriever = vectordb.as_retriever()

# 🤖 Define LLM using OpenRouter endpoint
llm = ChatOpenAI(
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key=os.environ["OPENROUTER_API_KEY"],
    model="mistralai/mistral-7b-instruct"
)

# 🔗 Combine retriever and LLM into a QA chain
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# 🧪 Launch terminal-based Q&A loop
print("\n🤖 Vincent Bot (OpenRouter) is ready. Ask me anything about Kipkemoi Vincent (type 'exit' to quit).\n")

while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        break
    result = qa_chain.run(query)
    print("Vincent Bot:", result)
