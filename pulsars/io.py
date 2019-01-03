""" I/O routines related to Pulsar data
"""
from __future__ import print_function, absolute_import, division, unicode_literals

from pkg_resources import resource_filename
import pdb

import numpy as np

from astropy.table import Table
from astropy.coordinates import SkyCoord
from astropy import units as u

# These should be update from time to time
DM_file = resource_filename('pulsars', 'data/atnf_cat/DM_cat_v1.56.dat')
Plx_file = resource_filename('pulsars', 'data/parallax/Plx_aug2018.dat')


def load_DM():
    """
    Load up the latest set of DMs (in our Repo)

    Returns:
        DMs : Table

    """
    print("Loading up DMs from {}".format(DM_file))
    DMs = Table.read(DM_file, format='ascii')
    # Fuss with coords a bit
    coords = SkyCoord(ra=DMs['RAJ'], dec=DMs['DECJ'], unit=(u.hourangle, u.deg))
    DMs['b'] = coords.galactic.b.value
    DMs['l'] = coords.galactic.l.value
    # Return
    return DMs

def load_parallax():
    """
    Load up the Parallax data

    Returns:
        plx : Table

    """
    print("Loading up Parallax data from {}".format(Plx_file))
    plx = Table.read(Plx_file, format='ascii.fixed_width')
    # Return
    return plx

def load_pulsars():
    # Load em
    DMs = load_DM()
    plx = load_parallax()
    # Match em
    plx_val = np.zeros(len(DMs))
    plx_eminus = np.zeros(len(DMs))
    plx_eplus = np.zeros(len(DMs))
    for row in plx:
        idx = np.where(DMs['PSRJ'] == row['JNAME'])[0]
        if len(idx) == 0:
            pass
        elif len(idx) > 1:
            pdb.set_trace()
        else:
            plx_val[idx] = row['PI']
            plx_eminus[idx] = row['eminus']
            plx_eplus[idx] = row['eplus']
    # Add to DM table
    DMs['PI'] = plx_val
    DMs['PIm'] = plx_eminus
    DMs['PIp'] = plx_eplus

    # Return
    return DMs
