import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as s:
    r.adjust_for_ambient_noise(s)

    while True:
        audio = r.listen(s)

        speech = r.regonize_google(audio, language='pt')

        print('voce disse', speech)
