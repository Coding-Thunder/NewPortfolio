import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)

if __name__ == "__main__":
    speak("news for today")
    url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=b19b8e3bec81460285a57a84ab5aa768"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict["articles"]
    for content in arts:
        speak(content["title"])   
        speak("Next Is  ")