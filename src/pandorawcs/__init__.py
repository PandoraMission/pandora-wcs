__version__ = "0.1.0"
import os  # noqa

PACKAGEDIR = os.path.abspath(os.path.dirname(__file__))


import logging  # noqa: E402

logging.basicConfig()
logger = logging.getLogger("pandorawcs")
