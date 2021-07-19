import argparse
import os, sys
from plexcsv import create_playlist

def playlist_type(args):
    if args.type not in ('s','c', 'smart', 'classic'):
        print('type must be s or c - (s)mart (c)lassic')
    elif  args.type in ('s', 'smart'):
        return create_playlist.create_smart_playlist(args.title, args.libtype, args.path, args.scope)
    elif  args.type in ('c', 'classic'):
        return create_playlist.create_classic_playlist(args.title, args.libtype,  args.path)

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

create_parser = subparsers.add_parser('create')
create_parser_required = create_parser.add_argument_group('required arguments')
create_parser.set_defaults(func=playlist_type)
create_parser_required.add_argument('-t', '--type', dest='type', help='playlist type - options: c, classic, s, smart', required=True)
create_parser.add_argument('-s', '--scope', dest='scope', default='any', help='match any or all - default: any - options: any, all')
create_parser_required.add_argument('-l', '--libtype', dest='libtype', help='library type - options: artist, album, track', required=True)
create_parser_required.add_argument('-T', '--title', dest='title', help='playlist title', required=True)
create_parser_required.add_argument('-p', '--path', dest='path', help='CSV file path', required=True)

args = parser.parse_args()
args.func(args)
