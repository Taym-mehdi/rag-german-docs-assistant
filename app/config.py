# app/config.py
import os
from pathlib import Path
from dotenv import load_dotenv

# try to load a .env file if present (development)
root = Path(__file__).resolve().parents[1]
env_path = root / ".env"
if env_path.exists():
    load_dotenv(env_path)

# Default dev DB: sqlite file in project root
DEFAULT_DB = f"sqlite:///{root / 'data' / 'rag_dev.db'}"

DATABASE_URL = os.getenv("DATABASE_URL", DEFAULT_DB)
