from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Member
        fields = ['firstname', 'lastname', 'role', 'email', 'mobile', 'phone', 'whatsapp', 'city', 'state', 'country', 'zipcode', 'password', 'confirm_password', 'notes']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
