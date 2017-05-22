# -*- coding: utf-8 -*-

import os
import sys
import signal

import tweepy

from .authenticate import *
from .stream import *


class Manager(object):
    """This client's manager."""
    def __init__(self, arg=None):
        self.t = tweepy.API(get_authen())
        self.stream_dict = {
            'home': userstream_generator
        }

    def listen(self, arg=None):
        """
        command parser, user input, etc
        """
        # TODO: urwid
        while True:
            pass

    def shutdown(self):
        print("byebye")
        sys.exit(0)

    def init(self, arg=None):
        # TODO: changeable with config
        self.stream_dict.get('home')(self.t.auth)

    def run(self, arg=None):
        # TODO: some check here
        # TODO: some stream set
        # TODO: some user input listener set
        self.init()
        self.listen()
