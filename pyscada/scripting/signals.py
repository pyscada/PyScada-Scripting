# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pyscada.models import BackgroundProcess
from pyscada.scripting.models import Script

from django.dispatch import receiver
from django.db.models.signals import post_save

import logging

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Script)
def _reinit_daq_daemons(sender, instance, **kwargs):
    """
    update the daq daemon configuration when changes be applied in the models
    """
    if type(instance) is Script:
        try:
            #todo select only one script not all
            bp = BackgroundProcess.objects.get(process_class_kwargs__contains=str('"script_id": ' + str(instance.id)))
        except:
            return False
        bp.restart()
    else:
        logger.debug('post_save from %s' % type(instance))
