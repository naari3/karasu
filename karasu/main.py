# -*- coding: utf-8 -*-

import os
import sys

import tweepy

from .authenticate import *


def main():
    t = tweepy.API(get_authen())

    user = t.verify_credentials()
    print(user.name)

    for status in tweepy.Cursor(t.user_timeline, screen_name=user.screen_name, count=5).items(5):
        print(status.text)


if __name__ == '__main__':
    main()
