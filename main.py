import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from deep_translator import GoogleTranslator

# voice listener

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# talk function


def talk(text):
    engine.say(text)
    engine.runAndWait()


# edith?


def welcome():
    engine.say("Hello, Yusef. I am Edith. Your personal virtual assistant. How can I help you? ")
    engine.runAndWait()


welcome()


# listen function


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'edith' in command:
                command = command.replace('edith', '')
    except:
        pass
    return command


# language translator function

# def lang_trans():


# web bot functions


def good_life():
    talk("Enter the shoe that you are looking for")
    shoe = input("Enter the shoe that you are looking for ")
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.thegoodlifespace.com/")
    print(driver.title)
    search = driver.find_element_by_id("search")
    search.send_keys(shoe)
    search.send_keys(Keys.RETURN)


def adidas():
    talk("Enter the shoe that you are looking for")
    shoe = input("Enter the shoe that you are looking for ")
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://shop.adidas.ae")
    print(driver.title)
    search = driver.find_element_by_id("js-search-input")
    search.send_keys(shoe)
    search.send_keys(Keys.RETURN)

# jarvis function


def run_edith():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('The time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'search' in command:
        item = command.replace('search', '')
        report = wikipedia.summary(item, 1)
        print(report)
        talk(report)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'translate' in command:
        translate = command.replace('translate', '')
        talk("To which language?")
        print("1. English\n2. French\n3. Arabic\n4. Spanish\n5. German ")
        lang = input("Enter ")
        if lang == '1':
            dest = 'en'
            language = 'english'
        elif lang == '2':
            dest = 'fr'
            language = 'french'
        elif lang == '3':
            dest = 'ar'
            language = 'arabic'
        elif lang == '4':
            dest = 'es'
            language = 'spanish'
        elif lang == '5':
            dest = 'de'
            language = 'german'
        to_translate = translate
        translated = GoogleTranslator(source='auto', target=dest).translate(to_translate)
        talk(translate + ' in ' + language + ' is ' + translated)
        print(translate + ' in ' + language + ' is ' + translated)
    elif 'google' in command:
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        driver = webdriver.Chrome(PATH)
        driver.get("https://www.google.com/")
        print(driver.title)
        search = driver.find_element_by_name("q")
        web_search = command.replace('google', '')
        search.send_keys(web_search)
        search.send_keys(Keys.RETURN)
        web_search = command.replace('google', '')
        talk('heres what i found about ' + web_search + ' on the web')
        print('heres what i found about ' + web_search + ' on the web')
    elif 'amazon' in command:
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        driver = webdriver.Chrome(PATH)
        driver.get("https://www.amazon.ae/")
        print(driver.title)
        search = driver.find_element_by_id("twotabsearchtextbox")
        web_search = command.replace('amazon', '')
        search.send_keys(web_search)
        search.send_keys(Keys.RETURN)
        web_search = command.replace('amazon', '')
        talk('heres what i found for ' + web_search + ' on amazon')
        print('heres what i found for ' + web_search + ' on amazon')
    elif 'good life' in command:
        good_life()
    elif 'adidas' in command:
        adidas()
    elif 'thanks' or 'thank you' in command:
        print("No problem")
        talk("No problem")
    elif 'goodbye' or 'bye' in command:
        print("Goodbye")
        talk("Goodbye")
        exit()
    else:
        talk('Sorry I didnt get that. can you say it again')


while True:
    run_edith()
