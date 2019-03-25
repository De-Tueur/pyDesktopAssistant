import speech_recognition as sr
import os,sys
import webbrowser
import pyttsx3
#needs to install pip install python-espeak
obj=pyttsx3.init();
def listener():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            r.pause_threshold = 0.5
            r.adjust_for_ambient_noise(source)
            r.operation_timeout = 4
            #audio = r.record(source,duration=4)
            audio = r.listen(source,timeout=4)
            cmd = r.recognize_google(audio,language="en-US").lower()
    except sr.RequestError:
        obj.say('Slow NEtwork')
        cmd=listener()
    except sr.UnknownValueError:
        obj.say('Your last command couldn\'t be heard')
        cmd = listener();
    return cmd
def talker(audio):
    obj.say(audio)
def myCommand():
        obj.say("Ready")
        command=listener()
        obj.say('You said: ' + command)
        obj.runAndWait()
        return command

def assistant(command):
    if 'open duck' in command:
        url = 'https://www.duckduckgo.com/'
        talker('Just doing my thing')
        webbrowser.open(url)
    elif 'website' in command:
        obj.say("Enter The Website Name")
        domain = listener()
        url = 'https://www.' + domain
        webbrowser.open(url)
        talker('Just doing my thing')
    elif 'repeat' in command:
        talker(' You Said '+command)
    elif 'system' in command:
        print(os.uname())
    elif 'hi' in command:
        talker('Hello User')
    elif 'exit' in command:
        obj.close()
        sys.exit()
    else:
        talker('I don\'t know what you mean!')

if __name__=="__main__":
    while True:
        cmd=myCommand()
        assistant(cmd)
