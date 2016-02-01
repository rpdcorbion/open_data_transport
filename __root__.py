import os


def path():
    return os.path.dirname(__file__) + "/"


def real_path():
    file_path = os.path.realpath(__file__)
    str_end = file_path.find(__name__)
    file_path = file_path[:str_end]

    return os.path.realpath(file_path) + "/"


def lib():
    return path() + "lib/"


def assign_dir(dir_rel_path):
    source_dir = real_path() + dir_rel_path
    if not os.path.exists(source_dir):
        os.makedirs(source_dir)
    return source_dir
