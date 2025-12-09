import time
from pynput.keyboard import Controller, Key
from pynput import mouse

# Keyboard controller for key events
keyboard = Controller()

# Define the functions for specific actions
def CtrlShiftRight():
    """Perform Ctrl + Shift + Right Arrow."""
    with keyboard.pressed(Key.ctrl):
        with keyboard.pressed(Key.shift):
            keyboard.press(Key.right)
            keyboard.release(Key.right)

def CtrlX():
    """Perform Ctrl + X (Cut)."""
    with keyboard.pressed(Key.ctrl):
        keyboard.press('x')
        keyboard.release('x')

def CtrlLeft():
    """Perform Ctrl + Left Arrow."""
    with keyboard.pressed(Key.ctrl):
        keyboard.press(Key.left)
        keyboard.release(Key.left)

def CtrlV():
    """Perform Ctrl + V (Paste)."""
    with keyboard.pressed(Key.ctrl):
        keyboard.press('v')
        keyboard.release('v')

def perform_actions():
    """Sequence of actions to automate."""
    print("Performing actions...")
    CtrlShiftRight()   # Ctrl + Shift + Right Arrow
    time.sleep(0.1)
    CtrlX()            # Ctrl + X
    time.sleep(0.1)
    keyboard.press(Key.down)  # Press Down Arrow
    keyboard.release(Key.down)
    time.sleep(0.1)
    CtrlLeft()         # Ctrl + Left Arrow
    time.sleep(0.1)
    CtrlV()            # Ctrl + V
    time.sleep(0.1)
    keyboard.press(Key.enter)  # Press Enter
    keyboard.release(Key.enter)
    time.sleep(0.5)

# Function to handle mouse clicks
def on_click(x, y, button, pressed):
    if pressed:  # Detects the press, not the release
        print("Mouse click detected, executing actions...")
        perform_actions()

# Setting up the mouse listener
print("Waiting for mouse clicks to execute actions...")
with mouse.Listener(on_click=on_click) as listener:
    listener.join()  # Keeps the listener active indefinitely