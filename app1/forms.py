
from django import forms
from .models import CosmoUser,CosmoTrainerdata

class CosmoForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    uid = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    passwd = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
    cwpasswd = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
    mail = forms.CharField(widget=forms.TextInput(), required=True)
    mobileno= forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    qualification=forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    status = forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)
    class Meta:
        model=CosmoUser
        fields=['name','uid','mail','passwd','cwpasswd','mobileno','qualification','status']

class CosmoTrainerdataForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    uid=forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    mail=forms.CharField(widget=forms.TextInput(), required=True)
    passwd=forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
    qualification=forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    mobileno=forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    designation=forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    Experience=forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    authkey=forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)
    status = forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)
    class Meta:
        model=CosmoTrainerdata
        fields=['name','uid','mail','passwd','qualification','mobileno','designation','Experience','authkey','status']


