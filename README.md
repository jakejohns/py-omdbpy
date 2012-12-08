omdbpy
======

Really simple python wrapper OMDb ( http://www.omdbapi.com/ )

Includes a simple command line interface

- Search for movies
- Display movie information (based on title or imdb id)

## Usage

## Commandline 

    # search for movie
    $ omdbpy search "blade run*"

    # display movie information based on title
    $ omdbpy title "blade runner"

    # display movie information base don imdb id
    $ omdbpy imdbid tt0083658

There is a paramter to specify a year (eg. "-y 1982").
There is the option to include rotten tomatoes info, but its slower (eg. "-t")
There is the option to include longer plot summaries (eg. "-p")

see --help for more.

## Python

    import omdb.service

    omdb = omdb.service.omdb_api()
    results = omdb.search('blade runner')


# todo
- make more formatters for commandline output
- actually include tomatoes data in output
- write real documentation or something



