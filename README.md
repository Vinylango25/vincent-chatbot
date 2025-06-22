# Vincent Chatbot: Personalized Profile Assistant

## 1. Introduction & Purpose

### Overview

The Vincent Chatbot project represents a significant milestone in my journey into the world of artificial intelligence and natural language processing. This chatbot is designed to interactively answer questions specifically related to my personal professional profile, providing an intuitive and engaging experience for users interested in understanding my background, skills, and accomplishments.

This project serves not only as a showcase of my expertise but also as a practical application of Large Language Models (LLMs) and vector-based semantic search technologies to deliver accurate, context-aware responses from a custom knowledge base.

### Background and Motivation

In today’s digital landscape, interactive AI assistants have become powerful tools for enhancing user experience. They serve as accessible gateways to information, making complex data easy to retrieve through simple conversational interfaces. Inspired by this, I sought to build a chatbot tailored exclusively to represent my profile, allowing potential collaborators, employers, or clients to explore my capabilities and career highlights in an innovative manner.

The motivation behind this project can be summarized as follows:

1. **Demonstrate proficiency with LLMs and AI technologies:** By building a chatbot that understands and responds to detailed profile data, I aim to prove my ability to work with advanced language models and modern AI frameworks.
   
2. **Create a unique portfolio piece:** Instead of a static CV or traditional portfolio, this chatbot offers a dynamic way to present information, making my profile more memorable and interactive.
   
3. **Explore knowledge retrieval from custom documents:** The chatbot leverages vector databases and semantic search, demonstrating an understanding of how to convert unstructured text into meaningful queryable knowledge.
   
4. **Deploy a fully functional application:** The project encompasses end-to-end development—from data preprocessing, embedding generation, model interaction, to deployment on scalable platforms.

### What Makes This Chatbot Unique

Unlike generic chatbots designed for broad purposes, the Vincent Chatbot is a **domain-specific assistant**. It is trained not by re-training a full language model, but by using embeddings and vector stores to retrieve relevant context from a curated document base that contains information about my education, skills, work experience, and projects.

This approach ensures that answers are accurate, relevant, and directly tied to my professional narrative, avoiding the pitfalls of hallucination or misinformation common in general LLMs.

### Technical Context

At the core of the chatbot’s intelligence is the use of:

- **Text Loaders and Splitters:** To prepare raw profile documents into manageable chunks.
- **Embeddings:** Specifically, the HuggingFace `all-MiniLM-L6-v2` model converts text chunks into semantic vectors.
- **Vector Databases (Chroma):** These vectors are stored and indexed for efficient similarity search.
- **Custom LLM Wrapper:** The chatbot uses an OpenRouter-powered LLM for generating conversational responses based on retrieved context.
- **FastAPI Backend:** Handles API requests and orchestrates retrieval and response generation.
- **Streamlit Frontend (optional):** For interactive UI deployment.

This pipeline reflects a modern approach to building intelligent assistants by combining retrieval-augmented generation (RAG) techniques with state-of-the-art NLP models.

### Summary

The Vincent Chatbot project is a comprehensive showcase of applied AI skills. It bridges the gap between raw profile data and conversational AI, transforming static information into a lively, question-answering assistant. This project not only highlights my technical abilities but also demonstrates innovative thinking in presenting personal professional information through emerging AI tools.

## 3. Python Code and Architecture Overview

The core of the Vincent chatbot project is implemented using Python, a versatile language widely adopted for AI and web development. The backend is designed to efficiently serve chat requests, leverage large language models, and manage semantic knowledge retrieval, all while maintaining a clean and scalable architecture.

At the foundation lies **FastAPI**, a modern web framework known for its speed, simplicity, and native support for asynchronous programming. FastAPI allows us to expose the chatbot as a RESTful API service that can handle concurrent requests effectively. This choice ensures that the chatbot remains responsive and scalable under various loads.

To enforce structured communication, the API uses Pydantic models for input validation. For example, each chat request is expected to contain a JSON object with a single string field — the user query. This guarantees that the API processes only well-formed requests, improving robustness and reducing runtime errors.

One of the more advanced elements of the implementation is a custom wrapper around an external large language model hosted by OpenRouter. Rather than directly calling the OpenRouter API everywhere, we encapsulate this interaction inside a dedicated class. This class formats outgoing chat messages, manages HTTP requests, and parses the responses into a structure compatible with LangChain's interfaces. This abstraction simplifies integration and allows for easy swapping or upgrading of the underlying model in the future.

The chatbot's knowledge base begins with loading profile-related documents from a text file. Using LangChain's document loader, the system converts raw text into manageable chunks, breaking the text into smaller pieces to optimize retrieval and context relevance. A recursive splitter is employed to divide the content into chunks of approximately 1000 characters with some overlap, preserving continuity when fetching relevant information.

Once the text is prepared, the next step involves embedding these chunks into a vector database using a pretrained HuggingFace embedding model. This model transforms each document chunk into a dense vector that captures its semantic meaning, enabling similarity searches. The vector store chosen for this project is Chroma, which supports persistence, meaning embeddings are saved on disk and reused across sessions, boosting performance.

When the chatbot receives a query, it employs the vector store’s retriever to locate the top five document chunks most semantically aligned with the input. These chunks are then combined to provide context to the language model. The system prompt instructs the LLM to respond as "Vincent Bot," grounding its answers in the retrieved context to ensure relevance and accuracy.

By orchestrating the document retrieval and response generation within a single API endpoint, the system provides seamless interaction where user queries are dynamically answered based on Vincent’s profile information. This design effectively bridges large language models with domain-specific knowledge, creating a personalized chatbot experience.

Another important aspect of the project is security and configuration management. Sensitive information such as API keys is stored outside the source code in environment variables, loaded at runtime using the `dotenv` library. This best practice prevents secrets from being exposed in public repositories and simplifies environment-specific configuration during deployment.

In summary, the Python code architecture demonstrates several key strengths:

1. **Modularity**: Separation of concerns with dedicated classes and functions for API serving, LLM communication, document handling, and embedding.
2. **Scalability**: Use of FastAPI's async capabilities to handle multiple requests efficiently.
3. **Reusability**: Abstracted LLM wrapper enabling flexibility to swap models.
4. **Efficiency**: Persistent vector stores reduce redundant computations.
5. **Security**: Environment-based configuration safeguards sensitive credentials.

Together, these components create a robust, maintainable, and extensible backend that forms the brain of the Vincent chatbot — ready to serve intelligent, context-aware answers based on Vincent’s personal profile.

---

**End of Step 3: Python Code and Architecture Overview**

