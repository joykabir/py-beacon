# -*- coding: utf-8 -*-
"""
Finds current working directory and
prints contents recursively
"""
########################
## Author: Ziaul Kabir
## 2016.03.01
## Pylint verified for PEP8
########################
import os

def get_dir_contents(rel_path):
    """
    This function prints current directory contents
    """
    rval = []
    abs_path = os.path.abspath(rel_path)
    if os.path.exists(abs_path):
        for child in os.listdir(abs_path):
            try:
                child_abs_path = os.path.join(rel_path, child)
                if os.path.isdir(child_abs_path):
                    get_dir_contents(child_abs_path)
                else:
                    rval.append(child_abs_path)
            except RuntimeError as rte:
                print rte.message('Wrong path')
    return tuple(rval)

def find_current_dir():
    """
    Call path function and provide path as an argument
    """
    cpath = os.getcwd()
    print get_dir_contents(cpath)

def run():
    """
    Run main module
    """
    find_current_dir()

if __name__ == '__main__':
    run()
