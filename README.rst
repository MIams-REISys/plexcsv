plexcsv
=======

Overview
--------

* This library makes it possible to create classic and smart music playlists in Plex using CSV files.
* It reduces the effort needed to build / rebuild  complex playlists, and allows automating those tasks.
* It also provides the ability to back up and share playlist criteria.


Install
-------

``pip install plexcsv``

Usage
-----

* You can import the plexcsv library into your project, or build playlists instantly using the built-in CLI tool.

**Creating a playlist using the CLI:**

* The create command takes up to six arguments. Four of them mandatory.
* See the `wiki`_ for full details.

.. _wiki: https://github.com/swills1/plexcsv/wiki

``plexcsv create [-h] -t TYPE [-s SCOPE] -l LIBTYPE -T TITLE -p PATH``
