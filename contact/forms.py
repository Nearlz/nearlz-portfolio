from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True,widget=forms.TextInput(
        attrs={'class':'form-control form-field'}
    ))
    email = forms.EmailField(required=True,widget=forms.EmailInput(
        attrs={'class':'form-control form-field'}
    ))
    subject = forms.CharField(required=True,widget=forms.TextInput(
        attrs={'class':'form-control form-field'}
        ))
    content = forms.CharField(required=True,widget=forms.TextInput(
        attrs={'class':'form-control form-field md-textarea','rows':3}
    ))