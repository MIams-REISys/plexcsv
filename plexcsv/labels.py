import os
import re
import pandas as pd
from plexapi.server import PlexServer
from dotenv import load_dotenv

load_dotenv()
MY_ENV_VAR = os.getenv('PLEXAPI_CONFIG_PATH')
plex = PlexServer()

def export_album_data(path):
    album_list = []
    all_albums = plex.library.section('Music')
    for album in all_albums.search(libtype='album'):
        album_labels = str(album.labels)[1:-1]
        album_list.append((album.parentTitle,album.title,album.year,album_labels))

    my_df = pd.DataFrame(album_list, columns=('Artist', 'Album', 'ReleaseYear', 'Labels'))
    my_df.to_csv(path, index=False)

export_album_data('/home/steven/Projects/plexcsv/plexcsv_dev/plexcsv/labelf.csv')
