import requests
import os
from dotenv import load_dotenv
import spacy
import dateparser
from datetime import datetime, timedelta

load_dotenv()
API_KEY = os.getenv('OPENWEATHER_API_KEY')

nlp = spacy.load('en_core_web_sm')

def query(question):
    locations, dates = parse_question(question)
    if not locations:
        return "I'm sorry, I couldn't find a location in your question."
    if not dates:
        date_text = 'today' 
    else:
        date_text = dates[0]

    location = locations[0]

    # Preprocess the date_text to handle phrases like 'this weekend', 'next Monday'
    date_text = preprocess_date_text(date_text)

    # Parse date with improved settings
    target_date = parse_date(date_text)
    if not target_date:
        return "I'm sorry, I couldn't understand the date you mentioned."

    # Check if the date is within the next 5 days (OpenWeatherMap's forecast limit)
    now = datetime.now()
    max_forecast_date = now + timedelta(days=5)
    if target_date.date() > max_forecast_date.date():
        return "Sorry, I can only provide forecasts up to 5 days from today."

    weather_data = get_weather(location)
    if 'list' in weather_data:
        forecast = get_forecast_for_date(weather_data, target_date)
        if forecast:
            response = generate_response(location, target_date, forecast)
        else:
            response = f"Sorry, I couldn't find weather data for {location} on {date_text}."
    else:
        response = f"Sorry, I couldn't retrieve weather data for {location}."
    return response

def parse_question(question):
    doc = nlp(question)
    locations = [ent.text for ent in doc.ents if ent.label_ == 'GPE']
    dates = [ent.text for ent in doc.ents if ent.label_ == 'DATE']

    
    if not dates:
        common_date_phrases = ['this weekend', 'next weekend', 'next week', 'next Monday', 'tomorrow']
        for phrase in common_date_phrases:
            if phrase in question.lower():
                dates.append(phrase)
                break

    return locations, dates

def preprocess_date_text(date_text):
    date_mappings = {
        'this weekend': 'next Saturday',
        'next weekend': 'in 1 week',
        'next week': 'in 1 week',
        'next Monday': 'next Monday',
    }
    date_text_lower = date_text.lower()
    for phrase, replacement in date_mappings.items():
        if phrase in date_text_lower:
            date_text = date_text_lower.replace(phrase, replacement)
            break
    return date_text

def parse_date(date_text):
    settings = {
        'PREFER_DATES_FROM': 'future',  # Prefer future dates
        'RELATIVE_BASE': datetime.now(),  # Set the base date for relative parsing
    }
    target_date = dateparser.parse(date_text, settings=settings)
    return target_date

def get_weather(location):
    # Using the 5-day forecast API endpoint
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def get_forecast_for_date(weather_data, target_date):
    forecast_list = weather_data.get('list', [])
    for forecast in forecast_list:
        forecast_time = datetime.fromtimestamp(forecast['dt'])
        if forecast_time.date() == target_date.date():
            return forecast
    return None

def generate_response(location, target_date, forecast):
    # Extract necessary information from forecast data
    description = forecast['weather'][0]['description']
    temp_celsius = forecast['main']['temp']
    temp_celsius = round(temp_celsius, 1)

    # convert to Fahrenheit
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    temp_fahrenheit = round(temp_fahrenheit, 1)

    date_formatted = target_date.strftime('%A, %B %d')
    response = (f"The weather in {location} on {date_formatted} will be {description} "
                f"with a temperature of {temp_celsius}°C ({temp_fahrenheit}°F).")
    return response
