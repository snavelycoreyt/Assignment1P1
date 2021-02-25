from django import forms
from django.contrib.auth.models import User

from .models import Inventory
from .models import Store

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ('inventory_name', 'inventory_amount', 'store', )

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('store_brand', 'store_addr', 'store_category')

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']