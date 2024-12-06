from django import forms
from course.models import Register

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['name',"phone", 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'style': 'width: 300px; margin-left: 20px'}),
            'email': forms.TextInput(attrs={'style': 'width: 300px;'}),
            'last_name': forms.TextInput(attrs={'style': 'width: 300px; margin-left: 21px'}),
        }