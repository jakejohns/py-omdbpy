#!/usr/bin/env python

# this fileis part of omdb
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
# File: formatter.py
# Author: Jake Johns <jake@jakejohns.net>
# Description: 
# Created: 2012-10-23
# Modified: 2012-12-07  21:58

import sys

class abstract_formatter:
    """
    abstract formatter for cli interface
    """
    
    def error(self, result):
        raise NotImplementedError( "Should have implemented this" )

    def search_results(self, result):
        raise NotImplementedError( "Should have implemented this" )

    def movie(self, result):
        raise NotImplementedError( "Should have implemented this" )


class debug_formatter(abstract_formatter):
    """
    Semi useless debug formatter
    """

    def error(self, result):
        print result

    def search_results(self, result):
        print result

    def movie(self, result):
        print result


class json_formatter(abstract_formatter):

    def error(self, result):
        raise NotImplementedError( "Should have implemented this" )

    def search_results(self, result):
        raise NotImplementedError( "Should have implemented this" )

    def movie(self, result):
        raise NotImplementedError( "Should have implemented this" )



class human_formatter(abstract_formatter):
    """
    Default colorized human readable formater
    """

    def __init__(self):
        """
        Configures colors and such
        """
        self.colors = (
            'BLACK', 'RED', 'GREEN', 'YELLOW',
            'BLUE', 'MAGENTA', 'CYAN', 'WHITE'
        )

        self.disable_color = True

        if sys.stdout.isatty():
            self.disable_color = False


    def disable_color(self):
        """
        Utility method to disable color
        """
        self.disable_color = True


    def _color(self, text, color_name=None, bold=False):
        """
        Simple way to color text
        """

        if self.disable_color == True:
            return text
        
        if color_name == None:
            color_name = 'YELLOW'

        if color_name in self.colors:
            return '\033[{0};{1}m{2}\033[0m'.format(
                int(bold), self.colors.index(color_name) + 30, text)

        raise Exception('ERROR: "{0}" is not a valid color.\n'.format(color_name))
        raise Exception('VALID COLORS: {0}.\n'.format(', '.join(self.colors)))    


    def error(self, result):
        """
        Formats an error
        """
        print "Error: " + self._color(result.message, 'RED')


    def search_results(self, results):
        """
        Formats a search result list
        """
        for index, item in enumerate(results):
            print '[%s] %s (%s) {%s}' % (
                    index, 
                    self._color(item.title), 
                    self._color(item.year, 'RED'), 
                    self._color(item.imdbid, 'GREEN'))


    def movie(self, movie):
        """
        Formats a movie
        """
        print
        print  '%s (%s) {%s}' % (
                self._color(movie.title, 'YELLOW', True), 
                self._color(movie.year), 
                self._color(movie.imdbid))
        print 'IMDB: %s'  % self._color('http://imdb.com/title/' + movie.imdbid,
                'MAGENTA')

        print 'Poster: %s' % self._color(movie.poster_url, 'MAGENTA')
        print
              

        print 'Genre: %s' % ', '.join([self._color(genre) for genre in movie.genres])
        print 'Rated: %s | Released: %s' % (
                self._color(movie.mpaa_rating), 
                self._color(movie.released,))
        print 'IMDB Rating: %s | Votes: %s' % (
                self._color(movie.imdb_rating),
                self._color(movie.imdb_votes)
                )

        print
        print 'Writers: %s' % ', '.join([self._color(person) for person in movie.writers])
        print 'Directors: %s' % ', '.join([self._color(person) for person in movie.directors])
        print 'Actors: %s' % ', '.join([self._color(person) for person in movie.actors])
        print 
        print 'Plot'
        print self._color(movie.get_plot())
        print





