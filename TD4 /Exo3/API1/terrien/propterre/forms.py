from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class PtForm(ModelForm):
    class Meta:
        model = models.Pt
        fields = ('lieu', 'surface', 'culture', 'renseignements','date_mise', 'jachere')
        labels = {
            'lieu' : _('Lieu '),
            'surface' : _('Surface ') ,
            'culture' : _('Type de culture'),
            'renseignements' : _('Renseignements terrain '),
            'date_mise' : _('Date de parution '),
            'jachere' : _('Champs jacheres ou non'),
    }
        
    localized_fields = ('date_mise')
