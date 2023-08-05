#!/usr/bin/env python3

"""  Complex types - string and int/float to tuple. """

import math
from typing import Optional, Tuple


def to_kv(k: Optional[str], v: Optional[float]) -> Tuple:
    """ This function takes a string k and an int OR float v as
        arguments and returns a tuple.
    """
    return (k, v*v)
