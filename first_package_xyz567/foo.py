import random


def shuffle_args(*args):
    random_args = list(args)
    random.shuffle(random_args)
    return random_args
