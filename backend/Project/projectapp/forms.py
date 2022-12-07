from django import forms

class EmailForm(forms.Form):
    Email = forms.EmailField(required=True)
    FirstName = forms.CharField(required=True)
    LastName = forms.CharField(required=True)
    Text = forms.CharField(required=True)