# --- Setup ---

import toml

# Import speech_recognition, pyttsx3, wikipedia, spotipy, and other sources
from dotenv import load_dotenv
import os
import spotipy
import json
import wikipedia
import webbrowser
import pyttsx3
from datetime import datetime
import speech_recognition as sr
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(
        index, name))

# Import dotenv
load_dotenv()

# Validate Spotify
username = os.environ.get('user_name')
clientID = os.environ.get('client_ID')
clientSecret = os.environ.get('client_secret')
redirect_uri = os.environ.get('redirect_uri')

oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()

# To print the response in readable format
print(json.dumps(user_name, indent=4, sort_keys=True))

# Speech engine initialization
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[11].id)
activationWord = 'computer'  # Single word

# Configure browser
# Set the path
firefox_path = r"/usr/bin/firefox"
webbrowser.register(
    'firefox', None, webbrowser.BackgroundBrowser(firefox_path))

# Configure Spotify
# Set the path
spotify_path = r"/usr/bin/spotify"
webbrowser.register(
    'spotify', None, webbrowser.BackgroundBrowser(spotify_path))

# Configure Steam
# Set the path
steam_path = r"/home/mashumelo/.steam/debian-installation/steam.sh"
webbrowser.register('steam', None, webbrowser.BackgroundBrowser(steam_path))

# Configure Discord
# Set the path
discord_path = r"/usr/bin/discord"
webbrowser.register(
    'discord', None, webbrowser.BackgroundBrowser(discord_path))


def speak(text, rate=120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()


def parseCommand():
    listener = sr.Recognizer()
    print('Listening for a command')

    with sr.Microphone() as source:
        listener.pause_threshhold = 2
        input_speech = listener.listen(source)

        try:
            print('Recognizing speech...')
            query = listener.recognize_google(input_speech, language='en_gb')
            print(f'The input speech was: {query}')
        except Exception as exception:
            print('I did not quite catch that')
            speak('I did not quite catch that')
            print(exception)
            return 'None'

        return query


def search_wikipedia(query=' '):
    searchResults = wikipedia.search(query)
    if not searchResults:
        print('No wikipedia result')
        return 'No result received'
    try:
        wikiPage = wikipedia.page(searchResults[0])
    except wikipedia.DisambiguationError as error:
        wikiPage = wikipedia.page(error.options[0])
    print(wikiPage.title)
    wikiSummary = str(wikiPage.summary)
    print(' ')
    print(wikiSummary)
    return wikiSummary


def listOrDict(var):
    if isinstance(var, list):
        return var[0]['plaintext']
    else:
        return var['plaintext']


# --- Main ---
if __name__ == '__main__':
    speak('All systems nominal.', 120)

    while True:
        # Parse as a list
        query = parseCommand().lower().split()

        if query[0] == activationWord:
            query.pop(0)

            # List commands
            if query[0] == 'say':
                if 'hello' in query:
                    speak('Greetings, all.')
                else:
                    query.pop(0)
                    speech = ' '.join(query)
                    speak(speech)

            # Navigation for browser
            if query[0] == 'go' and query[1] == 'to':
                speak('Opening...')
                query = ' '.join(query[2:])
                webbrowser.get('firefox').open_new(query)

            # Spotify application
            if query[0] == 'open' and query[1] == 'spotify':
                speak('Opening...')
                query = ' '.join(query[1:])
                webbrowser.get('spotify').open_new(query)

            # Spotify song search in browser
            if query[0] == 'play' and query[1] == 'spotify':
                speak('Opening...')
                query = ' '.join(query[3:])
                search_song = query.replace('play', '')
                results = spotifyObject.search(search_song, 1, 0, 'track')
                songs_dict = results['tracks']
                song_items = songs_dict['items']
                song = song_items[0]['external_urls']['spotify']
                webbrowser.open(song)
                print('Song has been opened.')
                speak('Song has been opened.')

            # Spotify pause playback
            if query[0] == 'pause' and query[1] == 'spotify':
                spotifyObject.pause_playback(query)

            # Spotify start playback
            if query[0] == 'resume' and query[1] == 'spotify':
                spotifyObject.start_playback(query)

            # Steam application
            if query[0] == 'open' and query[1] == 'steam':
                speak('Opening...')
                query = ' '.join(query[1:])
                webbrowser.get('steam').open_new(query)

            # Discord application
            if query[0] == 'open' and query[1] == 'discord':
                speak('Opening...')
                query = ' '.join(query[1:])
                webbrowser.get('discord').open_new(query)

            # Wikipedia
            if query[0] == 'wikipedia':
                query = ' '.join(query[1:])
                speak('Querying the universal databank.')
                speak(search_wikipedia(query))

            # Note taking
            if query[0] == 'log':
                speak('Ready to record your note')
                newNote = parseCommand().lower()
                now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
                with open('note_%.txt' % now, 'w') as newFile:
                    newFile.write(newNote)
                speak('Note written')

            if query[0] == 'exit':
                speak('Goodbye')
                break

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
    "pyttsx3",
    "wikipedia",
    "spotipy",
    "speech_recognition"
    }
}

with open('config.toml', 'w') as f:
    toml.dump(config_data, f)