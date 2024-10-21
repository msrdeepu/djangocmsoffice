from django import forms
from .models import Member
from .models import Page
from setup.models import SelectList

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




class PageForm(forms.ModelForm):
    
    class Meta:
        model = Page
        fields = '__all__'  # Include all fields from the model
        

    def __init__(self, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)
        # Dynamically load choices for page_type from SelectList where type='PAGETYPE'
        self.fields['page_type'].choices = [
            (item.value, item.value) for item in SelectList.objects.filter(type='PAGETYPE')
        ]
        
        self.fields['group'].choices = [
            (item.value, item.value) for item in SelectList.objects.filter(type='GROUP')
        ]
        
        self.fields['content_access_level'].choices = [
            (item.value, item.value) for item in SelectList.objects.filter(type='CONTENTACCESS')
        ]