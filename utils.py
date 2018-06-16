import os


def get_env(key, dft=None):
    return os.environ.get(key, dft)
