# -*- coding: utf-8 -*-
"""
Dictionary converter of various kinds and forms
"""
from json import loads, dumps
from collections import OrderedDict

def to_dict(input_ord_dict):
    """
    Convert nested ordereddict to dictionary
    :param input_ord_dict: nested OrderedDict
    """
    return loads(dumps(input_ordered_dict))
