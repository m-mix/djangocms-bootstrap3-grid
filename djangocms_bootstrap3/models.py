# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from cms.models import CMSPlugin


GRID_CONFIG = {'COLUMNS': 12,
               'ROW_TEMPLATES': (('djangocms_bootstrap3/row.html', _('Row')),
                                 ('djangocms_bootstrap3/container_row.html', _('Container Row')),)
}

GRID_CONFIG.update(getattr(settings, 'DJANGOCMS_BOOTSTRAP3_CONFIG', {}))


# Medium devices Desktops (>=992px)
# Used as default column size
DJANGOCMS_GRID_MD_CHOICES = [('col-md-%s' % i, '%s' % i ) for i in range(1, GRID_CONFIG['COLUMNS']+1)]

# Large devices Desktops (>=1200px)
DJANGOCMS_GRID_LG_CHOICES = [('',_('Default'))] + [('col-lg-%s' % i, '%s' % i) for i in range(1, GRID_CONFIG['COLUMNS']+1)]

# Small devices Tablets (>=768px)
DJANGOCMS_GRID_SM_CHOICES = [('',_('Default'))] + [('col-sm-%s' % i, '%s' % i) for i in range(1, GRID_CONFIG['COLUMNS']+1)]

# Extra small devices Phones (<768px)
DJANGOCMS_GRID_XS_CHOICES = [('',_('Default'))] + [('col-xs-%s' % i, '%s' % i) for i in range(1, GRID_CONFIG['COLUMNS']+1)]


class Row(CMSPlugin):
    custom_classes = models.CharField(_('custom classes'), max_length=200, blank=True)
    template = models.CharField(_('Row template'), choices=GRID_CONFIG['ROW_TEMPLATES'],
                                default=GRID_CONFIG['ROW_TEMPLATES'][0][0], max_length=100)

    translatable_content_excluded_fields = ['custom_classes']

    def __unicode__(self):
        return _(u"Row")


class RowColumn(CMSPlugin):
    size = models.CharField(_('size'), max_length=100)
    custom_classes = models.CharField(_('custom classes'), max_length=200, blank=True)
    translatable_content_excluded_fields = ['custom_classes']

    def __unicode__(self):
        return u"%s" % self.size
