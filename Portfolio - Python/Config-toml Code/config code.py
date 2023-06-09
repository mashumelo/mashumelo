# mashbot.py
# Exports config.toml
config_data = {
    "information": {
    "name": "Mashbot",
    "authors": "Waylon Neal [<93296689+mashumelo@users.noreply.github.com>]",
    "version": "0.0.5",
    "description": "Mashumelo's personal Discord bot",
    "readme": "README.md",
    "website": "https://github.com/mashumelo/mashumelo",
    },              
    "config": {
        "embedColour": 0x00ff00,
        "command_prefix": "!",
        "limit": 10
    },
    "dependencies": {
        "discord.py": "1.7.2",
        "giphy_client": "3.0.0",
        "toml": "0.10.2"
    }
}

with open("config.toml", "w") as f:
    toml.dump(config_data, f)

# adventure(demo).py
# Exports config.toml
config_data = {
    "information": {
        "name": "Adventure Game Demo",
        "authors": "Waylon Neal [<93296689+mashumelo@users.noreply.github.com>]",
        "version": "1.0.0",
        "description": "Simple text adventure game demo",
        "readme": "README.md",
        "website": "https://github.com/mashumelo/mashumelo",
    }}

with open("config.toml", "w") as f:
    toml.dump(config_data, f)

# calculator.py
# Exports config.toml
config_data = {
    "information": {
        "name": "Calculator",
        "authors": "Waylon Neal [<93296689+mashumelo@users.noreply.github.com>]",
        "version": "1.0.0",
        "description": "Simple calculator",
        "readme": "README.md",
        "website": "https://github.com/mashumelo/mashumelo",
    }}

with open("config.toml", "w") as f:
    toml.dump(config_data, f)

# assistant.py
# Exports config.toml
config_data = {
    "information": {
    "name": "AI Assistant",
    "authors": "Waylon Neal [<93296689+mashumelo@users.noreply.github.com>]",
    "version": "0.0.5",
    "description": "Mashumelo's personal AI Assistant",
    "readme": "README.md",
    "website": "https://github.com/mashumelo/mashumelo",
    },
    "config": {
    "activation_word": "computer",
    "firefox_path": "/usr/bin/firefox",
    "spotify_path": "/usr/bin/spotify",
    "steam_path": "/home/mashumelo/.steam/debian-installation/steam.sh",
    "discord_path": "/usr/bin/discord",
    "voice": 11,
    "rate": 120
    },
    "dependencies": {
    "pyttsx3": "2.90.0",
    "wikipedia": "1.4.0",
    "spotipy": "2.23.0",
    "speech_recognition": "3.10.0"
    }
}

with open('config.toml', 'w') as f:
    toml.dump(config_data, f)