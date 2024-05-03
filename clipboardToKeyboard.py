# This script is used to write your clipboard to a keypress
# Useful for writing to say a web VM where you cannot paste your password if you use a password manager

def handle_keypress():
    # this function handles to the key press event
    
    # Get clipboard
    text_to_Written = pyperclip.paste()
    
    # Write text wtih a delay if there some input lag
    keyboard.write(text_to_Written,  delay=0.02, restore_state_after=False) 
    text_to_Written = "" # clear variable

# require pyperclip and keyboard

import keyboard
import pyperclip

# hook onto a combination of keypress
hook = keyboard.add_hotkey('alt+ctrl+v', lambda: handle_keypress())

# prevent program from closing until esc key is pressed, then clear the hook
keyboard.wait('esc')
keyboard.unhook(hook)