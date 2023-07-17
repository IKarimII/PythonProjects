import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


date = input("Enter a date: YYYY-MM-DD")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
file = response.text

soup = BeautifulSoup(file, 'html.parser')

song_titles = soup.select('ul li ul h3')

songs_list = [songs.getText().strip() for songs in song_titles]
print(songs_list)

Spotify_client_id = '8ea9509b799d4325a9590de58ab4bf11'
Spotify_secret = '46332bdbca0548b49d12c5d082b0fda8'

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=Spotify_client_id,
        client_secret=Spotify_secret,
        show_dialog=True,
        cache_path="token.txt"
    ))

user_id = sp.current_user()["id"]

song_uris = []
for song in songs_list:
    result = sp.search(q=f"track:{song} ", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user_id, f"Top 100 {date}", public=False, description=f'Playlist of the 100 best songs of {date}, presented to you by Karim')

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)