from django import forms

from .models import SignUp

class ContactForm(forms.Form):
    #code
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()
    
class SignUpForm(forms.ModelForm):
    #code
    class Meta:
        #code
        model = SignUp
        fields = ['full_name', 'email']
        # exclude = ['full_name']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')
        return email
    
    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        return full_name