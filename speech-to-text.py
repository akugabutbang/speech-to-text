import speech_recognition as sr

def inputCommand():
    r = sr.Recognizer()
    query = ""
    with sr.Microphone(device_index=2) as source:
        print("Listening...")
        r.pause_threshold = 2
        try:
            query = r.recognize_google(r.listen(source), language="en-IN")
        except Exception as e:
            output("Say that again Please...")
    return query

while True:
    results = inputCommand().lower()
    print(results)
