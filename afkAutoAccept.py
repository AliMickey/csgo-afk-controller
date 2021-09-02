import time, pyautogui

def init():
    print("Auto Match Accept Controller Initialised. Make sure to tab into the game within 5 seconds.")
    while True:
        time.sleep(5)
        size = pyautogui.size()
        pyautogui.moveTo(5,5)
        pyautogui.moveTo(size[0]/2, size[1]/2+50)
        pyautogui.click()
        print("Clicked")