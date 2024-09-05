# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies, Chrome, and ChromeDriver
RUN apt-get update && apt-get install -y \
    gnupg tmux unzip wget \
    && rm -rf /var/lib/apt/lists/*

ADD https://dl-ssl.google.com/linux/linux_signing_key.pub /tmp/google_signing_key.pub
RUN apt-key add /tmp/google_signing_key.pub \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.pip.txt

# Create a volume to persist the entire app directory
VOLUME ["/app"]

# Create a script to check for tmux and run the Python script
RUN echo '#!/bin/bash\n\
    if ! command -v tmux &> /dev/null; then\n\
    apt-get update && apt-get install -y tmux && rm -rf /var/lib/apt/lists/*\n\
    fi\n\
    tmux new-session -d "python main.selenium.py"\n\
    tmux attach-session' > /app/start.sh && chmod +x /app/start.sh

# Run the start script
CMD ["/app/start.sh"]


