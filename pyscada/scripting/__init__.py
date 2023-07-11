# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__version__ = "0.8.0"
__author__ = "Martin Schröder, Camille Lavayssiere"
__email__ = "team@pyscada.org"
__description__ = (
    "Scripting extension for PyScada a Python and Django based Open Source SCADA System"
)
__app_name__ = "Scripting"

parent_process_list = [
    {
        "pk": 95,
        "label": "pyscada." + __app_name__.lower(),
        "process_class": "pyscada." + __app_name__.lower() + ".worker.MasterProcess",
        "process_class_kwargs": '{"dt_set":30}',
        "enabled": True,
    }
]
