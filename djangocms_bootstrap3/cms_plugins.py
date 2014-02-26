# -*- coding: utf-8 -*-
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from .models import Row, RowColumn, GRID_CONFIG
from django.utils.translation import ugettext_lazy as _
from .forms import RowColumnPluginForm


class RowPlugin(CMSPluginBase):
    model = Row
    name = _('Grid row')
    module = _('Grid')
    render_template = GRID_CONFIG['ROW_TEMPLATES'][0][0]
    allow_children = True
    child_classes = ['RowColumnPlugin']

    def render(self, context, instance, placeholder):

        if instance.template:
            self.render_template = instance.template

        context.update({
            'grid': instance,
            'placeholder': placeholder,
        })
        return context


class RowColumnPlugin(CMSPluginBase):
    model = RowColumn
    name = _('Grid Column')
    module = _('Grid')
    render_template = 'djangocms_bootstrap3/column.html'
    allow_children = True
    form = RowColumnPluginForm

    def save_model(self, request, obj, form, change):
        res = []
        size_lg = form.cleaned_data['size_lg']
        size_md = form.cleaned_data['size_md']
        size_sm = form.cleaned_data['size_sm']
        size_xs = form.cleaned_data['size_xs']

        if size_lg:
            res.append(size_lg)
        if size_md:
            res.append(size_md)
        if size_sm:
            res.append(size_sm)
        if size_xs:
            res.append(size_xs)

        obj.size = ' '.join(res)
        response = super(RowColumnPlugin, self).save_model(request, obj, form, change)
        return response

    def render(self, context, instance, placeholder):
        context.update({
            'column': instance,
            'placeholder': placeholder,
        })
        return context

plugin_pool.register_plugin(RowPlugin)
plugin_pool.register_plugin(RowColumnPlugin)
