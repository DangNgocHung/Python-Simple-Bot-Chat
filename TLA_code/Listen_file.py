import speech_recognition as sr

bot_ear = sr.Recognizer()

   	with sr.Microphone() as mic:
	# mic = sr.Microphone()

	print("bot: Listening...")
	audio = bot_ear.listen(mic)

you = bot_ear.recognize_google(audio)

print("you: " + you)
