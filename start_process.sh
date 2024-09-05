#!/bin/bash

BASE_DIR=$(pwd)
# Check if tmux is installed
if ! command -v tmux &> /dev/null
then
    echo "tmux could not be found. Please install tmux to continue."
    exit 1
fi

# Activate conda environment
if command -v conda &> /dev/null; then
    echo "Activating conda environment 'iot-automation'..."
    eval "$(conda shell.bash hook)"
    conda activate iot-automation
else
    echo "Conda is not installed or not in PATH. Please install Conda or add it to your PATH."
    exit 1
fi


# Check if the session already exists
if tmux has-session -t "scraper" 2>/dev/null; then
    echo "Session 'scraper' already exists. Attaching to it."
    tmux attach-session -t "scraper"
else
    echo "Session 'scraper' does not exist. Creating a new session."

    # Create a new tmux session named "scraper"
    tmux new-session -d -s "scraper"

    # Create a window for running the Python script
    tmux send-keys -t "scraper:0" "cd $BASE_DIR" C-m
    tmux send-keys -t "scraper:0" "python3 main.selenium.py" C-m

    # Attach to the session
    tmux attach-session -t "scraper"
fi
