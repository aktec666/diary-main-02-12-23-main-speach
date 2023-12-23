import speech_recognition as sr

def audio():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("говори")
        audio = r.listen(source)

    return r.recognize_amazon(audio, region='en-EN')

print(audio())