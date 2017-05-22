# -*- coding: utf-8 -*-

import os
import sys
import signal

import tweepy

from .manager import Manager


def run():
    """
    [WIP] test place
    """
    try:
        manager = Manager()

        def quit():
            manager.shutdown()

        ctrl_c_handler = lambda signum, frame: quit()
        signal.signal(signal.SIGINT, ctrl_c_handler)

        manager.run()

    except Exception as e:
        print(e)
        sys.exit(1)
    except (KeyboardInterrupt, RuntimeError, SystemExit) as e:
        pass
