from django import forms
from trainer.models import *

class Createxamform(forms.ModelForm):
    class Meta:
        model=createexam
        fields=['date','title','subjectname','typeofexam']
