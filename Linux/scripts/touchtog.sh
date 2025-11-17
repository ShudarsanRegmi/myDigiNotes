#!/bin/bash

# Automatically find the Touchpad ID
TOUCHPAD_ID=$(xinput list | grep -i "Touchpad" | grep -o 'id=[0-9]*' | cut -d= -f2)

# If the touchpad wasn't found, show an error and exit
if [ -z "$TOUCHPAD_ID" ]; then
    notify-send "Touchpad Toggle Error" "Could not find a Touchpad device."
    exit 1
fi

# File to track lock state
LOCK_STATE_FILE="$HOME/.touchpad_lock_state"

# Toggle the touchpad
if [ -f "$LOCK_STATE_FILE" ]; then
    xinput enable "$TOUCHPAD_ID"
    rm "$LOCK_STATE_FILE"
    notify-send "Touchpad Enabled" "Your touchpad is now active again."
else
    xinput disable "$TOUCHPAD_ID"
    touch "$LOCK_STATE_FILE"
    notify-send "Touchpad Disabled" "Touchpad input has been turned off."
fi

