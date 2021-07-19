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

* See `wiki`_ for full details.

.. _wiki: https://github.com/swills1/plexcsv/wiki

* The create command takes five main arguments. Four of them mandatory.

``plexcsv create [-h] -t TYPE [-s SCOPE] -l LIBTYPE -T TITLE -p PATH``

The library supports using list operators such as contains, does not contain, is, is not, begins with, ends with.

Current Limitations
-------------------
* Currently, the library only supports Artist, Album, and Track as filters. 
* Does not Currently support setting the playlist sort.
* Does not support nested rule groups.

There are plans to add these items. Sort being number 1.
