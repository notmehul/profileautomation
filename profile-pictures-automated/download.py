import webbrowser
from pynput.keyboard import Controller, Key
import time

def process_links(input_file):
    with open(input_file, 'r') as file:
        links = file.readlines()

    for link in links:
        link = link.strip()  # Remove leading/trailing whitespaces and newlines
        webbrowser.open_new_tab(link)
        time.sleep(2)
        press_cmd_s()
        print(f"Opened: {link}")
        time.sleep(2)  # Wait for 3 seconds before closing the tab
        press_cmd_w()
        time.sleep(1)
        
def press_cmd_s():
    keyboard = Controller()
    keyboard.press(Key.cmd)
    keyboard.press('s')
    keyboard.release('s')
    keyboard.release(Key.cmd)
    print("Pressed cmd + s")

def press_cmd_w():
    keyboard = Controller()
    keyboard.press(Key.cmd)
    keyboard.press('w')
    keyboard.release('w')
    keyboard.release(Key.cmd)
    print("Pressed cmd + w")
    
input_file = 'input.txt'  # Replace with your input file containing Google Drive links
process_links(input_file)