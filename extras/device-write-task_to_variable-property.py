#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
handles write tasks for variables attached to the generic devices
"""

from pyscada.models import DeviceWriteTask, VariableProperty
from time import time
import logging

logger = logging.getLogger(__name__)


def startup(self):
    """
    write your code startup code here, don't change the name of this function
    :return:
    """
    pass


def shutdown(self):
    """
    write your code shutdown code here, don't change the name of this function
    :return:
    """
    pass


def script(self):
    """
    write your code loop code here, don't change the name of this function

    :return:
    """
    # add
    for task in DeviceWriteTask.objects.filter(
        done=False,
        start__lte=time(),
        failed=False,
        variable_property__variable__device__protocol=1,
    ):
        if task.variable_property.variable.scaling is not None:
            task.value = task.variable_property.variable.scaling.scale_output_value(
                task.value
            )
        if task.variable_property:
            # write the freq property to VariableProperty use that for later read
            vp = VariableProperty.objects.update_property(
                variable_property=task.variable_property, value=task.value
            )
            if vp:
                task.done = True
                task.finished = time()
                task.save()
                continue

        logger.debug("nothing to do for device write task %d" % task.pk)
        task.failed = True
        task.finished = time()
        task.save()
