import speech_recognition as sr
import pyttsx3
from datetime import date, datetime

# bot_mouth은 봇의 사고 방식을 텍스트에서 음성으로 바꾸는 변수다.
bot_mouth = pyttsx3.init() 
# bot_ear은 사용자의 음성을 인식하여 텍스트로 변환하는 변수
bot_ear = sr.Recognizer()


while True:
	with sr.Microphone() as mic:
		print("bot: Listening...")
		audio = bot_ear.listen(mic)
	try:
		you = bot_ear.recognize_google(audio)
	# 사용자 음성을 감지 할 수없는 경우 예외 처리.
	except sr.UnknownValueError:
			print("Could not understand audio")
	# request에 대한 예외 처리.	
	except sr.RequestError as e:
			print("Could not request results; {0}".format(e))

# 봇의 간단한 답변들:
	if you == "":
		bot_brain = "umm.. I would not understand you.. try again"
	elif "hello" in you:
		print("hello user.")
	elif "today" in you:
		bot_brain = str(date.today())
	elif "time" in you:
		date_time =datetime.now()
		bot_brain = date_time.strftime("%H hours %M minutes %S seconds")
	elif "bye" in you:
		# 봇의 인사를 출력하고 싶다.
		bot_brain = "see you again."
		print("you: " + you)
		bot_mouth.say(you)
		bot_mouth.runAndWait()
		break
	else:
		bot_brain == "Can you say again?"

# 사용자의 말을 출력한다.
# 봇은 말한후 기다려 지킨다.
print("you: " + you)
bot_mouth.say(bot_brain)
bot_mouth.runAndWait()
