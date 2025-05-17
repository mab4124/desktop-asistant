# Voice-Controlled Desktop Assistant (Speech-to-Text)

This project is a **voice-activated desktop assistant** that responds to natural speech to perform various actions such as fetching news, telling jokes, providing weather updates, searching Wikipedia, and playing YouTube videos. 
It uses speech recognition, text-to-speech synthesis, APIs, and browser automation for a seamless user experience.

## Features
**Voice Interaction**: Accepts voice commands and responds using text-to-speech (TTS).
**Wikipedia Search**: Searches and displays information using browser automation.
**YouTube Playback**: Plays requested videos using automated browser control.
**Weather Updates**: Retrieves real-time weather data for Hyderabad using OpenWeatherMap API.
**Latest News**: Reads top 3 news articles using NewsAPI.
**Random Jokes**: Fetches a random joke from an online API.
**Fun Facts**: Speaks a random interesting fact using the 'randfacts' module.

## File Structure

File Name             
'assistant.py'               Main file to run the assistant, handles command parsing and logic.
'jokes.py'                   Retrieves random jokes from an online joke API.             
'news.py'                    Fetches latest news headlines using NewsAPI.                
'weather.py'                 Gets current temperature and weather description.           
'wikipedia_automation.py'    Automates Wikipedia searches using Selenium.                
'youtube_automation.py'      Automates YouTube video searches and playback using Selenium. 

---

## Requirements

- Python 3.x
- Packages:
  - 'speechrecognition'
  - 'pyttsx3'
  - 'selenium'
  - 'requests'
  - 'randfacts'
- Chrome Browser
- ChromeDriver (place path correctly in 'wikipedia_automation.py' and 'youtube_automation.py')


How to Run

1. Install the required Python libraries.
2. Ensure ChromeDriver path is correct and Chrome browser is installed.
3. Run the main script:

bash
python assistant.py
