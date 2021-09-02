import afkInGame, afkAutoAccept, chatTranslate

logLocation = "D:\Games\Steam\steamapps\common\Counter-Strike Global Offensive\csgo"

print("Choose from the following options:")
print("1 - In Game AFK Controller")
print("2 - Auto Match Accept Controller")
print("3 - Auto Chat Translator")
print("4 - Quit")

while True:
    while True:
        try:
            inp = int(input("Enter a number: "))
            break
        except:
            print("Invalid input")

    if inp == 1:
        afkInGame.init(logLocation)
    elif inp == 2:
        afkAutoAccept.init()
    elif inp == 3:
        chatTranslate.init(logLocation)
    elif inp == 4:
        exit()