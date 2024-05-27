import pyautogui
import time

print("""
DDDDD   IIIIII  MMM   MMM  MMM   MMM  Y     Y
D    D    I     M  M M  M  M  M M  M   Y   Y 
D     D   I     M   M   M  M   M   M    Y Y  
D     D   I     M       M  M       M     Y   
D     D   I     M       M  M       M     Y   
D    D    I     M       M  M       M     Y   
DDDDD   IIIIII  M       M  M       M     Y   
""")

# Define the text and the number of times to write it
text_to_write = input("Text to write: ")
repeat_count = int(input("Number of times to write the text: "))
current_count = 0

def on_click(x, y, button, pressed):
    if pressed:
        for _ in range(repeat_count):
            pyautogui.write(text_to_write)
            pyautogui.press('enter')
            time.sleep(0.1)  # Small delay to ensure text is written properly
        current_count += 1
    
        if current_count >= repeat_count:
            # Close the program after printing the text repeat_count times
            print("Closing the program ...")
            return False  # Stop the listener and close the program

# Use pyautogui's mouse event listener
from pynput import mouse

# Create an instance of Listener and assign the on_click function to handle click events
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
    
