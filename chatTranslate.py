import sched, time
from googletrans import Translator

logLocation = ""
translator = Translator()
scheduler = sched.scheduler(time.time, time.sleep)

def getTranslateLine():
    lines = list(open(logLocation, "r", encoding='utf-8'))
    lastLines = lines[-20:]
    for line in lastLines:
        lang = translator.detect(line)[0]
        print(lang)
        if lang != "en":
            translated = translator.translate(line, dest="en")
            print(translated)

    print("Checked for new chat")

def init(logDir):
    global logLocation 
    logLocation = logDir + "\\console.log"
    print("Auto Translate Initialised.")
    while True:
        e1 = scheduler.enter(2, 1, getTranslateLine)
        scheduler.run()