import afkInGame, afkAutoAccept, chatTranslate, os

# Edit the first path location only. Don't touch "\console.log"
logLocation = "D:\Games\Steam\steamapps\common\Counter-Strike Global Offensive\csgo" + "\console.log"

print("Choose from the following options:")
print("1 - In Game AFK Controller")
print("2 - Auto Match Accept Controller")
print("3 - Auto Chat Translator")
print("4 - Delete Logfile (CS:GO Must Be Closed)")
print("5 - Quit")

while True:
    while True:
        try:
            choice = int(input("Enter a number: "))
            break
        except Exception as e:
            print(e)
            print("Invalid input")
            break

    if choice == 1:
        afkInGame.init(logLocation)
    elif choice == 2:
        afkAutoAccept.init()
    elif choice == 3:
        chatTranslate.init(logLocation)
    elif choice == 4:
        if os.path.exists(logLocation):
            os.remove(logLocation)
            print("Logfile deleted.")
        else:
            print("Logfile does not exist.")
    elif choice == 5:
        exit()