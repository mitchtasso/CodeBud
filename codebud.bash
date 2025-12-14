#!/bin/bash

# Define variables
FILE_NAME="codebud"
DOWNLOAD_URL="https://raw.githubusercontent.com/mitchtasso/CodeBud/refs/heads/main/codebud"
DEST_PATH="/usr/local/bin/$FILE_NAME"

# Download the file
curl -L -o "$FILE_NAME" "$DOWNLOAD_URL"

# Make it executable
chmod +x "$FILE_NAME"

# Move it to /usr/local/bin (requires sudo)
sudo mv "$FILE_NAME" "$DEST_PATH"

echo "codebud downloaded and installed to $DEST_PATH"
echo "run the 'codebud --help' command to start"
