from django import forms

NUM_CHOICES = (
    (1, 1),
    (5, 5),
    (10, 10),
    (25, 25),
    (50, 50)
)

class QueryForm(forms.Form):
    num = forms.ChoiceField(choices=NUM_CHOICES)
