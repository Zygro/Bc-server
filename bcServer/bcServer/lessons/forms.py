from django import forms

class SubmitForm(forms.Form):
    submitfile = forms.FileField(label='select a file'),
    user = forms.IntegerField(label='user'),
    lesson = forms.IntegerField(label='lesson'),
