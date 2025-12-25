# RAG Q&A Assistant for German Documents

This project implements a Retrieval-Augmented Generation (RAG) system for answering questions based on German documents (PDF, text). It includes:

- Document ingestion and chunking
- Embedding generation (sentence-transformers)
- Vector search (FAISS)
- Metadata and query storage in SQL
- FastAPI backend for query/API access
- Hugging Face models for generation

This repository is a learning and production-quality project to improve my skills in:
Python, NLP, SQL, FastAPI, Docker, LLMs, and software engineering.

## Run
```bash
uvicorn app.main:app --reload