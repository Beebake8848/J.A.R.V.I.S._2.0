import speech_recognition as sr
import pywhatkit
import webbrowser
import datetime
import pyttsx3
import pyjokes
import os
import sys
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    
    except Exception as e:
        print(e)
        print("Say that Again please...")
        speak("Say that Again please...")
        return "None"
    return query.lower()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis 2 point o , Sir. Please tell me how may I help you")


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], 
                 ["wikipedia", "https://www.wikipedia.com"],
                   ["google", "https://www.google.com"],
                   ["chat gpt", "https://chat.openai.com"],
                   ]
        
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speak(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'what is' in query or 'who is' in query:
            speak('Searching...')
            try:
                results = wikipedia.summary(query, sentences=1)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.PageError:
                speak(f"Sorry, I couldn't find any information on '{query}' on Wikipedia.")
            except Exception as e:
                speak(f"An error occurred: {e}")

        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current time is ' + time)

        elif 'date' in query:
            current_date = datetime.datetime.now().strftime('%B %d, %Y')
            speak('Today is ' + current_date)

        elif 'open code' in query:
            codePath = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'are you single' in query:
            speak('I am in a relationship with wifi')

        elif 'who are you' in query:
            speak('I am Jarvis , a virtual assistant created by beebake')

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)
            
        elif 'calculate' in query:
            expression = query.replace('calculate', '').strip()
            expression = expression.replace('x', '*').replace('times', '*')  # Convert 'x' or 'times' to '*'
            try:
                result = eval(expression)
                speak(f"The result of {expression} is {result}")
            except Exception as e:
                speak("Sorry, I couldn't calculate that.")

            
        elif 'jarvis stop' in query or 'exit jarvis' in query:
            speak("Thank you for using Jarvis! Have a great day! Goodbye!")
            sys.exit()

        