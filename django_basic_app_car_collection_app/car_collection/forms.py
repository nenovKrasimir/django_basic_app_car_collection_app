from django import forms
from .models import Profile, Car


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}), }

        labels = {
            'username': 'Username',
            'email': 'Email',
            'age': 'Age',
            'password': 'Password', }


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(CreateProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['disabled'] = True


class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class EditCarForm(CreateCarForm):
    pass


class DeleteCarForm(CreateCarForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['disabled'] = True
