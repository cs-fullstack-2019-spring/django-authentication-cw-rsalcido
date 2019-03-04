from django import forms
from.models import CalTrackModel


# model form created for the model required to save information to the database
class CalTrackForm(forms.ModelForm):
    class Meta:
        model= CalTrackModel
        fields = "__all__"

















