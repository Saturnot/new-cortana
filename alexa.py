from os import replace
import speech_recognition as sr
import pyttsx3
import pyaudio
import pywhatkit
import datetime
import wikipedia
import webbrowser
import pyperclip
import json
from random import *
from time import sleep



#------------------------------------- initialisation -------------------------

wikipedia.set_lang('fr')

listener = sr.Recognizer()
# pyttsx3
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0"
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voice_id)
engine.setProperty("rate", 170)


run = True


#------------------------------------ def des fonctions ------------------------
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('en ecoute...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="fr-FR")
            command = command.lower()
    except:
        pass
    return command

def run_jarvis():
    command = take_command()
    print (command)
    if 'copie' in command:
        text_copy = command.replace('copie', '')
        pyperclip.copy(text_copy)
    elif 'bonjour' in command:
        talk('Bonjour je m\'apppelle Jarvis')
    elif 'joue' in command:
        song = command.replace('joue', '')
        talk('d\'accord je joue ' + song + "sur youtube")
        pywhatkit.playonyt(song)
    elif 'heure' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('Il est '+ time )
    elif 'qui est' in command:
        person = command.replace('qui est ', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'blague' in command:
        n = randint(0,221)
        with open('myjokes_fr.json', 'r', encoding='utf-8') as f:
            json_object = json.loads(f.read())
        talk(json_object['jokes'][n]['joke'])
        sleep(1.0)
        talk(json_object['jokes'][n]['answer'])
    elif 'recherche' and 'google' or 'internet' in command:
        search = command.replace('recherche ', '')
        search = search.replace('rechercher ', '')
        search = search.replace(' sur google', '')
        search = search.replace(' sur internet', '')
        search = search.replace(' ', '+')
        url = 'https://www.google.com/search?q=' + search
        print(url)
        webbrowser.open(url)
    elif 'stop' in command:
        run = False
    else:
        talk('Je n\'ai pas compris')


#------------------------------ run code -----------------------------------

while run == True:
    run_jarvis()
