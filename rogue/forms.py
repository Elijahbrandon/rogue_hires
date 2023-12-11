from django import forms


class BookingForm(forms.Form):
    booking_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    return_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), required=False)

    def save(self, commit):
        pass

class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=50)
    password = forms.CharField(label='password', widget=forms.PasswordInput)