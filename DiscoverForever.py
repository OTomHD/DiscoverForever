import configparser
import spotipy
from spotipy.oauth2 import SpotifyOAuth

config = configparser.ConfigParser()
config.read(".config.ini")

CLIENT_ID = config.get("CLIENT", "id")
CLIENT_SECRET = config.get("CLIENT","secret")
REDIRECT_URL = config.get("CLIENT", "redirURL")
scope = "playlist-read-private playlist-modify-private playlist-modify-public playlist-read-collaborative"

DiscoverWeekly = config.get("USER", "Week")
DiscoverForever = config.get("USER","Forever")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URL,
                                               scope=scope))
inputplaylist = sp.playlist_tracks(DiscoverWeekly)

tracks = []

for idx, item in enumerate(inputplaylist['items']):
    track = item['track']
    print(track["name"])
    tracks.append(track["uri"])

sp.playlist_add_items(DiscoverForever, tracks)