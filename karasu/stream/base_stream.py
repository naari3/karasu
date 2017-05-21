# -*- coding: utf-8 -*-

import tweepy


class BaseStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text, end=("\n" + "=" * 30 + "\n\n"))
