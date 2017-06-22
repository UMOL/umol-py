import os


def path(file_name: str) -> list:
    """
    Return the full path to the requested file
    """
    here = os.path.dirname(os.path.realpath(__file__))
    # use file extension name as subdirectory name
    _, subdir = os.path.splitext(file_name)
    return os.path.join(here, subdir.replace(".", ""), file_name)
