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

rag-german-docs-assistant/
│
├── README.md
├── requirements.txt
├── .gitignore
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI entrypoint
│   ├── config.py            # configuration settings
│   ├── db/
│   │   ├── __init__.py
│   │   ├── models.py        # SQLAlchemy models
│   │   ├── database.py      # DB engine & session
│   ├── ingestion/
│   │   ├── __init__.py
│   │   ├── chunker.py       # chunking logic
│   │   ├── ingest.py        # document ingestion pipeline
│   ├── retrieval/
│   │   ├── __init__.py
│   │   ├── embeddings.py    # embedding model
│   │   ├── vector_store.py  # FAISS index
│   ├── generation/
│   │   ├── __init__.py
│   │   ├── generator.py     # HuggingFace model
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── query.py         # Pydantic schemas
│   ├── utils/
│       ├── __init__.py
│       ├── pdf_reader.py    # later
│       ├── logger.py
│
├── tests/
│   ├── test_chunking.py
│   ├── test_embeddings.py
│   ├── test_api.py
│
└── docker-compose.yml    # later
