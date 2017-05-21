# -*- coding: utf-8 -*-

import os
import sys

import tweepy

from .authenticate import *
from .stream import *


def main():
    """
    [WIP] test place
    """
    t = tweepy.API(get_authen())

    user = t.verify_credentials()
    print(user.name)

    for status in tweepy.Cursor(t.user_timeline, screen_name=user.screen_name, count=5).items(5):
        print(status.text)

    listener = BaseStreamListener()
    stream = tweepy.Stream(t.auth, listener)
    stream.userstream(async=True)


if __name__ == '__main__':
    main()
