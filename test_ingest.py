# test_ingest.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.models import Base
from app.ingestion.ingest import ingest_document
from app.retrieval.vector_store import VectorStore

# 1️⃣ Setup database session (adjust your DB URL if needed)
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables if not exist
Base.metadata.create_all(bind=engine)

def test_ingest():
    db = SessionLocal()

    # 2️⃣ Example text
    text = (
        "Das ist ein langer deutscher Text, der für das Testen der Chunking-"
        "und Embedding-Pipeline verwendet wird. Wir wollen prüfen, ob alles "
        "richtig funktioniert."
        "Khalifa entered the pornographic film industry in October 2014, after being recruited by a man who asked her if she was interested in nude modeling.[11][12] Her stage name was taken from the name of her dog, Mia, and American rapper Wiz Khalifa.[13] She came to widespread attention after the release of a scene from Bang Bros in which she wears a hijab during a threesome with Julianna Vega and Sean Lawless.[5] The scene brought Khalifa instant popularity, as well as criticism from writers and religious figures, and led to her parents publicly disowning her.[5][14] Alex Hawkins, vice president of marketing for xHamster, said, The outrage it caused in the Arab world ended up being a bit of a 'Streisand effect'. Suddenly, everyone was searching for her. The effort to censor her only made her more ubiquitous.[5] With more than 1.5 million views, the 22-year-old Khalifa became the most searched-for performer on the adult video sharing website Pornhub.[2]On December 28, 2018, Pornhub revealed that she was the No. 1 ranked performer on their website.[4] After becoming the most searched-for actress on Pornhub, Khalifa received online death threats,[1][15] including a digitally manipulated image of Khalifa being beheaded by the Islamic State[16] and a warning that she would be the first person in Hellfire,[17] to which she jokingly replied,I've been meaning to get a little tan recently. Lebanese newspapers wrote articles critical of Khalifa, which she considered trivial due to other events in the region.[19]"
    )

    # 3️⃣ Ingest document
    document = ingest_document(
        db=db,
        title="Test Document",
        filename="test.txt",
        text=text
    )

    print("Document ingested with ID:", document.id)

    # 4️⃣ Verify chunks
    print("Chunks saved:")
    for chunk in document.chunks:
        print(f"- {chunk.id}: {chunk.chunk_text}")

    # 5️⃣ Verify vectors in VectorStore
    vector_store = VectorStore()
    results = vector_store.similarity_search("deutscher Text")
    print("\nTop similarity search results for 'deutscher Text':")
    for r in results:
        print(f"- ID: {r['id']}, Score: {r['score']}, Text: {r['document']}")

    db.close()

if __name__ == "__main__":
    test_ingest()
