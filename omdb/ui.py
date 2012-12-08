#!/usr/bin/env python

# this fileis part of flicks
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
# Modified: 2012-12-07  21:22


import omdb.service
import argparse
import omdb.formatter
import omdb.model


class cli_interface:
    """
    Command line interface for omdb 
    """


    def __init__(self):
        """
        Initializes service
        """
        self.service = None
        self.formatter = None
        self.formatter_options = {
                'human': omdb.formatter.human_formatter,
                'debug': omdb.formatter.debug_formatter
                }

    def _set_formatter(self, formatter_name):
        """
        Sets the formatter used by commands
        """
        self.formatter = self.formatter_options[formatter_name]()


    def get_service(self):
        """
        Returns service
        """
        if None == self.service:
            self.service = omdb.service.omdb_api()
        return self.service


    def cmd_search(self, args):
        """
        Search for movie
        """
        service = self.get_service()
        results = service.search(args.query, args.year)
        if isinstance(results, omdb.model.omdb_error):
            self.formatter.error(results)
        else:
            self.formatter.search_results(results)


    def cmd_title(self, args):
        """
        Gets movie information based on title
        """
        service = self.get_service()
        result = service.title(args.title, args.year, args.plot, args.tomatoes)
        if isinstance(result, omdb.model.omdb_error):
            self.formatter.error(result)
        else:
            self.formatter.movie(result)


    def cmd_imdbid(self, args):
        """
        Gets movie information based on imdbID
        """
        service = self.get_service()
        result = service.imdbid(args.imdbid, args.plot, args.tomatoes)
        if isinstance(result, omdb.model.omdb_error):
            self.formatter.error(result)
        else:
            self.formatter.movie(result)


    def get_argparser(self):
        """
        Sets up and returns argument parser for cli
        """

        parser = argparse.ArgumentParser(
                prog='omdbpy',
                description='commandline interface for http://www.omdbapi.com/',
                )

        parser.add_argument('-f', '--formatter',
                metavar='FMT',
                choices = list(self.formatter_options.keys()),
                default='human',
                help='format of the output')


        subparsers = parser.add_subparsers(
                title='Methods',
                description='method to retrieve movie information',
                help='method help')

        #
        # Search
        #

        parser_search = subparsers.add_parser('search',
                help='search for movie return matching results')

        parser_search.add_argument('query',
                metavar='STRING',
                help='string to search for')

        parser_search.add_argument('-y', '--year', 
                help='optional year to narrow results')

        parser_search.add_argument('-i', '--interactive', 
                action='store_true',
                help='starts interactive mode')

        parser_search.set_defaults(func=self.cmd_search)


        #
        # Title
        #

        parser_title = subparsers.add_parser('title',
                help='returns movie information based on the title')

        parser_title.add_argument('title', 
                help='title of the movie')

        parser_title.add_argument('-p', '--plot', 
                action='store_true',
                help='show extended plot details')

        parser_title.add_argument('-t', '--tomatoes', 
                action='store_true',
                help='adds rotten tomatoes data (slow)')

        parser_title.add_argument('-y', '--year', 
                help='optional year to narrow results')

        parser_title.set_defaults(func=self.cmd_title)

        #
        # IMDBid
        #

        parser_imdbid = subparsers.add_parser('imdbid',
                help='returns movie information based on the imdbid')

        parser_imdbid.add_argument('imdbid', 
                help='imdbid of the movie')

        parser_imdbid.add_argument('-p', '--plot', 
                action='store_true',
                help='show extended plot details')

        parser_imdbid.add_argument('-t', '--tomatoes', 
                action='store_true',
                help='adds rotten tomatoes data (slow)')

        parser_imdbid.set_defaults(func=self.cmd_imdbid)

        return parser


    def run(self):
        """
        Runs commandline interface
        """
        parser = self.get_argparser()
        args = parser.parse_args()
        self._set_formatter(args.formatter)
        args.func(args)





