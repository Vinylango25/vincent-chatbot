## 1. Project Overview: Building the Vincent Profile Chatbot

This project involved designing and developing a custom chatbot specifically trained to answer questions about my professional background, technical skills, and project experience. The goal was to create an intelligent, queryable assistant — "Vincent Bot" — capable of responding with relevant and contextually accurate information extracted from a curated profile document.

### Objective

The main objective was to demonstrate proficiency in deploying Large Language Models (LLMs) using modern AI development tools and frameworks. Rather than using general-purpose LLMs, I customized the chatbot with domain-specific knowledge — in this case, my own professional portfolio — and built a full-stack application capable of:

- Understanding and interpreting natural language queries.
- Retrieving relevant information from vectorized profile documents.
- Responding with concise, human-like answers via a deployed API.

This chatbot acts as both a technical proof-of-concept and a dynamic, interactive CV.

### What I Did

Below is a clear outline of the tasks I carried out:

1. **Prepared the Profile Data**:  
   - Created a `portfolio_text.txt` file containing structured and unstructured data about my career, skills, education, projects, tools, and technologies used.
   - Cleaned and formatted the text to ensure better chunking and context retention during retrieval.

2. **Document Embedding and Vector Storage**:
   - Used LangChain's `TextLoader` to load the profile text.
   - Applied `RecursiveCharacterTextSplitter` to break down the document into manageable chunks for semantic indexing.
   - Generated vector embeddings for the document chunks using HuggingFace’s `all-MiniLM-L6-v2` embedding model.
   - Stored the embeddings using ChromaDB (`Chroma.from_documents`), enabling efficient vector search for retrieval.

3. **Language Model Setup**:
   - Integrated a lightweight, instruction-tuned LLM via OpenRouter (`mistralai/mistral-7b-instruct`).
   - Built a custom wrapper (`OpenRouterChat`) that formats messages and sends API requests to OpenRouter’s endpoint, receiving well-structured responses.
   - Secured the OpenRouter API key using `.env` variables and `python-dotenv`.

4. **FastAPI Backend Implementation**:
   - Developed a `FastAPI` application with a `/chat` endpoint that:
     - Accepts POST requests with a user query.
     - Retrieves top-k relevant document chunks via semantic similarity.
     - Passes the context and query to the LLM.
     - Returns the generated response as JSON.
   - Encapsulated business logic (retrieval + generation) inside a single function for clarity and modularity.

5. **Local Testing**:
   - Used `curl` and Python clients to test interactions locally.
   - Verified that the chatbot could answer specific questions like:
     - “What programming languages does Vincent use?”
     - “Where did Vincent study?”
     - “List Vincent’s experience as a machine learning engineer.”

### Skills Demonstrated

- **LangChain**: Document loading, text splitting, embedding, and retrieval chain setup.
- **FastAPI**: REST API creation, input validation with Pydantic, and asynchronous execution.
- **Vector Databases**: Practical use of ChromaDB to store and search dense vector representations.
- **LLM Deployment**: Working with hosted models on OpenRouter and building a custom integration.
- **Secure API Development**: Managing environment variables and sensitive keys using `.env`.

---

This part of the project established the core AI logic and backend service needed for the chatbot to work. Next, I focused on developing a user interface and deploying both the backend and frontend services to production platforms.
