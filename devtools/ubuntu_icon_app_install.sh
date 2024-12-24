#!/bin/bash

# Variables
PYCHARM_BIN_PATH="/home/aparichit/Apps/pycharm-2024.3.1.1/bin"
DESKTOP_ENTRY_PATH="$HOME/.local/share/applications/pycharm.desktop"
LOG_FILE="pycharm_setup.log"
ICON_PATH_SVG="$PYCHARM_BIN_PATH/pycharm.svg"
ICON_PATH_PNG="$PYCHARM_BIN_PATH/pycharm.png"

# Logging function
log_message() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

log_message "Starting PyCharm setup script."

# Check if PyCharm bin path exists
if [ -d "$PYCHARM_BIN_PATH" ]; then
    log_message "PyCharm bin path exists: $PYCHARM_BIN_PATH"
else
    log_message "Error: PyCharm bin path does not exist: $PYCHARM_BIN_PATH"
    exit 1
fi

# Add PyCharm to PATH in .bashrc
if grep -q "$PYCHARM_BIN_PATH" ~/.bashrc; then
    log_message "PyCharm bin path is already added to PATH."
else
    echo "export PATH=\"$PYCHARM_BIN_PATH:\$PATH\"" >> ~/.bashrc
    log_message "Added PyCharm bin path to PATH in ~/.bashrc."
    source ~/.bashrc
    log_message "Reloaded ~/.bashrc."
fi

# Create desktop entry
log_message "Creating desktop entry for PyCharm."
cat > "$DESKTOP_ENTRY_PATH" <<EOL
[Desktop Entry]
Type=Application
Name=PyCharm
Exec="$PYCHARM_BIN_PATH/pycharm.sh" %f
Icon=${ICON_PATH_PNG:-${ICON_PATH_SVG}}
Terminal=false
Categories=Development;IDE;
EOL

if [ -f "$DESKTOP_ENTRY_PATH" ]; then
    log_message "Desktop entry created at: $DESKTOP_ENTRY_PATH"
else
    log_message "Error: Failed to create desktop entry."
    exit 1
fi

# Check for icons and validate
if [ -f "$ICON_PATH_SVG" ]; then
    log_message "SVG Icon found: $ICON_PATH_SVG"
elif [ -f "$ICON_PATH_PNG" ]; then
    log_message "PNG Icon found: $ICON_PATH_PNG"
else
    log_message "Error: No valid icon file found in the bin directory."
    exit 1
fi

log_message "Making the desktop entry executable."
chmod +x "$DESKTOP_ENTRY_PATH"

log_message "Updating desktop database."
update-desktop-database ~/.local/share/applications/

log_message "Setup complete. PyCharm is ready to use."
echo "Please restart your terminal or source ~/.bashrc for PATH changes to take effect."
