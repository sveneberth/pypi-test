import random
import string

from .foo import shuffle_args


def make_args(k=5):
    return random.choices(string.ascii_letters + string.digits, k=5)


def make_random_args(k=5):
    return shuffle_args(*make_args(k))


def get_version():
    from . import __version__
    return __version__
