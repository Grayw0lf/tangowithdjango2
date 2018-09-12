from django import forms
from django.contrib.auth.admin import User
from rango.models import Page, Category, UserProfile


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text='Please enter the category name.')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Category
        fields = ('name',)
        exclude = ('slug',)


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
                            help_text='Please enter the title of the page.')
    url = forms.URLField(max_length=200,
                         help_text='Please enter the URL of the page.')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        exclude = ('category', 'slug')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    website = forms.URLField(required=False)
    picture = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
        exclude = ('user',)
