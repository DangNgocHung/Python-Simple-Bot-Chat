from datetime import date, datetime

you = "time"
bot_brain = ""

#기계에 대한 5 개의 간단한 답을 만들기.

if you == "":
	print("you dont say any thing.")
	bot_brain = "umm.. I would not understand you.. try again"
elif you == "hello":
	print("you: " + you)
	bot_brain = "Hello user."
elif you == "today":
	print("you: " + you)
	today = date.today()
	bot_brain = str(date.today())
elif "time" in you:
	date_time =datetime.now()
	bot_brain = date_time.strftime("%H hours %M minutes %S seconds")
else:
	bot_brain = "Can you say again?"	

print("bot: " + bot_brain)

