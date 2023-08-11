from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User

from .models import Profile, AddGames, GiftCards, AddExpert, AddKeys


class ProfileModelForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password'
    }))

    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email'
            }),
        }
    # class Meta:
    #     model = Profile
    #     fields = '__all__'
    #     widgets = {
    #         'first_name': forms.TextInput(attrs={
    #             'placeholder': 'First Name'
    #         }),
    #         'last_name': forms.TextInput(attrs={
    #             'placeholder': 'Last Name'
    #         }),
    #         'email': forms.EmailInput(attrs={
    #             'placeholder': 'Email'
    #         }),
    #         'password': forms.PasswordInput(attrs={
    #             'placeholder': 'Password'
    #         }),
    #         'username': forms.TextInput(attrs={
    #             'placeholder': 'Username'
    #         }),
    #     }
    # 'image': forms.URLInput(attrs={
    #     'placeholder': 'image'
    # }),
    # }
    # labels = {
    #     "image_url": "Image URL"
    # }


class AddGamesModelForm(forms.ModelForm):
    class Meta:
        model = AddGames
        fields = '__all__'
        widgets = {
            'game_name': forms.TextInput(attrs={
                'placeholder': 'Game Name'
            }),
            'producer': forms.TextInput(attrs={
                'placeholder': 'Producer'
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Price'
            }),
        }
        labels = {
            "image_url": "Image URL"
        }


class GiftCardsModelForm(forms.ModelForm):
    class Meta:
        model = GiftCards
        fields = '__all__'
        widgets = {
            'your_name': forms.TextInput(attrs={
                'placeholder': 'Game Name'
            }),
            'amount': forms.NumberInput(attrs={
                'placeholder': 'Amount'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Comment'
            }),
        }


class AddExpertModelForm(forms.ModelForm):
    class Meta:
        model = AddExpert
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Game Name'
            }),
            'games_done': forms.NumberInput(attrs={
                'placeholder': 'Games Done'
            }),
            'check_me': forms.Textarea(attrs={
                'placeholder': 'Tag'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Comment'
            }),
        }
        labels = {
            "image_url": "Image URL"
        }


class AddKeysModelForm(forms.ModelForm):
    class Meta:
        model = AddKeys
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Key Name'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Product description'
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Price'
            }),
        }
        labels = {
            "image_url": "Image URL"
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileAndPasswordForm(ProfileEditForm, PasswordChangeForm):
    pass


class UserDeleteForm(forms.Form):
    confirm_delete = forms.BooleanField(label='I confirm that I want to delete my profile', required=True)