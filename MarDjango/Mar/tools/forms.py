from django import forms


class AddForm(forms.Form):
    a = forms.CharField()
    b = forms.CharField(widget=forms.Textarea(attrs = {'class':'postData'}))
