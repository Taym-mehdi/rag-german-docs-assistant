# app/config.py
import os
from pathlib import Path
from dotenv import load_dotenv

# Determine project root (rag-german-docs-assistant/)
root = Path(__file__).resolve().parents[1]

# Load .env if exists
env_path = root / ".env"
if env_path.exists():
    load_dotenv(env_path)

# Default development DB (local SQLite)
DEFAULT_DB = f"sqlite:///{root / 'data' / 'rag_dev.db'}"

DATABASE_URL = os.getenv("DATABASE_URL", DEFAULT_DB)
