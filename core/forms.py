from django import forms
from .models import Beverage
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

class PumpForm(forms.Form):
    pump1 = forms.ModelChoiceField(Beverage.objects.all(), label='Насос 1', to_field_name='name')
    pump2 = forms.ModelChoiceField(Beverage.objects.all(), label='Насос 2', to_field_name='name')
    pump3 = forms.ModelChoiceField(Beverage.objects.all(), label='Насос 3', to_field_name='name')

    def __init__(self, *args, **kwargs):
        super(PumpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_class = 'blueForms'
        self.helper.form_action = '/choose_cocktails/'
        self.helper.add_input(Submit('submit', 'Сохранить'))