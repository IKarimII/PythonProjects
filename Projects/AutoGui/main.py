import time
import pyautogui

# Open the application (example: Notepad)
pyautogui.press('win')  # Open the start menu
time.sleep(1)  # Wait for the start menu to open
pyautogui.typewrite('notepad')  # Type "notepad" to search for the Notepad application
time.sleep(1)  # Wait for the search results to appear
pyautogui.press('enter')  # Press Enter to open Notepad
time.sleep(2)  # Wait for Notepad to open

# Interact with the application
pyautogui.typewrite('YOU ARE THE GAYEST PERSON ALIVE ')  # Type "Hello, World!" in Notepad
time.sleep(3)  # Wait for the text to be typed
pyautogui.hotkey('ctrl', 's')  # Press Ctrl+S to save the file
time.sleep(1)  # Wait for the save dialog to appear
pyautogui.typewrite('gaynessover9000.txt')  # Type the file name
time.sleep(1)  # Wait for the file name to be typed
pyautogui.press('enter')  # Press Enter to save the file
time.sleep(1)  # Wait for the file to be saved

# Close the application
pyautogui.hotkey('alt', 'f4')  # Press Alt+F4 to close the application