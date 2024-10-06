import sys
from .weather_query import query

def main():
    if len(sys.argv) > 1:
        question = ' '.join(sys.argv[1:])
        answer = query(question)
        print(f"Question: {question}")
        print(f"Answer: {answer}")
    else:
        try:
            while True:
                question = input("Ask a weather question (or type 'exit' to quit): ")
                if question.lower() in ['exit', 'quit']:
                    print("Goodbye!")
                    break
                answer = query(question)
                print(f"Answer: {answer}\n")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            sys.exit()
