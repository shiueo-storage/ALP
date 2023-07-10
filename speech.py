import requests
from bs4 import BeautifulSoup
import webbrowser
import speech_recognition as sr

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36'
                  '(KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
Recognizer = sr.Recognizer()
mic = sr.Microphone()
while 1:
    data = ""
    with mic as source:
        print('recording started')
        audio = Recognizer.listen(source, phrase_time_limit=2)
    try:
        data = Recognizer.recognize_google(audio, language="ko")
        print(data)
    except Exception as e:
        print(e)

    if '검색' in data:

        link = f"https://www.google.com/search?q={data[:-2]}"
        webbrowser.open(link)
    else:
        print("no query", data)
