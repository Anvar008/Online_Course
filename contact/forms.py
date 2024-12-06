from django import forms
from contact.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'style': 'width: 350px; height: 33px; border-radius: 10px;'}),
            'email': forms.TextInput(attrs={'style': 'width: 350px; height: 33px; border-radius: 10px; margin-left: 4px; margin-top: 8px'}),
            # 'message': forms.TextInput(attrs={'style': 'margin-top: 5px; margin-bottom: 15px'})
        }