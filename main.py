from app import RagPipeline


def main():
    pipeline = RagPipeline()

    pipeline.ingest("data/data.txt")

    while True:
        query = input("\nAsk a question: ")

        answer = pipeline.query(query)

        print(f"\nAnswer:\n: {answer}")

if __name__ == "__main__":
    main()
