#!/bin/bash

BASE_DIR=$(pwd)
# Check if tmux is installed
if ! command -v tmux &> /dev/null
then
    echo "tmux could not be found. Please install tmux to continue."
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

    # Activate conda environment and run the Python script
    tmux send-keys -t "scraper:0" "cd $BASE_DIR" C-m
    tmux send-keys -t "scraper:0" "if command -v conda &> /dev/null; then" C-m
    tmux send-keys -t "scraper:0" "    echo \"Activating conda environment 'iot-automation'...\"" C-m
    tmux send-keys -t "scraper:0" "    eval \"\$(conda shell.bash hook)\"" C-m
    tmux send-keys -t "scraper:0" "    conda activate iot-automation" C-m
    tmux send-keys -t "scraper:0" "    python3 main.selenium.py" C-m
    tmux send-keys -t "scraper:0" "else" C-m
    tmux send-keys -t "scraper:0" "    echo \"Conda is not installed or not in PATH. Please install Conda or add it to your PATH.\"" C-m
    tmux send-keys -t "scraper:0" "    exit 1" C-m
    tmux send-keys -t "scraper:0" "fi" C-m

    # Attach to the session
    tmux attach-session -t "scraper"
fi
