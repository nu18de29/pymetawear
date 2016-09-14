# -*- coding: utf-8 -*-
"""Release data for the PyMetaWear project."""

# -----------------------------------------------------------------------------
#  Copyright (c) 2016, Nedomkull Mathematical Modeling AB.
# -----------------------------------------------------------------------------

import os
from ctypes import cdll, c_longlong
from pymetawear.mbientlab.metawear.core import Fn_DataPtr, Fn_VoidPtr_Int
from pymetawear.mbientlab.metawear.functions import setup_libmetawear
from pymetawear.utils import IS_64_BIT

# Version information.
__version__ = '0.5.0a4'
version = __version__  # backwards compatibility name
version_info = (0, 5, 0, 'a4')

if os.environ.get('METAWEAR_LIB_SO_NAME') is not None:
    libmetawear = cdll.LoadLibrary(os.environ["METAWEAR_LIB_SO_NAME"])
else:
    libmetawear = cdll.LoadLibrary(
        os.path.join(os.path.abspath(os.path.dirname(__file__)),
                     'libmetawear.so'))

setup_libmetawear(libmetawear)

# Alleviating Segfault causing pointer errors in 64-bit Python.
if IS_64_BIT:
    libmetawear.mbl_mw_datasignal_subscribe.argtypes = [c_longlong, Fn_DataPtr]
    libmetawear.mbl_mw_datasignal_unsubscribe.argtypes = [c_longlong, ]
    libmetawear.mbl_mw_datasignal_log.argtypes = [c_longlong, Fn_DataPtr]
    libmetawear.mbl_mw_datasignal_read.argtypes = [c_longlong]
