
import webbrowser
import wolframalpha
import pyttsx3
import speech_recognition as sr
import wikipedia
from datetime import datetime
import webbrowser
import subprocess
import pywhatkit


# Initializations:
running = True
engine = pyttsx3.init()
voices = engine.getProperty('voices')


#voice selection:
select_voice = input("Select voice(Male/Female): ")
if select_voice.lower() == "male":
    engine.setProperty('voice',voices[0].id)
    name = "Eren"
else:
    engine.setProperty('voice',voices[1].id)
    name = "Mikasa"

client = wolframalpha.Client("92QAR3-8T389K6VU8")


#speak function:
def speak(text):
    print(f"{name}: {text}")
    engine.say(text)
    engine.runAndWait()


#listen function:
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print(f"User: {command}")
        except:
            speak("I could not understand that, will you please repeat it?")         
            command = listen().lower()
    return command


def intro():
    speak(f"Hi, I am {name}.")
    speak("I am your personal assistant!")


intro()
while running:

    command = listen().lower()
    if ("exit" or "bye") in command:
        speak("Exiting program.")
        speak("Thankyou for using me.")
        running = False
    

    elif "open youtube" in command:
        speak("What is the title?")
        title = listen()
        pywhatkit.playonyt(title)
        speak(f"Searching for {title} on YouTube.")


    elif "take screenshot" in command:
        speak("Capturing a Screenshot.")
        pywhatkit.take_screenshot()
    

    elif "notepad" in command:
        speak("Opening notepad.")
        subprocess.run('notepad')
        #running = False
    

    elif "on google" in command:
        speak("Searching it on google.")
        pywhatkit.search(command)
        #running = False


    elif "open google" in command:
        speak("Opening Google.")
        webbrowser.open('www.google.com')
        #running = False
    

    elif "open camera" in command:
        speak("Okay, opening camera")
        subprocess.run('start microsoft.windows.camera:', shell= True)
        speak("Good to see you!")
        #running = False
    

    elif "shutdown" in command:
        speak("Shutting down!")
        subprocess.run('shutdown /s')


    elif "restart" in command:
        speak("Restarting your pc.")
        subprocess.run('shutdown /r')
    

    elif "log out" in command:
        speak("You will be logged out in a minute..")
        subprocess.run('shutdown /l')


    elif "create file" in command:
        speak("Name of the file? (without extension)")
        file_name = listen()
        with open(f"{file_name}.txt", 'w') as file:
            speak("Content of the file?")
            file_content = listen()
            file.write(file_content)
            speak("File created successfully!")
    

    elif "date" in command:
        date = datetime.now().date()
        speak(f"Today: {date}")
    

    elif "time" in command:
        time = datetime.now().time()
        speak(f"Today: {time}")
    

    else:

        if "wikipedia" in command:
            summary = wikipedia.summary(command, sentences =2)
            speak(summary)
            
        else:
            try:
                res = client.query(command)
                result = res.results
                speak(next(result).text)
                     
            except:
                speak("I didnt catch that, would you like me to search that on google?")
                ans = listen()
                if "yes" in ans:
                    speak("alright.")
                    pywhatkit.search(command)
                    running = False
                if "no" in ans:
                    speak("okay.")
                
                    

                

