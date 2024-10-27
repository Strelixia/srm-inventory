from django import forms
from .models import User, Product, Order

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','role']

    def clean_mail(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email= email).exists():
            raise forms.ValidationError('Cet email est déjà utilisé.')
        return email

