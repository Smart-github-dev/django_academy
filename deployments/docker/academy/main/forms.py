from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Questions
from django.forms import ModelForm, Textarea
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible, ReCaptchaV2Checkbox
from accounting.models import Subscriber, Plans

class faqForm(forms.ModelForm):
    captcha         = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    class Meta:
        model = Questions
        fields = [ 'first_name', 'last_name', 'email', 'subject', 'body']
        widgets = {
                    'body': Textarea(attrs={'cols': 40, 'rows': 20}),
                }



class ContactForm(forms.Form):
    first_name      = forms.CharField(min_length=2, max_length=30, widget=forms.TextInput(attrs={'class': "form-control border-0 text-center", 'placeholder' : "First name"}))
    last_name       = forms.CharField(min_length=2, max_length=30, widget=forms.TextInput(attrs={'class': "form-control border-0 text-center", 'placeholder' : "Last name"}))
    email           = forms.CharField(min_length=4, max_length=100, widget=forms.EmailInput(attrs={'class': "form-control border-0 text-center", 'placeholder' : "Write your email here."}))
    subscription    = forms.ModelChoiceField(queryset=Plans.objects.all(), widget=forms.Select(attrs={'class': "form-control border-0"}))
    message         = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control", 'placeholder' : "Write your message here."}))


class UpdateInfo(forms.Form):
    first_name = forms.CharField(min_length=2, max_length=30)
    last_name = forms.CharField(min_length=2, max_length=30)
    email = forms.EmailField()

    def clean(self):
        cleaned_data = super(UpdateInfo, self).clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        if not first_name or not last_name or not email:
            raise forms.ValidationError('Please enter required information')



class UpdateSettingsForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', ]



class UpdateSubscriptionInfoForm(UserChangeForm):

    class Meta:
        model = Subscriber
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'zip_code', 'state', 'city']


class RegistrationForm(UserCreationForm):

    email = forms.EmailField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = {
            'username',
            'last_name',
            'first_name',
        }

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']


        if commit:
            user.save()


        return user
