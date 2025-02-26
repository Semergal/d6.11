from django import forms
from p_library.models import Author, Book, Friend
from django.forms import formset_factory


class AuthorForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Author
        fields = '__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorAdminForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput, label='Имя')


class FriendAdminForm(forms.ModelForm):
    name = forms.CharField(label='Имя друга', widget=forms.TextInput)


class FriendForm(forms.ModelForm):
    name = forms.CharField(label='Имя друга', widget=forms.TextInput)


    class Meta:
        model = Friend
        fields = '__all__'


class FriendEditForm(forms.ModelForm):
    name = forms.CharField(label='Имя друга', widget=forms.TextInput)
    class Meta:
        model = Friend
        fields = ('name',)