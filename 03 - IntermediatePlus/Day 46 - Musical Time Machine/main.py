import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv("../../.env")

SPOTIFY_CLIENT_ID = os.getenv("CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("CLIENT_SECRET")

URL = "https://www.billboard.com/charts/hot-100"  # Scrap data from billboard with the preferred date

preferred_date = input("Which year you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"{URL}/{preferred_date}")
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")  # created the soup to start scrapping data

songs = soup.select("li ul li h3")  # Selecting only the song titles, a way to approach
song_names = [song.get_text().strip() for song in songs]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
    )
)

user_id = sp.current_user()["id"]


song_uris = []
year = preferred_date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

print(song_uris)

playlist = sp.user_playlist_create(user=user_id, name=f"{preferred_date} BillBoard 100", public=False,
                                   collaborative=False)
playlist_id = playlist["id"]

sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)
