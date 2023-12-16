from django import forms
from .models import Machine

class MachineFilterForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['Model_of_equipment', 'Engine_model', 'Transmission_model',
                  'Drive_axle_model', 'Steering_axle_model', 'Zav_number_machine']

    def __init__(self, *args, **kwargs):
        super(MachineFilterForm, self).__init__(*args, **kwargs)
        self.fields['Model_of_equipment'].required = False
        self.fields['Engine_model'].required = False
        self.fields['Transmission_model'].required = False
        self.fields['Drive_axle_model'].required = False
        self.fields['Steering_axle_model'].required = False
        self.fields['Zav_number_machine'].required = False