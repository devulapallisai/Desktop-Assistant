import speech_recognition as sr
from datetime import datetime
import pyttsx3
import os
from googlesearch import search 
import pyjokes              
import wikipedia
import webbrowser
engine=pyttsx3.init('sapi5') 
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def wishme():
    if(datetime.now().hour>=0 and datetime.now().hour<12):
        speak('Good morning sir!')
    elif(datetime.now().hour>=12 and datetime.now().hour<16):
        speak('Good Afternoon Sir!')
    elif(datetime.now().hour>=16 and datetime.now().hour<=20):
        speak('Good evening sir!')
    else:
        speak('Good night sir!')
    speak('This is your desktop virtual assistant Jarvis and How may I help you!')
def detectourAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        r.adjust_for_ambient_noise(source, duration = 1)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        # speak(r"Please try saying that again sir I couldn't hear you properly")
        return "None"
    return query
def detectourAudiostart():
    print('Hello')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        # r.energy_threshold=400
        audio = r.listen(source)
        r.adjust_for_ambient_noise(source, duration = 1)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        # print(e)   
        print('Say that again..') 
        return "None"
    return query
def command(text):
    query=text.lower()
    if(query.find("wikipedia")!=-1):
        wikipedia.set_lang("en")
        speak('What do you want to search! sir')
        searchit=detectourAudio()
        speak('According to wikipedia...')
        data=wikipedia.summary(searchit,sentences="2")
        speak(data)
    elif(query.find("i am")!=-1):
        speak('Welcome sir! Please say your command and I will give results accordingly')
    elif(query.find("google")!=-1 or query.find("chrome")!=-1):
        webbrowser.open_new_tab('http://google.com')
    elif(query.find("youtube")!=-1):
        webbrowser.open_new_tab('https://www.youtube.com')
    elif(query.find("codewithharry")!=-1):
        webbrowser.open_new_tab('https://www.youtube.com/c/CodeWithHarry/playlists')
    elif(query.find("stack overflow")!=-1):
        webbrowser.open_new_tab('https://stackoverflow.com/')
    elif(query.find('gmail')!=-1):
        webbrowser.open_new_tab('https://mail.google.com/mail/u/0/')
    elif(query.find('class')!=-1):
        webbrowser.open_new_tab('https://docs.google.com/document/d/16_o_b5Gxtsmg4-3Xa3VNlwR5G5O3XCKMOe-sGUQmwQk/edit')
    elif(query.find('time')!=-1):
        strTime = datetime.now().strftime("%H:%M:%S")    
        speak(f"Sir, the time is {strTime}")
    elif(query.find('music')!=-1):
        listindir=r'C:\Users\user\OneDrive\Desktop\songs\Vikramvedha.mp3'
        os.startfile(listindir)
    elif(query.find('vs code')!=-1):
        os.startfile(r'C:\Users\user\AppData\Local\Programs\Microsoft VS Code\Code.exe')
    elif(query.find('joke')!=-1):
        speak(pyjokes.get_joke())
    elif 'exit' in query:
        speak(r"Thanks for giving me your time I am pleased to hear your queries again and to answer them")
        exit()
    elif(query.find('your name')!=-1 or query.find('you')!=-1):
        speak(r'My name is Jarvis sir.You can call me Jarvis.')
    elif(query.find('whatsapp')!=-1):
        os.startfile(r'C:\Users\user\AppData\Local\WhatsApp\WhatsApp.exe')
    elif(query.find('github')!=-1):
        webbrowser.open(r'https://github.com/')
    elif(query.find('vmware')!=-1):
        os.startfile(r'F:\Vmware workstation\vmware.exe')
    elif(query.find(r'how are you')!=-1):
        speak('I am fine sir thanks for asking and How are you?')
    elif(query.find('solidedge')!=-1):
        os.startfile(r'F:\Solid edge\Program\Edge.exe')
    elif(query.find('search')!=-1):
        speak('what do you want to search now')
        searchit=detectourAudio()
        listed=search(searchit,tld="com",num=1)
        webbrowser.open(str(listed))


if __name__=="__main__":
    string=detectourAudiostart()
    if(string.lower().find("hello")!=-1):
        wishme()
        while(True):
            query=detectourAudio()
            if(query==""):
                speak(r"Please try saying that again sir I couldn't hear you properly")
            else:
                command(query)