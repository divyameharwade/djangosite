from django import forms
from django.forms import models
from stuffapp.models import Thing

class StuffForm(models.ModelForm):

    class Meta:
        # converts the db fields into form fields automatically
        model = Thing
        #for specific fields use below:
        fields = ('title', 'description')
        # to exclude a field
        # exclude = ('quantity')

