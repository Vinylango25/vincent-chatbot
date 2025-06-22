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

## Part 2: Deploying the Chatbot and Building a User Interface

After developing the backend logic and successfully testing it locally, the next major milestone in this project was to make the chatbot publicly accessible through a user-friendly interface and deploy it to a cloud platform. This process involved two key components: first, integrating a lightweight web interface for user interaction; second, deploying the application online so it could be accessed by anyone without requiring any development tools or local environments.

To begin with, I designed a simple yet effective user interface using **Streamlit**, a Python-based framework well-suited for building data and AI web apps. The goal was to create an interface where users could ask questions about my profile and receive intelligent responses from the chatbot, powered by the LLM in the backend. Streamlit was selected for its rapid prototyping capabilities, ease of use, and tight integration with Python, which made it ideal for deploying machine learning and language model applications without the complexity of front-end development tools.

The user interface consisted of a clean layout with a text input box for queries, a button to submit the question, and a section to display the chatbot's response. I also handled edge cases, such as when users submitted empty input or encountered a failed API request. This part of the project emphasized usability — ensuring that anyone interacting with the chatbot would have a seamless and intuitive experience.

Once the UI was built and connected to the backend locally, I proceeded to deploy the full application stack. For this, I chose **Render**, a modern cloud platform for deploying web services. I set up a GitHub repository to manage the project source code and configured Render to deploy the application directly from the repo. The FastAPI backend was configured to expose a `/chat` endpoint, which Streamlit accessed via HTTP requests. I ensured the backend ran on an open port and was correctly bound to `0.0.0.0`, as required by Render’s hosting infrastructure.

A crucial step in the deployment process was managing environment variables and API keys securely. Instead of hardcoding sensitive credentials, I stored them in a `.env` file locally and later defined them as secret environment variables within the Render dashboard. This kept the deployment secure while ensuring that the language model could still authenticate and respond to requests.

I also faced challenges related to version control and repository management. Since the project involved a Python virtual environment and several large library files, I created a `.gitignore` file to exclude unnecessary folders such as `venv/`, cached files, and environment configurations. This helped maintain a clean and efficient repository, which is vital for collaboration and smooth deployment. I encountered a few push errors due to large files being accidentally committed — a learning moment that reinforced the importance of repository hygiene and size limitations on platforms like GitHub.

Through this deployment phase, I demonstrated my ability to connect machine learning services to real-world applications by combining backend logic, API communication, frontend user experience, and cloud hosting. This showcased my full-stack competence, especially in deploying language model applications for end-users. The chatbot was now available online — capable of intelligently answering profile-related questions, responding in real-time, and demonstrating the power of LLMs in a personal context.

This stage further highlighted essential software engineering practices such as continuous deployment, API design, user interface integration, and environment configuration. With the chatbot successfully deployed and operational, I had transformed a local prototype into a polished, shareable application that could be used as both a personal assistant and a public-facing demonstration of my AI capabilities.

