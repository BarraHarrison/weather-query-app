
import my_package 

questions = [
    "What will the weather be like in Seoul tomorrow?",
    "How is the weather in New York today?",
    "Will it rain in London this weekend?",
    "What's the forecast for Tokyo next Monday?",
    "Do you think it will snow in Moscow next week?"
]

for question in questions:
    answer = my_package.query(question)
    print(f"Question: {question}")
    print(f"Answer: {answer}\n")
