import sched, time
from googletrans import Translator

logLocation = ""
translator = Translator()
scheduler = sched.scheduler(time.time, time.sleep)

def getTranslateLine():
    with open(logLocation, "r", encoding='ISO-8859-1') as logfile:
        lines = list(logfile)
        lastLines = lines[-20:]
        for line in lastLines:
            lang = translator.detect(line)[0]
            if lang != "en":
                translated = translator.translate(line, dest="en")
                print(f"Language: {lang}. Translated: {translated}")
        print("Checked for new chat.")

def init(initLogLocation):
    global logLocation 
    logLocation = initLogLocation
    print("Auto Translate Initialised.")
    while True:
        e1 = scheduler.enter(2, 1, getTranslateLine)
        scheduler.run()