import requests
import json
import pyttsx3
from greet import *  # Import custom modules

from searchnow import *

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to use pyttsx3 to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

def latestnews():
    # Dictionary with category and corresponding NewsAPI URLs
    apidict = {
        "business": "https://newsdata.io/api/1/news?apikey=pub_5358546115a3045c36dc855d38800928a5f22&q=technology&country=in&language=en&category=entertainment ",
        "entertainment": "https://newsdata.io/api/1/news?apikey=pub_5358546115a3045c36dc855d38800928a5f22&q=technology&country=in&language=en&category=entertainment ",
        "health": "https://newsdata.io/api/1/news?apikey=pub_5358546115a3045c36dc855d38800928a5f22&q=technology&country=in&language=en&category=health ",
        "science": "https://newsdata.io/api/1/news?apikey=pub_5358546115a3045c36dc855d38800928a5f22&q=sports&country=in&language=en&category=science ",
        "sports": "https://newsdata.io/api/1/news?apikey=pub_5358546115a3045c36dc855d38800928a5f22&q=sports&country=in&language=en&category=sports ",
        "technology": "https://newsdata.io/api/1/news?apikey=pub_5358546115a3045c36dc855d38800928a5f22&q=sports&country=in&language=en&category=technology "
    }

    url = None  # Initialize URL as None

    # Asking the user for a news category
    speak("Which field news do you want? [business], [health], [technology], [sports], [science]")
    field = takeCommand()  # Taking voice input from the user

    # Searching for the appropriate category in the dictionary
    for key, value in apidict.items():
        if key.lower() in field.lower():  # Check if user's input matches a category
            url = value  # Assign the corresponding URL
            print(url)
            break

    # If no valid URL was found (i.e., the category wasn't recognized)
    if url is None:
        print("URL is not found.")  # Inform the user that the category wasn't recognized
        speak("Sorry, the field you requested is not available.")
        return  # Exit the function since no valid URL is available

    try:
        # Making a request to the NewsAPI to fetch news articles
        news_response = requests.get(url)
        news_response.raise_for_status()  # This will raise an HTTPError if the response was unsuccessful
        news = news_response.json()  # Parsing the JSON response

        # Debugging: Print the entire response to see its structure
        print("API Response:", json.dumps(news, indent=4))

        # Access the correct key in the response
        if "results" in news:  # Assuming the articles are stored under 'results' in newsdata.io
            arts = news["results"]  # Fetching the articles from the response
        else:
            speak("Sorry, no articles found.")
            return

        # Informing the user that news is being read
        speak("Here is the first news article.")

        # Iterating over the articles
        for article in arts:
            title = article.get("title", "No title available")  # Extracting the title of the article
            print(title)  # Print the title
            speak(title)  # Speak the title out loud

            # Extracting the URL of the article for more details
            news_url = article.get("link", "No URL available")
            print(f"For more info visit: {news_url}")  # Print the URL

            # Asking the user if they want to continue or stop
            a = input("[Press 'a' to continue] or '2' to stop: ")
            if str(a) == "2":
                break  # Break the loop if the user chooses to stop

        # Informing the user that all articles have been read
        speak("That's all the news for now.")

    # Handling any errors that occur during the request
    except requests.exceptions.RequestException as e:
        # If any error occurs (like network issues or invalid API response), inform the user
        speak("Sorry, I couldn't fetch the news.")
        print(f"Error fetching news: {e}")
