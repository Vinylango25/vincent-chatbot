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

## Part 3: Building the Knowledge Base from Vincent’s Profile

With the deployment infrastructure in place and the chatbot interface operational, the next critical step in the development process was to curate and integrate a knowledge base that the chatbot could reference to answer questions meaningfully. Since the primary objective of the chatbot was to answer questions related to *Vincent's professional profile*, the foundation of the chatbot’s knowledge had to be rooted in authentic content about my academic background, technical skills, experience, and achievements.

To achieve this, I began by preparing a document — a plain text file — containing detailed information about my career. This included descriptions of my roles as a data analyst, data scientist, and machine learning engineer, the tools and technologies I have mastered, notable projects I’ve worked on, academic qualifications, certifications, and other relevant professional highlights. The purpose of this content was to serve as the primary reference for the language model when generating responses to user queries.

Creating a solid knowledge base involved more than just gathering text. I needed to ensure the data was structured in a way that made it easy for a language model to reference and extract relevant context from. To facilitate this, I used techniques such as *text chunking* and *vector embedding*. Text chunking is the process of splitting large documents into smaller, semantically meaningful segments, which makes it easier for the model to retrieve only the relevant portions. For instance, information about skills, education, and work history were broken into discrete chunks so the retrieval system could quickly fetch only the parts related to a user’s question.

Once the document was prepared and divided into chunks, I used pre-trained embeddings to convert each chunk into a numerical vector that represents its semantic content. These vectors were then stored in a vector database, which could be queried at runtime to retrieve the most contextually relevant information. This architecture allowed the chatbot to simulate a contextual memory — accessing only the pieces of my profile that were pertinent to the question asked, instead of simply guessing from general knowledge.

A vital aspect of this process was selecting the right embedding model. I used a lightweight yet powerful sentence-transformer model that strikes a balance between performance and speed. This ensured that the chatbot could quickly retrieve relevant profile information without consuming too many compute resources. The embeddings created from the text chunks were indexed and stored in a persistent vector store so they could be re-used across sessions and even after server restarts.

This stage not only contributed to the chatbot's ability to provide factually grounded responses but also brought in key concepts from modern natural language processing workflows. It demonstrated the use of semantic search, vector databases, and embedding models — all of which are foundational to many real-world LLM applications today.

From a personal standpoint, this phase gave me hands-on experience in preparing domain-specific data for use with language models, a vital skill for anyone working with LLMs in production environments. It showed how context-aware AI systems can be tailored to specific use cases — such as answering personalized questions — by combining retrieval-based methods with generative capabilities.

By the end of this part of the project, I had successfully built a custom knowledge base tailored to my professional background, optimized it for retrieval, and connected it to the chatbot engine. This empowered the chatbot to provide rich, context-aware answers that were not only linguistically accurate but also factually grounded in real information about me — Vincent.

## Part 4: Developing the FastAPI Backend – The Chatbot Engine

This stage marked the core development of the backend system that powers the Vincent Chatbot. The objective was to build a robust, efficient, and scalable API that could receive user queries, search through relevant profile documents, and generate precise answers leveraging advanced large language models (LLMs). Here’s an overview of the critical components and work involved:

### Framework Selection and API Design
- **FastAPI** was selected as the backend framework due to its modern asynchronous capabilities, fast performance, and straightforward syntax for building RESTful APIs.
- A single POST endpoint `/chat` was implemented. This endpoint accepts a JSON payload containing the user’s query and returns the chatbot’s response.
- The API was designed to handle concurrency well, allowing multiple users to interact simultaneously without degradation in response times.

### Document Processing and Semantic Retrieval
- To enable the chatbot to ground its answers in Vincent’s actual profile data, I employed a semantic search approach rather than keyword matching.
- The document data (e.g., resume, portfolio text) was loaded and split into manageable chunks using `RecursiveCharacterTextSplitter`. This preserves context within the chunks and allows granular search.
- These chunks were embedded into vector representations using the `HuggingFaceEmbeddings` model (`all-MiniLM-L6-v2`), converting text into numerical vectors capturing semantic meaning.
- A **Chroma vector database** was created to store these embeddings. This database allows fast similarity searches, retrieving the top K chunks most relevant to the query.
- The vector retriever was integrated seamlessly into the API. For every query, it fetches relevant context chunks that inform the LLM’s generation.

### Custom LLM Integration and Prompt Engineering
- The chatbot uses OpenRouter’s API as the LLM backend, specifically the powerful `mistral-7b-instruct` model.
- I wrote a custom Python class `OpenRouterChat` to encapsulate API calls and adapt responses to the LangChain interface.
- Prompt engineering was a key focus: the retrieved document chunks are concatenated into a system message that instructs the LLM to respond based solely on this context.
- This approach ensures accurate, relevant answers and minimizes hallucinations or off-topic responses.
- The chatbot processes the conversation asynchronously, optimizing speed and user experience.

### Error Handling and Robustness
- Comprehensive try-except blocks were added to catch potential errors such as API failures or data retrieval issues.
- On error, the API returns informative JSON messages, improving debuggability and resilience.
- Logging and warning messages were used to monitor deprecations and potential future changes in LangChain dependencies.

### Skills and Knowledge Acquired
- Designing asynchronous backend APIs with FastAPI and Pydantic schemas.
- Using vector embeddings and similarity search to build retrieval-augmented generation systems.
- Deep understanding of prompt engineering techniques to control LLM outputs.
- Practical experience integrating third-party LLM APIs in a production setting.
- Debugging and writing maintainable, production-grade Python code.
- Managing dependencies and staying current with rapidly evolving NLP libraries.

This backend forms the critical "brain" of the Vincent Chatbot, combining document retrieval and advanced language modeling to deliver intelligent, contextually aware responses.

---

## Part 5: Deployment and Hosting on Render.com – Making the Chatbot Live

After developing the chatbot backend locally, the next significant step was to deploy the application so it could be accessed online by users anywhere. I chose Render.com for deployment, a modern cloud platform offering automated builds, continuous deployment, and easy environment management.

### Preparing the Project for Deployment
- A `.gitignore` file was created and configured carefully to exclude unnecessary files such as the entire `venv` directory (virtual environment), compiled Python bytecode (`__pycache__`), and environment variables files (`.env`).
- This kept the repository clean, reducing upload size and preventing secrets or bulky dependencies from being pushed to GitHub.
- The codebase was pushed to a GitHub repository, enabling integration with Render’s GitHub connector for automated deployments on every push.

### Managing Dependencies and Environment Variables
- All Python dependencies were listed in a `requirements.txt` file to allow Render to install the exact versions needed.
- Sensitive information like the `OPENROUTER_API_KEY` was never hardcoded; instead, it was securely injected via Render’s environment variable settings.
- This separation ensures security best practices and easy updates without changing source code.

### Configuring Render Web Service
- The backend was deployed as a **Web Service** on Render, suitable for dynamic API hosting.
- Since FastAPI listens on a port, I specified the correct port binding (`PORT` environment variable) in the startup command so Render could route traffic properly.
- Logs were monitored during deployment to troubleshoot startup issues such as port conflicts or missing dependencies.
- Warning messages about deprecated LangChain classes were noted for future upgrades.

### Testing and Validation
- Once deployed, the API was tested by sending HTTP requests to the public URL to verify proper functioning.
- Response times, accuracy, and error handling were validated against the local version.
- Basic frontend clients (e.g., Streamlit apps) were connected to the live backend to provide an interactive user interface.

### Lessons Learned and Skills Gained
- Cloud deployment workflows and integration with CI/CD pipelines.
- Best practices for environment and secret management in hosted environments.
- Handling Linux-based deployment environments when developing locally on macOS.
- Debugging deployment-specific issues such as network binding and dependency compatibility.
- Understanding platform-specific constraints like GitHub’s file size limits and Render’s port detection process.
- Gaining confidence in deploying AI-powered applications to production environments with scalability and reliability.

### Summary
Deploying the Vincent Chatbot backend to Render.com was a transformative step that turned the project from a local prototype into a fully accessible cloud service. This phase solidified practical DevOps and cloud skills critical for real-world AI product development. The experience also highlighted the importance of careful project organization, security considerations, and proactive monitoring to maintain uptime and performance in production.

---

This detailed documentation serves as a comprehensive record of the backend development and deployment process, showcasing proficiency in cutting-edge AI tools, backend engineering, and cloud infrastructure management.



