from django.forms import (ModelMultipleChoiceField, ModelForm, TextInput,
                          Textarea, CharField, PasswordInput, EmailField,
                          EmailInput, Form, SelectMultiple)
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from captcha.fields import CaptchaField

from blog.models import Post, Tag


class ContactForm(Form):
    subject = CharField(
        label='Тема',
        widget=TextInput(attrs={'class': 'form-control'})
    )
    message = CharField(
        label='Текст',
        widget=Textarea(attrs={'class': 'form-control', 'rows': 5})
    )
    captcha = CaptchaField()


class PostForm(ModelForm):
    tags = ModelMultipleChoiceField(
        widget=SelectMultiple(attrs={'size': 4}),
        queryset=Tag.objects.all()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Категория не выбрана"

    class Meta:
        model = Post
        fields = ["category", "title", "tags", "body", "photo", "is_published"]

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control mb-4',
                'placeholder': 'Название статьи',
            }),
            'body': Textarea(attrs={
                'class': 'form-control mb-4',
                'placeholder': 'Контент блога',
            }),
        }

    def clean_title(self):
        title = self.cleaned_data['title']

        if len(title) > 200:
            raise ValidationError("The length mustn't exceed 200 characters")
        return title

    def clean_slug(self):
        self.slug = slugify(self.name)
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create" ')
        return new_slug


class UserLoginForm(AuthenticationForm):
    username = CharField(label='Имя пользователя',
                         widget=TextInput(attrs={
                             'class': 'form-control',
                         }))
    password = CharField(label='Пароль',
                         widget=PasswordInput(attrs={
                              'class': 'form-control'
                          }))


class UserRegisterForm(UserCreationForm):
    username = CharField(label='Имя пользователя',
                         help_text="- Имя пользователя не должен превышать 150 символов",
                         widget=TextInput(attrs={
                             'class': 'form-control',
                         }))
    password1 = CharField(label='Пароль',
                          help_text="- Длина пароля должна быть не меньше 8 символов",
                          widget=PasswordInput(attrs={
                              'class': 'form-control'
                          }))
    password2 = CharField(label='Подтверждение пароля',
                          widget=PasswordInput(attrs={
                              'class': 'form-control'
                          }))
    email = EmailField(label='E-mail',
                       widget=EmailInput(attrs={
                           'class': 'form-control'
                       }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


