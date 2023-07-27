import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser

client_id = "ae798d1560374cfba622c0526ed07c89"
client_secret = "cbfd29c9409f492ca44765972f369917"
redirect_uri = "http://localhost:8888/callback"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope="user-read-playback-state playlist-modify-public",
    )
)


current_playback = sp.current_playback()

if current_playback is not None:
    artist = current_playback["item"]["artists"][0]["name"]
    track_name = current_playback["item"]["name"]
    album = current_playback["item"]["album"]["name"]
    # print(f"Currently playing: {track_name} by {artist} from the album {album}")

    # add to playlist
    song_name = f'{track_name}" "{artist}'
    results = sp.search(song_name, type="track")
    track_uri_here = results["tracks"]["items"][0]["uri"]

    playlist_id = "7mwS6iSBxq6oxjVuA9gFAw"
    track_uri = f"{track_uri_here}"

    sp.playlist_add_items(playlist_id, [track_uri])

else:
    webbrowser.open("D:/College/Portfolio/animated-404-page/index.html")
