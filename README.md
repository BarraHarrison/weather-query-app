# Weather Query Application

This project is a Python package that allows users to ask natural language questions about the weather and receive responses in natural language. It uses natural language processing (NLP) to interpret user queries and fetches weather data from the OpenWeatherMap API.

Features:

- Interpret natural language weather questions.
- Fetch current and forecast weather data for locations worldwide.
- Provide natural language responses with weather conditions and temperatures.
- Accessible via a command-line interface (CLI).

## Installation

### **Prerequisites**

- **Python 3.7 or higher** is required.
- Ensure that **pip** is installed and up to date.

### **Step 1: Clone the Repository**

bash
git clone https://github.com/your_username/weather-query-app.git
cd weather-query-app


## Usage

### **Running the Application**

You can interact with the application using the `weather-cli` command.

#### **Option 1: Interactive Mode**

- Run the following command to start the application in interactive mode:

bash
weather-cli

Ask a weather question (or type 'exit' to quit):
What is the weather like in Paris tomorrow?
Answer: The weather in Paris on Monday, October 07 will be clear sky with a temperature of 18.5°C (65.3°F).

#### **Option 2: Direct Question**

- You can also ask your question directly as a command-line argument.

weather-cli "Will it rain in London this weekend?"
 
- Expected Output:

Question: Will it rain in London this weekend?
Answer: The weather in London on Saturday, October 12 will be light rain with a temperature of 14.3°C (57.7°F).


## Troubleshooting

- **OpenWeatherMap API Key Not Found:**

  Ensure that you've created a `.env` file in the project root directory with your API key:

  ```dotenv
  OPENWEATHER_API_KEY=your_actual_api_key_here

## Dependencies

The application requires the following Python packages:

- `requests`
- `spacy`
- `python-dotenv`
- `dateparser`

Install all dependencies using:

```bash
pip install -r requirements.txt
