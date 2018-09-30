# Module to run tests on Pulsar I/O
from __future__ import print_function, absolute_import, division, unicode_literals

# TEST_UNICODE_LITERALS

import pytest
import os

from astropy.table import Table

from pulsars import io as pio

def data_path(filename):
    data_dir = os.path.join(os.path.dirname(__file__), 'files')
    return os.path.join(data_dir, filename)

def test_load_DMs():
    DMs = pio.load_DM()
    assert isinstance(DMs, Table)
    assert 'b' in DMs.keys()

def test_load_plx():
    plx = pio.load_parallax()
    assert isinstance(plx, Table)

def test_load_pulsars():
    ptbl = pio.load_pulsars()
    assert 'PI' in ptbl.keys()



