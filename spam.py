import pyautogui
import time
from pynput import mouse

print("""
DDDDD   IIIIII  MMM   MMM  MMM   MMM  Y     Y
D    D    I     M  M M  M  M  M M  M   Y   Y 
D     D   I     M   M   M  M   M   M    Y Y  
D     D   I     M       M  M       M     Y   
D     D   I     M       M  M       M     Y   
D    D    I     M       M  M       M     Y   
DDDDD   IIIIII  M       M  M       M     Y   
""")

# Get input from user
text_to_write = input("Text to write: ")
repeat_count = int(input("Number of times to write the text: "))
current_count = 0

def on_click(x, y, button, pressed):
    global current_count
    if pressed:
        for _ in range(repeat_count):
            pyautogui.write(text_to_write)
            pyautogui.press('enter')
            time.sleep(0.1)
        current_count += 1

        if current_count >= 1:
            print("Text writing completed. Exiting...")
            return False
time.sleep(5)

# Start mouse listener
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
