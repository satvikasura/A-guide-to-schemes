from django import forms
OPTION_CHOICES= [
    ('yes', 'Yes'),
    ('no', 'No'),
    ]

class checkform(forms.Form):
    options = forms.CharField(widget=forms.RadioSelect(choices=OPTION_CHOICES))