from django import forms
from .models import StudentDetails


class OrderForm(forms.ModelForm):
    name = forms.CharField(
        label="Name",
        widget=forms.TextInput(attrs={
            'placeholder': "Eg. Jobi Jo",
        })
    )
    age = forms.CharField(
        label="Age",
        widget=forms.NumberInput(attrs={
            'placeholder': "Eg. 20",
        })
    )
    mail_id = forms.CharField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'placeholder': "Eg. jobi@gmail.com",
        })
    )
    address = forms.CharField(
        label="Address",
        widget=forms.Textarea(attrs={
            'placeholder': "Enter Your Address.", 'rows': 5,
        })
    )
    phone_number = forms.CharField(
        widget=forms.NumberInput(attrs={
            'placeholder': "9745******",
        })
    )
    dob = forms.CharField(
        label="DOB",
        widget=forms.DateInput(
            attrs={
                'label': 'DOB',
                'type': 'date',
                'onkeydown': 'return-false',
                'min': '1950-01-01',
                'max': '2030-01-01',
            }
        )
    )

    class Meta:
        model = StudentDetails
        fields = '__all__'
        GENDER_CHOICES = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other')
        )
        widgets = {
            'gender': forms.RadioSelect(choices=GENDER_CHOICES, attrs={'class': 'btn-check'}),

        }
