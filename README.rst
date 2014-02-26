djangocms-bootstrap3-grid
==============

A Grid Plugin for django CMS, that uses a bootstrap 3 grid system.
Contains:
container
row
column

Installation
------------

This plugin requires `django CMS` 2.4 or higher to be properly installed.
Works with `django CMS` 3.0.beta3

* Run ``pip install https://github.com/m-mix/djangocms-bootstrap3-grid/archive/master.zip``.
* Add ``'djangocms_bootstrap3'`` to your ``INSTALLED_APPS`` setting.
* Run ``manage.py migrate djangocms_bootstrap3``.


Configure your bootstrap grid system (if it need)
-------------------

DJANGOCMS_BOOTSTRAP3_CONFIG = {'COLUMNS': 12,
               'CONTAINER_TEMPLATES': (('djangocms_bootstrap3/container.html', _('Container')),
                                 ('djangocms_bootstrap3/container_fluid.html', _('Container fluid')),
                                 ),
               'ROW_TEMPLATE': 'djangocms_bootstrap3/row.html',
               'COLUMN_TEMPLATE': 'djangocms_bootstrap3/column.html'

}


