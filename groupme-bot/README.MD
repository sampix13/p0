# Project Name

A brief description of your project.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

List the new features you added to your code here. Provide a brief description of each feature and explain how it enhances the functionality of your project.

### Bot Responds Only to Author

The bot has been updated to respond only to messages from the author. This ensures that the bot's responses are directed specifically to me and it doesn't respond to other group members messages

### Good Morning and Good Night Messages

The bot has the ability to respond to 'good morning' and 'good night', responding with good morning/night <MY NAME> 

### Joke Feature

The bot can now tell you a joke upon request. Simply send a message to the bot with the command "tell me a joke" and it will respond with a funny joke. This feature adds a fun and entertaining element to your interactions with the bot.

## Installation and Setup

To create virtual environment and install dependencies: 
``` 
    python3 -m venv venv

    # activate virtual environment
    source venv/bin/activate # for mac/linux
    venv\Scripts\activate # for windows


    # install dependencies
    pip install -r requirements.txt
```

To make the bot respond to you, create a .env file and include the following: 
```
    BOT_ID=""
    GROUP_ID=""
    ACCESS_TOKEN=""
    MY_SENDER_ID = ""
```

## Usage

To run the script and have the bot respond to you and only you, follow these steps:
1. Open the terminal and navigate to the project directory.
2. Run the commands:  
```
# Activate virtual environment
source venv/bin/activate #for mac/linux
venv\Scripts\activate # for windows

# Run bot
python3 bot.py
```
3. Send a message in the GroupMe chat containing one of the commands.
4. The bot will respond to your message, but not to messages from others.
