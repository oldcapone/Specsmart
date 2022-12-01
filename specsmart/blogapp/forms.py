from django import forms


class ContactForm(forms.Form):
    name_1 = forms.CharField(label='Название')
    email = forms.EmailField(label='email')
    message = forms.CharField(label='Сообщение')
    tel_1 = forms.CharField(label='Телефон')