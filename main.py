from app import RagPipeline


def main():
    """Initialize and run the RAG pipeline for answering user queries."""
    try:
        pipeline = RagPipeline()
        pipeline.ingest("data/data.txt")

        while True:
            query = input("\nAsk a question: ")
            answer = pipeline.query(query)
            print(f"\nAnswer:\n: {answer}")
    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
