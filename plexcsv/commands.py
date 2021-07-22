import os, sys
import argparse
import dotenv
from plexcsv import playlist

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

def config_path(args):
    if args.show:
        print(os.environ['FILE_PATH']) 
    elif args.path:
        os.environ['FILE_PATH'] = args.path
        dotenv.set_key(dotenv_file, 'FILE_PATH', os.environ['FILE_PATH'])

def playlist_type(args):
    if args.type not in ('s','c', 'smart', 'classic'):
        print('type must be s or c - (s)mart (c)lassic')
    elif  args.type in ('s', 'smart'):
        return playlist.create_smart_playlist(args.title, args.libtype, args.path, args.scope)
    elif  args.type in ('c', 'classic'):
        return playlist.create_classic_playlist(args.title, args.libtype,  args.path)

def main():
    #main parser
    parent_parser = argparse.ArgumentParser()
    subparsers = parent_parser.add_subparsers()

    #config sub-command
    config_parser = subparsers.add_parser('config')
    #config_parser_required = config_parser.add_argument_group('required arguments')
    config_parser.set_defaults(func=config_path)
    config_parser.add_argument('--show', help='show current config file path - takes no input', action='store_true')
    config_parser.add_argument('--update', help='modify config file path', dest='path')

    #create sub-command
    create_parser = subparsers.add_parser('create')
    create_parser_required = create_parser.add_argument_group('required arguments')
    create_parser.set_defaults(func=playlist_type)
    create_parser_required.add_argument('--type', dest='type', help='playlist type - options: c, classic, s, smart', required=True)
    create_parser.add_argument('--scope', dest='scope', default='any', help='match any or all - default: any - options: any, all')
    create_parser_required.add_argument('--libtype', dest='libtype', help='library type - options: artist, album, track', required=True)
    create_parser_required.add_argument('--title', dest='title', help='playlist title', required=True)
    create_parser_required.add_argument('--path', dest='path', help='csv file path', required=True)

    args = parent_parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()