#!/bin/bash

# Automatically find the keyboard ID for "AT Translated Set 2 keyboard"
KEYBOARD_ID=$(xinput list | grep -i "AT Translated Set 2 keyboard" | grep -o 'id=[0-9]*' | cut -d= -f2)

# If the keyboard wasn't found, show an error and exit
if [ -z "$KEYBOARD_ID" ]; then
    notify-send "Keyboard Toggle Error" "Could not find 'AT Translated Set 2 keyboard'."
    exit 1
fi

# File to track lock state
LOCK_STATE_FILE="$HOME/.keyboard_lock_state"

# Toggle the keyboard
if [ -f "$LOCK_STATE_FILE" ]; then
    xinput enable "$KEYBOARD_ID"
    rm "$LOCK_STATE_FILE"
    notify-send "Keyboard Unlocked" "Your keyboard is now active again."
else
    xinput disable "$KEYBOARD_ID"
    touch "$LOCK_STATE_FILE"
    notify-send "Keyboard Locked" "Keyboard input has been disabled."
fi

