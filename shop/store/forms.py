from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Flavor, Amount


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'surname', 'email', 'phone_number', 'password1', 'password2']
        

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')
    

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)
    flavor = forms.ModelChoiceField(queryset=Flavor.objects.none(), required=False)
    amount = forms.ModelChoiceField(queryset=Amount.objects.none(), required=False)
    
    def __init__(self, *args, **kwargs):
        product = kwargs.pop('product', None)
        super().__init__(*args, **kwargs)
        if product:
            self.fields['flavor'].queryset = product.flavors.all()
            self.fields['amount'].queryset = product.amounts.all()