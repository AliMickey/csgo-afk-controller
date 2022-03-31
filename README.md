# CSGO Utilities
A script to handle auto gun drops amongst other things

## Installation
1. Download Python: `https://www.python.org/downloads`
2. Edit `main.py` to change logLocation to your CSGO installation path.
Example: `D:\Games\steamapps\common\Counter-Strike Global Offensive\csgo`

## Usage
1. Enter `con_logfile "console.log"` into the CSGO console each time or into your autoexec config. (Restart CSGO if it is running)
2. Run the `start.bat` file each time you need to. (Pin to taskbar for easy access)

## Features
1. In Game AFK Controller
    - Use this when you need to go AFK while in a match. This feature ensures that you will not be automatically kicked for being AFK. It also enables your teammates to drop guns using your money. Instructions will be put into the chat so randoms will understand.  

2. Auto Match Accept Controller
    - Use this feature when you need to go AFK while searching for a game.

3. Auto Chat Translator
    - (BETA) Use this feature to automatically translate foreign chat into English. Useful if playing in a different region.

## Notes
This tool requires you to be tabbed into the game.
There is an option to delete the logfile through the tool. Use this occaisonly as otherwise the logfile size can get quite large.
This should work on Linux/Mac OS, however it has not been tested.