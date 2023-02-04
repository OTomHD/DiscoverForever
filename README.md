# DiscoverForever
Python Script to copy one playlist into another from spotify

Set up as a cron job that runs weekly to add my Discover Weekly playlist to my DiscoverForever Playlist

Uses spotipy

``` pip install configparser ```
``` pip install spotipy ```


# Templete config file

create file ``` .config.ini ```

copy and fill in
```
[CLIENT]
id = <CLIENT_ID>
secret = <CLIENT_SECRET>
redirURL = http://localhost:8888/

[USER]
week = <FROM_PLAYLIST_ID>
Forever = <TO_PLAYLIST_ID>
```
