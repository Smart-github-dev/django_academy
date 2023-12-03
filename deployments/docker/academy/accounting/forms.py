from django import forms
from accounting.models import Plans, Subscriber


class SubscriptionForm(forms.ModelForm):
    class Meta:
         model = Subscriber
         fields = ['first_name', 'last_name', 'address', 'city', 'state', 'phone', 'zip_code', 'email']

    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'John'}))

    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Wick'}))

    address = forms.CharField(
        min_length=2,
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': '1600 Pennsylvania Avenue NW'}))

    city = forms.CharField(
        min_length=2,
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Washington'}))

    state = forms.CharField(
        min_length=2,
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'DC'}))

    phone = forms.CharField(
        min_length=2,
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': '+1 (872) xxx-xxxx'}))

    zip_code = forms.CharField(min_length=2,
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': '60000'}))

    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'john@fuchicorp.com'}))

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')
        city = cleaned_data.get('city')
        state = cleaned_data.get('state')

        if not first_name or not last_name or not email or not phone or not city or not state:
            raise forms.ValidationError('Please enter required information')
