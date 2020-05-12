# Zoom-desktop-control-reverse-shell

This project was for a Special Course in Information Security at Aalto university. The goal of the project was to find weaknesses in Zooms desktop control feature. The script represented in this repo can open a reverse shell to the attackers machine if the victim has granted the attacker control to his desktop over Zoom. This script exploits Zooms lack of input sanitation from machine to machine.

The goal of the script is to open a terminal window on the victims machine through Spotlight (Only for macOS). In the terminal window, the attacker would then open a reverse shell to his/hers machine and gain access to the victims machine with the priviliges of the current victims user. The script automates this using Python. This way the foothold on the victims machine can be established as fast as possible.

## How to use

In a Zoom meeting, ask the victim to give you remote control of his/hers desktop. When you have controll of the desktop, open a listener on a port of your choise, e.g. 4444:

```sh
nc -nvl 4444
```

Then run the Python script to automate your input and moove back to the victims desktop:

```sh
python set-reverse-shell-mac.py
```

When the Python script is ready, you should see a reverse shell appers in the terminal window where you have the listner.

## Discalimer

The information and material in this repository is intended for educational perposes ONLY. I do not take responsibility for any matters regarding the scrip presented.
