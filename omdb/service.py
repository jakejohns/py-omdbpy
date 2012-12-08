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
# File: flick
# Author: Jake Johns <jake@jakejohns.net>
# Description: 
# Created: 2012-10-23
# Modified: 2012-12-07  21:19


import urllib, urllib2
import json
import omdb.model


    

class omdb_api:
    """
    Simple wraper for OMDB Api
    """


    def __init__(self):
        """
        Configure the basic settings
        """
        self.API_ROOT = 'http://www.omdbapi.com/'
        self.KEY_SEARCH = 's'
        self.KEY_YEAR = 'y'
        self.KEY_TITLE = 't'
        self.KEY_IMDBID = 'i'
        self.KEY_PLOT = 'plot'
        self.KEY_TOMATOES = 'tomatoes'
        self.VALUE_PLOTFULL = 'full'
        self.VALUE_TOMATOES = 'true'


    def _request(self, values):
        """
        Makes a request to omdb based on a dictionary of values
        """
        data = urllib.urlencode(values)
        request = urllib2.Request(self.API_ROOT + '?' + data)
        response = urllib2.urlopen(request)
        response_body = response.read()
        response_dict = json.loads(response_body)
        return response_dict

    def _movie(self, data, plot=None, tomatoes=None):
        """
        Creates a movie object from the response data
        """
        return omdb.model.omdb_movie(data)


    def search(self, query, year=None):
        """
        Searches for a movie title, and returns search results in a list. Search
        results are not full fledged movie entries
        """
        values = {}
        values[self.KEY_SEARCH] = query
        if year:
            values[self.KEY_YEAR] = year
        data =  self._request(values)

        if 'Error' in data:
            result = omdb.model.omdb_error(data)
        elif 'Search' in data:
            result = []
            for item in data['Search']:
                result.append(omdb.model.search_result(item))
        else:
            raise Exception('Invalid response from omdb!')

        return result


    def title(self, title, year=None, plot=None, tomatoes=None):
        """
        Takes a title and returns a movie object 
        """
        values = {}
        values[self.KEY_TITLE] = title
        if year:
            values[self.KEY_YEAR] = year
        if plot:
            values[self.KEY_PLOT] = self.VALUE_PLOTFULL
        if tomatoes:
            values[self.KEY_TOMATOES] = self.VALUE_TOMATOES

        data = self._request(values)

        if 'Response' in data:
            if data['Response'] == 'True':
                return self._movie(data, plot, tomatoes)
            else:
                return omdb.model.omdb_error(data)
        else:
            raise Exception('Invalid response from omdb!')


    def imdbid(self, imdbid, plot=None, tomatoes=None):
        """
        Takes an IMDBid and returns a movie object
        """
        values = {}
        values[self.KEY_IMDBID] = imdbid
        if plot:
            values[self.KEY_PLOT] = self.VALUE_PLOTFULL
        if tomatoes:
            values[self.KEY_TOMATOES] = self.VALUE_TOMATOES

        data =  self._request(values)

        if 'Response' in data:
            if data['Response'] == 'True':
                return self._movie(data, plot, tomatoes)
            else:
                return omdb.model.omdb_error(data)
        else:
            raise Exception('Invalid response from omdb!')


        








