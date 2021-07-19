import pandas as pd
import numpy as np
from plexapi.server import PlexServer
from config import baseurl, token

plex = PlexServer(baseurl, token)

def create_classic_playlist (title, libtype, path):
    """create classic playlist"""

    dataframe = pd.read_csv(path)
    dataframe_nan = dataframe.replace(np.nan, '', regex=True)
    playlist_items = []

    for i, row in enumerate(dataframe_nan.itertuples(index=False), 1):
        if(not row.artist): artist_filter = ""
        else: artist_filter = row.artist

        if(not row.album): album_filter = ""
        else: album_filter = row.album

        if(not row.track): track_filter = ""
        else: track_filter = row.track

        artist_filter_key = "artist.title" + row.artistop
        album_filter_key = "album.title" + row.albumop
        track_filter_key = "track.title" + row.trackop

        playlist_search = plex.library.section('Music').search(filters={artist_filter_key: artist_filter, album_filter_key: album_filter, track_filter_key: track_filter}, libtype=libtype)
        playlist_items += playlist_search

    playlist_all_items = playlist_items
    plex.createPlaylist(title, items=playlist_all_items)


def create_smart_playlist (title, libtype, path, scope='any'):
    """create smart playlist"""

    playlist_series = pd.read_csv(
        path,
        header=None,
        names=['key', 'value'],
        index_col=['key'],
        squeeze=True,
    )

    playlist_dict = [{key: value} for key, value in playlist_series.items()]
    filter_scope = {}

    if scope=='all':
        filter_scope = {'and': playlist_dict}
    elif scope=='any':
        filter_scope = {'or': playlist_dict}

    plex.createPlaylist(title, libtype=libtype, smart=True, section='Music', filters=filter_scope)
    print(filter_scope)


