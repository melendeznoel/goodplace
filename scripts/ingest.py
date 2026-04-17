from app import RagPipeline


def main():
    pipeline = RagPipeline()

    pipeline.ingest("data/data.txt")

    print("Ingestion complete.")

if __name__ == "__main__":
    main()
