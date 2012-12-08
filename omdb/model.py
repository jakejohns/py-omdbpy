#!/usr/bin/env python

# this fileis part of omdbpy
# 
# Copyright 2012 Jake Johns <jake@jakejohns.net>.
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 
# File: model.py
# Author: Jake Johns <jake@jakejohns.net>
# Description: 
# Created: 2012-10-23
# Modified: 2012-12-07  21:58



class omdb_error:
    """
    Basic error type to return
    """

    def __init__(self, data):
        """
        Store error message
        """
        self.message = data['Error']


class search_result:
    """
    Represents an entry returned from search 
    """

    def __init__(self, raw_data):
        """
        Loads data from response
        """
        data = {}
        for key, value in raw_data.items():
            data[key.encode('utf8')] = value.encode('utf-8')

        self.imdbid = data['imdbID']
        self.year = data['Year']
        self.title = data['Title']


class omdb_tomato_data:

    def __init__(self, data):
        self.meter = data['tomatoMeter']
        self.user_rating = data['tomatoUserRating']
        self.fresh = data['tomatoFresh']
        self.rotten = data['tomatoRotten']
        self.consensus = data['tomatoConsensus']
        self.user_reviews = data['tomatoUserReviews']
        self.user_meter = data['tomatoUserMeter']
        self.reviews = data['tomatoReviews']
        self.rating = data['tomatoRating']
        self.image = data['tomatoImage']


class omdb_movie:
    """
    Repersents a full fledged movie entry
    """

    def __init__(self, raw_data, plot=None, tomato=None):

        data = {}
        for key, value in raw_data.items():
            data[key.encode('utf8')] = value.encode('utf-8')


        self.imdbid = data['imdbID']
        self.title = data['Title']
        self.year = data['Year']
        self.released = data['Released']
        self.mpaa_rating = data['Rated']
        self.writers = data['Writer'].split(',')
        self.directors = data['Director'].split(',')
        self.actors = data['Actors'].split(',')
        self.imdb_votes = data['imdbVotes']
        self.poster_url = data['Poster']
        self.genres = data['Genre'].split(',')
        self.imdb_rating = data['imdbRating']
        self.runtime = data['Runtime']


        if plot:
            self.plot_full = data['Plot']
            self.plot_short = None
        else:
            self.plot_full = None
            self.plot_short = data['Plot']

        if tomato:
            self.tomato = omdb_tomato_data(data)
        else:
            self.tomato = None
        
    def get_plot(self):
        if self.plot_full:
            return self.plot_full
        else:
            return self.plot_short
    








