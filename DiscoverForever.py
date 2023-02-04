import configparser
import spotipy
from spotipy.oauth2 import SpotifyOAuth


try:
    config = configparser.ConfigParser()
    config.read(".config.ini")

    CLIENT_ID = config.get("CLIENT", "id")
    CLIENT_SECRET = config.get("CLIENT","secret")
    REDIRECT_URL = config.get("CLIENT", "redirURL")
    
    DiscoverWeekly = config.get("USER", "Week")
    DiscoverForever = config.get("USER","Forever")
except:
    print("Missing config details please enter details")
    print("And save as .config.ini next to the script")
    print("[CLIENT]\nid = <CLIENT_ID>\nsecret = <CLIENT_SECRET>\nredirURL = http://localhost:8888/\n\n[USER]\nweek = <FROM_PLAYLIST_ID>\nForever = <TO_PLAYLIST_ID>\n")
    exit()


scope = "playlist-read-private playlist-modify-private playlist-modify-public playlist-read-collaborative"
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