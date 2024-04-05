import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

def get_playlist_tracks(playlist_id):
    # Define your Spotify client credentials
    client_id = "09cfdea368b64101b4c4fcc3508ab23f"
    client_secret = "44a2130e4810455eb08c6a265e54e84c"
    redirect_uri = 'http://localhost:8000/callback'

    # Create a Spotify client instance with authorization and custom cache
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope='playlist-modify-public'))

    # Retrieve the playlist tracks
    tracks = sp.playlist_tracks(playlist_id)

    # Extract track names and artists from the response
    track_info = []
    for item in tracks['items']:
        track = item['track']
        track_name = track['name']
        artists = ", ".join([artist['name'] for artist in track['artists']])
        track_info.append(f"{track_name} ~ {artists}")

    return track_info

# Enter your playlist ID here
playlist_id = input("Input a playlist uri.\n")

# Get the track names and artists from the playlist
track_info = get_playlist_tracks(playlist_id)

# Print the track names and artists on one line
for info in track_info:
    print(info)