# plexcsv# plexcsv

Foobar is a Python library for dealing with word pluralization.

## Overview
* This library makes it possible to create classic and smart music playlists in Plex using CSV files.
* It reduces the effort needed to build / rebuild  complex playlists, and allows automating those tasks.
* It also provides the ability to back up and share playlist criteria.


## Installation

```bash
pip install plexcsv
```

## Usage

* You can import the plexcsv library into your project, or build playlists instantly using the built-in CLI tool.

**Creating a playlist using the CLI:**
* The create command takes up to six arguments. Four of them mandatory.
* See the [wiki](https://github.com/swills1/plexcsv/wiki) for full details.
```bach
plexcsv create [-h] -t TYPE [-s SCOPE] -l LIBTYPE -T TITLE -p PATH
```

## License
[MIT](https://choosealicense.com/licenses/mit/)