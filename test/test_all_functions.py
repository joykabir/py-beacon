# -*- coding: utf-8 -*-
"""
Tests all functions
"""
import examples
#from examples.find_folder_contents import get_dir_contents

def test_data(monkeypatch, capsys):
    """
    Test os/find_folder_contents.py
    """
    get_dir_contents('~/tmp')
    stdout, _ = capsys.readouterr()
    assert stdout is not None
