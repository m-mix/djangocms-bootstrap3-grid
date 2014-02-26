# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import( Column,
                     DJANGOCMS_GRID_LG_CHOICES,
                     DJANGOCMS_GRID_MD_CHOICES,
                     DJANGOCMS_GRID_SM_CHOICES,
                     DJANGOCMS_GRID_XS_CHOICES)


class ColumnPluginForm(forms.ModelForm):
    size_md = forms.ChoiceField(label=_("Medium size"), help_text=_('Medium devices Desktops (>=992px)'),
                                choices=DJANGOCMS_GRID_MD_CHOICES, required=True)

    size_lg = forms.ChoiceField(label=_("Large size"), help_text=_('Large devices Desktops (>=1200px)'),
                                choices=DJANGOCMS_GRID_LG_CHOICES, required=False)

    size_sm = forms.ChoiceField(label=_("Small size"), help_text=_('Small devices Tablets (>=768px)'),
                                choices=DJANGOCMS_GRID_SM_CHOICES, required=False)

    size_xs = forms.ChoiceField(label=_("Extra small size"), help_text=_('Extra small devices Phones (<768px)'),
                                choices=DJANGOCMS_GRID_XS_CHOICES, required=False)

    class Meta:
        model = Column
        exclude = ('size', 'page', 'position', 'placeholder', 'language', 'plugin_type')

    def __init__(self, *args, **kwargs):

        super(ColumnPluginForm, self).__init__(*args, **kwargs)
        if self.instance:
            current_size_list = self.instance.size.split()
            for size in current_size_list:
                if size in [x[0] for x in DJANGOCMS_GRID_LG_CHOICES]:
                    self.fields['size_lg'].initial = size
                elif size in [x[0] for x in DJANGOCMS_GRID_MD_CHOICES]:
                    self.fields['size_md'].initial = size
                elif size in [x[0] for x in DJANGOCMS_GRID_SM_CHOICES]:
                    self.fields['size_sm'].initial = size
                elif size in [x[0] for x in DJANGOCMS_GRID_XS_CHOICES]:
                    self.fields['size_xs'].initial = size
