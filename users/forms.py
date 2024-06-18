from django import forms
from models import Person


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(required=True, widget=forms.PasswordInput)

    class Meta:
        model = Person
        fields = ['username', 'email', 'password1', 'password2']


    def clean_password1(self):
        password1 = self.cleaned_data.get("password1", None)
        password2 = self.cleaned_data.get("password2", None)

        if password1 != password2:
            raise forms.ValidationError("passwords do Not match !")

        return password1

    # phle form instance banaate hee built-in validations chlti hain
    # cleaned_data banta hai first step mein ke baad
    # then jb is_valid() likhte hain toh custom validations chlti hain
    # then true kiya return toh shi hai other wise forms.error mein error return ho jayega


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput)