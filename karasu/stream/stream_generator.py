# -*- config: utf-8 -*-

import threading
import tweepy

from .base_stream import BaseStreamListener


def userstream_generator(auth, arg=None):
    listener = BaseStreamListener()
    stream = tweepy.Stream(auth, listener)
    userstream = stream.userstream

    th = threading.Thread(
        target=userstream,
        kwargs={'async': True},
    )
    th.daemon = True
    th.start()
