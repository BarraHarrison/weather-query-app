import pytest
from my_package import query

def test_query_valid():
    question = "What's the weather like in New York today?"
    answer = query(question)
    assert isinstance(answer, str)
    assert "weather in New York today" in answer.lower()

def test_query_no_location():
    question = "What's the weather like today?"
    answer = query(question)
    assert "couldn't find a location" in answer.lower()

def test_query_no_date():
    question = "What's the weather like in Paris?"
    answer = query(question)
    assert "weather in Paris today" in answer.lower()