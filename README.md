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
