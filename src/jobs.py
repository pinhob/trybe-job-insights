from functools import lru_cache
import csv


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    -------

    Com base em: https://stackoverflow.com/a/50402818
    """
    with open(path) as file:
        reader = csv.DictReader(file, delimiter=",", quotechar='"')
        jobs = list(reader)
        return jobs
